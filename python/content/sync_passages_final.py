#!/usr/bin/env python3
"""
Final PASSAGE sync script - syncs content/PASSAGES to AuraDB
"""

import os
import re
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
PASSAGES_DIR = "content/PASSAGES"


def extract_cypher_block(filepath):
    """Extract the Cypher block from markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract Cypher block
    match = re.search(r'```cypher\s*\n(.*?)\n```', content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def extract_name_from_yaml(filepath):
    """Extract passage name from YAML."""
    with open(filepath, 'r') as f:
        content = f.read()
    match = re.search(r'^name:\s*"([^"]+)"', content, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def get_auradb_passage_names(driver):
    """Get all PASSAGE node names from AuraDB."""
    with driver.session() as session:
        result = session.run("MATCH (p:PASSAGE) RETURN p.name as name")
        return [record['name'] for record in result]


def delete_passage_and_content(driver, passage_name):
    """Delete a PASSAGE node and its CONTENT nodes."""
    with driver.session() as session:
        # Delete relationships and nodes
        session.run("""
            MATCH (p:PASSAGE {name: $name})-[r:HAS_CONTENT]->(c:CONTENT)
            DELETE r, c
        """, name=passage_name)
        # Delete any remaining relationships to the passage
        session.run("""
            MATCH (p:PASSAGE {name: $name})-[r]-()
            DELETE r
        """, name=passage_name)
        # Delete the passage node
        session.run("""
            MATCH (p:PASSAGE {name: $name})
            DELETE p
        """, name=passage_name)


def execute_cypher_block(driver, cypher_block):
    """Execute a Cypher block."""
    with driver.session() as session:
        session.run(cypher_block)


def main():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        # Get local files and their passage names
        local_files = {}
        for filename in os.listdir(PASSAGES_DIR):
            if filename.endswith('.md'):
                filepath = os.path.join(PASSAGES_DIR, filename)
                name = extract_name_from_yaml(filepath)
                if name:
                    local_files[name] = filepath
        
        print(f"📁 Local PASSAGE files: {len(local_files)}")
        
        # Get AuraDB passage names
        auradb_names = get_auradb_passage_names(driver)
        print(f"🌐 AuraDB PASSAGE nodes: {len(auradb_names)}")
        
        # Find nodes to delete (in AuraDB but not local)
        to_delete = [n for n in auradb_names if n not in local_files]
        print(f"\n🗑️  To DELETE from AuraDB: {len(to_delete)}")
        for name in to_delete:
            print(f"   - {name}")
            delete_passage_and_content(driver, name)
            print(f"     ✅ Deleted")
        
        # Find nodes to create (in local but not AuraDB)
        to_create = [n for n in local_files.keys() if n not in auradb_names]
        print(f"\n🆕 To CREATE in AuraDB: {len(to_create)}")
        for name in to_create:
            filepath = local_files[name]
            print(f"   - {name}")
            cypher = extract_cypher_block(filepath)
            if cypher:
                try:
                    execute_cypher_block(driver, cypher)
                    print(f"     ✅ Created")
                except Exception as e:
                    print(f"     ❌ Error: {e}")
            else:
                print(f"     ⚠️  No Cypher block found")
        
        # For existing nodes, we need to verify/update their properties
        existing = [n for n in local_files.keys() if n in auradb_names]
        print(f"\n🔄 To VERIFY/UPDATE: {len(existing)}")
        
        # For now, just re-run the Cypher blocks for existing nodes to update properties
        # This is a simple approach - delete and recreate
        for name in existing:
            filepath = local_files[name]
            cypher = extract_cypher_block(filepath)
            if cypher:
                try:
                    # Delete old node and content
                    delete_passage_and_content(driver, name)
                    # Recreate with current Cypher
                    execute_cypher_block(driver, cypher)
                    print(f"   ✅ {name}")
                except Exception as e:
                    print(f"   ❌ {name}: {e}")
        
        # Final count
        final_names = get_auradb_passage_names(driver)
        print(f"\n✅ SYNC COMPLETE")
        print(f"   Total PASSAGE nodes in AuraDB: {len(final_names)}")
        
        if len(final_names) == 28:
            print(f"   🎉 Target achieved!")
        else:
            print(f"   ⚠️  Expected 28, found {len(final_names)}")
            
    finally:
        driver.close()


if __name__ == "__main__":
    main()
