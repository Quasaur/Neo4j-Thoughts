#!/usr/bin/env python3
"""
Create missing HAS_THOUGHT relationships for the 13 synced thoughts.
Extracts relationship creation logic from Cypher blocks in markdown files.
"""

import re
from pathlib import Path
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

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

def parse_relationships_from_markdown(file_path):
    """Extract relationship creation statements from Cypher block."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Cypher block
    cypher_match = re.search(r'```Cypher\n(.*?)\n```', content, re.DOTALL)
    if not cypher_match:
        return None
    
    cypher_block = cypher_match.group(1)
    
    # Extract HAS_THOUGHT relationship creation
    # Pattern: MATCH (parent:TOPIC) MATCH (child:THOUGHT) WHERE ... MERGE (parent)-[:HAS_THOUGHT {...}]->(child);
    has_thought_match = re.search(
        r'MATCH \(parent:TOPIC\)\s+MATCH \(child:THOUGHT\)\s+WHERE parent\.name = "([^"]+)" AND child\.name = "([^"]+)"\s+MERGE \(parent\)-\[:HAS_THOUGHT \{name: "([^"]+)"\}\]->\(child\);',
        cypher_block,
        re.DOTALL
    )
    
    if has_thought_match:
        parent_name = has_thought_match.group(1)
        child_name = has_thought_match.group(2)
        edge_name = has_thought_match.group(3)
        return {
            'parent': parent_name,
            'child': child_name,
            'edge_name': edge_name
        }
    
    return None

def create_relationship(session, parent_name, child_name, edge_name):
    """Create HAS_THOUGHT relationship between parent topic and child thought."""
    query = """
    MATCH (parent:TOPIC {name: $parent_name})
    MATCH (child:THOUGHT {name: $child_name})
    MERGE (parent)-[r:HAS_THOUGHT {name: $edge_name}]->(child)
    RETURN r
    """
    
    result = session.run(query, parent_name=parent_name, child_name=child_name, edge_name=edge_name)
    return result.single()

def main():
    """Create all missing HAS_THOUGHT relationships."""
    base_path = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS")
    
    print("=" * 80)
    print("CREATING MISSING HAS_THOUGHT RELATIONSHIPS")
    print("=" * 80)
    print()
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    results = {
        'created': [],
        'failed': []
    }
    
    try:
        with driver.session() as session:
            for filename in THOUGHT_FILES:
                file_path = base_path / filename
                
                if not file_path.exists():
                    print(f"❌ File not found: {filename}")
                    continue
                
                print(f"📄 Processing: {filename}")
                
                # Parse relationship from Cypher block
                rel_info = parse_relationships_from_markdown(file_path)
                
                if not rel_info:
                    print(f"  ⚠️  Could not parse HAS_THOUGHT relationship")
                    continue
                
                parent_name = rel_info['parent']
                child_name = rel_info['child']
                edge_name = rel_info['edge_name']
                
                print(f"  Creating: {parent_name} -[HAS_THOUGHT]-> {child_name}")
                print(f"  Edge name: {edge_name}")
                
                try:
                    result = create_relationship(session, parent_name, child_name, edge_name)
                    if result:
                        print(f"  ✅ Relationship created/verified")
                        results['created'].append({
                            'file': filename,
                            'parent': parent_name,
                            'child': child_name,
                            'edge_name': edge_name
                        })
                    else:
                        print(f"  ❌ Failed to create relationship")
                        results['failed'].append({
                            'file': filename,
                            'error': 'No result returned'
                        })
                except Exception as e:
                    print(f"  ❌ Error: {str(e)}")
                    results['failed'].append({
                        'file': filename,
                        'error': str(e)
                    })
                
                print()
        
        # Summary
        print("=" * 80)
        print("RELATIONSHIP CREATION SUMMARY")
        print("=" * 80)
        print(f"Files processed: {len(THOUGHT_FILES)}")
        print(f"Relationships created/verified: {len(results['created'])}")
        print(f"Failed: {len(results['failed'])}")
        
        if results['failed']:
            print("\n❌ FAILURES:")
            for item in results['failed']:
                print(f"  {item['file']}: {item['error']}")
        else:
            print("\n✅ All HAS_THOUGHT relationships created successfully!")
        
        print("=" * 80)
        
    finally:
        driver.close()

if __name__ == '__main__':
    main()
