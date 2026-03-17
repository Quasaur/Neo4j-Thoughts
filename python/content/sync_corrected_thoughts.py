#!/usr/bin/env python3
"""
Sync corrected THOUGHT markdown files to Neo4j AuraDB.

Reads Cypher blocks from markdown files, compares with current Neo4j values,
and updates any mismatched fields in the database.
"""

import re
from pathlib import Path
from neo4j import GraphDatabase

# Neo4j connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Files to process (from rss_weirdos.md)
THOUGHT_FILES = [
    "death-row.md",
    "divine-worth.md",
    "unfair.md",
    "quiet-the-flesh.md",
    "self-denial.md",
    "reaction.md",
    "first-rule.md",
    "the-irc.md",
    "another-sinner.md",
    "forbidden.md",
    "insatiable.md",
    "shocked.md",
    "the-end-of-evil.md",
]

def parse_markdown_cypher(file_path):
    """Parse Cypher block from markdown file to extract expected values."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Cypher block
    cypher_match = re.search(r'```Cypher\n(.*?)\n```', content, re.DOTALL)
    if not cypher_match:
        return None
    
    cypher_block = cypher_match.group(1)
    
    # Parse THOUGHT node properties
    thought_match = re.search(
        r'CREATE \(t:THOUGHT \{(.*?)\}\);',
        cypher_block,
        re.DOTALL
    )
    
    # Parse CONTENT node properties
    content_match = re.search(
        r'CREATE \(c:CONTENT \{(.*?)\}\);',
        cypher_block,
        re.DOTALL
    )
    
    if not thought_match or not content_match:
        return None
    
    thought_props = parse_properties(thought_match.group(1))
    content_props = parse_properties(content_match.group(1))
    
    return {
        'thought': thought_props,
        'content': content_props
    }

def parse_properties(props_str):
    """Parse property string from Cypher CREATE statement."""
    props = {}
    
    # Parse simple string values (quoted)
    for match in re.finditer(r'(\w+):\s*"([^"]*)"', props_str):
        key, value = match.groups()
        props[key] = value
    
    # Parse array values
    for match in re.finditer(r'(\w+):\s*\[(.*?)\]', props_str):
        key, array_str = match.groups()
        # Extract quoted strings from array
        array_values = re.findall(r'"([^"]*)"', array_str)
        props[key] = array_values
    
    # Parse numeric values
    for match in re.finditer(r'(\w+):\s*(\d+)(?=\s*[,}])', props_str):
        key, value = match.groups()
        props[key] = int(value)
    
    return props

def get_current_values(session, thought_name, content_name):
    """Query Neo4j to get current property values."""
    query = """
    MATCH (t:THOUGHT {name: $thought_name})
    OPTIONAL MATCH (t)-[:HAS_CONTENT]->(c:CONTENT {name: $content_name})
    RETURN t, c
    """
    
    result = session.run(query, thought_name=thought_name, content_name=content_name)
    record = result.single()
    
    if not record:
        return None, None
    
    thought_node = dict(record['t']) if record['t'] else None
    content_node = dict(record['c']) if record['c'] else None
    
    return thought_node, content_node

def compare_and_generate_updates(expected, current, node_name, node_label):
    """Compare expected vs current values and generate UPDATE statements."""
    if not current:
        print(f"  ⚠️  {node_label} node not found: {node_name}")
        return []
    
    updates = []
    
    for key, expected_value in expected.items():
        current_value = current.get(key)
        
        # Compare values
        if current_value != expected_value:
            updates.append({
                'key': key,
                'expected': expected_value,
                'current': current_value,
                'node_name': node_name,
                'node_label': node_label
            })
    
    return updates

def execute_updates(session, updates, dry_run=True):
    """Execute UPDATE statements for mismatched properties."""
    results = {
        'updated': [],
        'failed': []
    }
    
    for update in updates:
        node_name = update['node_name']
        node_label = update['node_label']
        key = update['key']
        expected = update['expected']
        current = update['current']
        
        # Create UPDATE query
        query = f"""
        MATCH (n:{node_label} {{name: $node_name}})
        SET n.{key} = $value
        RETURN n
        """
        
        if dry_run:
            print(f"  [DRY RUN] Would update {node_label}.{key}")
            print(f"    Current: {current}")
            print(f"    New:     {expected}")
        else:
            try:
                result = session.run(query, node_name=node_name, value=expected)
                result.consume()
                results['updated'].append(update)
                print(f"  ✅ Updated {node_label}.{key}")
            except Exception as e:
                results['failed'].append({
                    'update': update,
                    'error': str(e)
                })
                print(f"  ❌ Failed to update {node_label}.{key}: {str(e)}")
    
    return results

def process_file(file_path, session, dry_run=True):
    """Process a single markdown file."""
    print(f"\n📄 Processing: {file_path.name}")
    
    # Parse expected values from markdown
    expected = parse_markdown_cypher(file_path)
    if not expected:
        print(f"  ❌ Could not parse Cypher block")
        return None
    
    thought_name = expected['thought'].get('name')
    content_name = expected['content'].get('name')
    
    if not thought_name or not content_name:
        print(f"  ❌ Could not extract node names")
        return None
    
    print(f"  THOUGHT: {thought_name}")
    print(f"  CONTENT: {content_name}")
    
    # Get current values from Neo4j
    current_thought, current_content = get_current_values(session, thought_name, content_name)
    
    # Compare and generate updates
    thought_updates = compare_and_generate_updates(
        expected['thought'],
        current_thought,
        thought_name,
        'THOUGHT'
    )
    
    content_updates = compare_and_generate_updates(
        expected['content'],
        current_content,
        content_name,
        'CONTENT'
    )
    
    all_updates = thought_updates + content_updates
    
    if not all_updates:
        print(f"  ✅ No updates needed - all fields match!")
        return {'file': file_path.name, 'updates': 0}
    
    print(f"  🔧 Found {len(all_updates)} field(s) to update")
    
    # Execute updates
    results = execute_updates(session, all_updates, dry_run=dry_run)
    
    return {
        'file': file_path.name,
        'updates': len(all_updates),
        'results': results
    }

def main(dry_run=True):
    """Main execution function."""
    base_path = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS")
    
    print("=" * 80)
    print("SYNCING CORRECTED THOUGHTS TO NEO4J AURADB")
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
    print("=" * 80)
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    all_results = []
    
    try:
        with driver.session() as session:
            for filename in THOUGHT_FILES:
                file_path = base_path / filename
                
                if not file_path.exists():
                    print(f"\n❌ File not found: {filename}")
                    continue
                
                result = process_file(file_path, session, dry_run=dry_run)
                if result:
                    all_results.append(result)
        
        # Summary
        print("\n" + "=" * 80)
        print("SYNC SUMMARY")
        print("=" * 80)
        print(f"Files processed: {len(all_results)}")
        
        total_updates = sum(r['updates'] for r in all_results)
        print(f"Total fields to update: {total_updates}")
        
        if dry_run:
            print("\n💡 Run with dry_run=False to apply changes")
        else:
            print("\n✅ Sync complete!")
        
        print("=" * 80)
        
    finally:
        driver.close()

if __name__ == '__main__':
    # Execute actual updates
    main(dry_run=False)
