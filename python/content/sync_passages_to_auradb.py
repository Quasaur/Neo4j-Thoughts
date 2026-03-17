#!/usr/bin/env python3
"""
Sync PASSAGE nodes from content/PASSAGES to Neo4j AuraDB.
- Upload missing PASSAGE nodes
- Update existing PASSAGE nodes and their CONTENT nodes to match markdown files
- Target: 28 PASSAGE nodes in AuraDB
"""

import os
import re
from neo4j import GraphDatabase

# AuraDB connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

PASSAGES_DIR = "content/PASSAGES"


def extract_yaml_and_cypher(filepath):
    """Extract YAML frontmatter and Cypher block from markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    yaml_content = yaml_match.group(1) if yaml_match else ""
    
    # Parse YAML into dict
    yaml_data = {}
    for line in yaml_content.split('\n'):
        if ':' in line and not line.strip().startswith('#'):
            key, value = line.split(':', 1)
            yaml_data[key.strip()] = value.strip().strip('"').strip("'")
    
    # Extract Cypher block
    cypher_match = re.search(r'```cypher\s*\n(.*?)\n```', content, re.DOTALL | re.IGNORECASE)
    cypher_block = cypher_match.group(1) if cypher_match else ""
    
    return yaml_data, cypher_block


def get_passage_name_from_yaml(yaml_data):
    """Get passage name from YAML data."""
    return yaml_data.get('name', '')


def get_all_auradb_passages(driver):
    """Get all PASSAGE nodes from AuraDB."""
    with driver.session() as session:
        result = session.run("""
            MATCH (p:PASSAGE)
            RETURN p.name as name, p.alias as alias, p.parent as parent, 
                   p.sortedsource as sortedsource, p.level as level, p.tags as tags
        """)
        passages = {}
        for record in result:
            passages[record['name']] = {
                'alias': record['alias'],
                'parent': record['parent'],
                'sortedsource': record['sortedsource'],
                'level': record['level'],
                'tags': record['tags']
            }
        return passages


def get_passage_content_nodes(driver, passage_name):
    """Get CONTENT nodes connected to a PASSAGE."""
    with driver.session() as session:
        result = session.run("""
            MATCH (p:PASSAGE {name: $name})-[:HAS_CONTENT]->(c:CONTENT)
            RETURN c.name as name, c.en_content as en_content, c.en_title as en_title,
                   c.es_content as es_content, c.es_title as es_title,
                   c.fr_content as fr_content, c.fr_title as fr_title,
                   c.hi_content as hi_content, c.hi_title as hi_title,
                   c.zh_content as zh_content, c.zh_title as zh_title
        """, name=passage_name)
        contents = {}
        for record in result:
            contents[record['name']] = {
                'en_content': record['en_content'],
                'en_title': record['en_title'],
                'es_content': record['es_content'],
                'es_title': record['es_title'],
                'fr_content': record['fr_content'],
                'fr_title': record['fr_title'],
                'hi_content': record['hi_content'],
                'hi_title': record['hi_title'],
                'zh_content': record['zh_content'],
                'zh_title': record['zh_title']
            }
        return contents


def extract_properties_from_cypher(cypher_block):
    """Extract properties from Cypher CREATE statement."""
    # Extract PASSAGE node properties
    passage_match = re.search(r'CREATE \(\w+:PASSAGE \{([^}]+)\}', cypher_block, re.DOTALL)
    passage_props = {}
    if passage_match:
        props_text = passage_match.group(1)
        # Parse key-value pairs
        for match in re.finditer(r'(\w+):\s*"([^"]*)"', props_text):
            passage_props[match.group(1)] = match.group(2)
        for match in re.finditer(r'(\w+):\s*(\d+)', props_text):
            passage_props[match.group(1)] = int(match.group(2))
        # Parse tags array
        tags_match = re.search(r'tags:\s*(\[[^\]]*\])', props_text)
        if tags_match:
            tags_str = tags_match.group(1)
            passage_props['tags'] = [t.strip().strip('"') for t in tags_str.strip('[]').split(',') if t.strip()]
    
    # Extract CONTENT node properties
    content_match = re.search(r'CREATE \([a-z]:CONTENT \{([^}]+)\}', cypher_block, re.DOTALL)
    content_props = {}
    if content_match:
        props_text = content_match.group(1)
        # For CONTENT, we need to handle multiline strings
        lines = props_text.split('\n')
        current_key = None
        current_value = []
        
        for line in lines:
            if ':' in line:
                # Save previous if exists
                if current_key and current_value:
                    content_props[current_key] = '\n'.join(current_value).strip().strip('"')
                # Start new key
                key, val = line.split(':', 1)
                current_key = key.strip()
                current_value = [val.strip().strip('"')]
            elif current_key:
                current_value.append(line.strip())
        
        if current_key and current_value:
            content_props[current_key] = '\n'.join(current_value).strip().strip('"')
    
    return passage_props, content_props


def update_passage_node(driver, name, props):
    """Update PASSAGE node properties."""
    with driver.session() as session:
        # Build SET clause
        set_clauses = []
        params = {'name': name}
        for key, value in props.items():
            if key != 'name':
                set_clauses.append(f"p.{key} = ${key}")
                params[key] = value
        
        if set_clauses:
            query = f"""
                MATCH (p:PASSAGE {{name: $name}})
                SET {', '.join(set_clauses)}
            """
            session.run(query, **params)


def update_content_node(driver, name, props):
    """Update CONTENT node properties."""
    with driver.session() as session:
        set_clauses = []
        params = {'name': name}
        for key, value in props.items():
            if key != 'name':
                set_clauses.append(f"c.{key} = ${key}")
                params[key] = value
        
        if set_clauses:
            query = f"""
                MATCH (c:CONTENT {{name: $name}})
                SET {', '.join(set_clauses)}
            """
            session.run(query, **params)


def create_passage_and_content(driver, cypher_block):
    """Execute Cypher to create PASSAGE and CONTENT nodes."""
    with driver.session() as session:
        # Run the entire Cypher block
        session.run(cypher_block)


def sync_passages():
    """Main sync function."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        # Get all markdown files in content/PASSAGES
        md_files = [f for f in os.listdir(PASSAGES_DIR) if f.endswith('.md')]
        print(f"Found {len(md_files)} markdown files in {PASSAGES_DIR}")
        
        # Get all PASSAGE nodes from AuraDB
        auradb_passages = get_all_auradb_passages(driver)
        print(f"Found {len(auradb_passages)} PASSAGE nodes in AuraDB")
        
        # Track statistics
        to_create = []
        to_update = []
        
        for md_file in md_files:
            filepath = os.path.join(PASSAGES_DIR, md_file)
            yaml_data, cypher_block = extract_yaml_and_cypher(filepath)
            
            passage_name = get_passage_name_from_yaml(yaml_data)
            if not passage_name:
                print(f"⚠️  Skipping {md_file} - no name in YAML")
                continue
            
            if passage_name not in auradb_passages:
                to_create.append((md_file, passage_name, cypher_block))
            else:
                to_update.append((md_file, passage_name, cypher_block, auradb_passages[passage_name]))
        
        print(f"\n📊 SYNC SUMMARY:")
        print(f"   - Files to create: {len(to_create)}")
        print(f"   - Files to update: {len(to_update)}")
        
        # Create missing nodes
        if to_create:
            print(f"\n🆕 CREATING {len(to_create)} new PASSAGE nodes:")
            for md_file, passage_name, cypher_block in to_create:
                print(f"   Creating: {passage_name}")
                try:
                    create_passage_and_content(driver, cypher_block)
                    print(f"   ✅ Created successfully")
                except Exception as e:
                    print(f"   ❌ Error creating {passage_name}: {e}")
        
        # Update existing nodes
        if to_update:
            print(f"\n🔄 UPDATING {len(to_update)} existing PASSAGE nodes:")
            for md_file, passage_name, cypher_block, auradb_data in to_update:
                print(f"   Checking: {passage_name}")
                try:
                    passage_props, content_props = extract_properties_from_cypher(cypher_block)
                    
                    # Update PASSAGE node
                    update_passage_node(driver, passage_name, passage_props)
                    
                    # Get CONTENT node name and update
                    if content_props and 'name' in content_props:
                        content_name = content_props['name']
                        update_content_node(driver, content_name, content_props)
                    
                    print(f"   ✅ Updated successfully")
                except Exception as e:
                    print(f"   ❌ Error updating {passage_name}: {e}")
        
        # Final count
        final_passages = get_all_auradb_passages(driver)
        print(f"\n✅ SYNC COMPLETE")
        print(f"   Total PASSAGE nodes in AuraDB: {len(final_passages)}")
        
        if len(final_passages) != 28:
            print(f"   ⚠️  WARNING: Expected 28 nodes, found {len(final_passages)}")
        
    finally:
        driver.close()


if __name__ == "__main__":
    sync_passages()
