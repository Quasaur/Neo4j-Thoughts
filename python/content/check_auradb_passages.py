#!/usr/bin/env python3
"""
Check PASSAGE nodes in AuraDB and compare with content/PASSAGES
"""

import os
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

PASSAGES_DIR = "content/PASSAGES"


def get_all_auradb_passages(driver):
    """Get all PASSAGE nodes from AuraDB."""
    with driver.session() as session:
        result = session.run("""
            MATCH (p:PASSAGE)
            RETURN p.name as name
            ORDER BY p.name
        """)
        return [record['name'] for record in result]


def get_local_passage_names():
    """Get all passage names from markdown files."""
    import re
    names = []
    for filename in os.listdir(PASSAGES_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(PASSAGES_DIR, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            # Extract name from YAML
            match = re.search(r'^name:\s*"([^"]+)"', content, re.MULTILINE)
            if match:
                names.append(match.group(1))
    return sorted(names)


def main():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        auradb_names = get_all_auradb_passages(driver)
        local_names = get_local_passage_names()
        
        print("=== PASSAGE NODES COMPARISON ===\n")
        
        print(f"Local files in {PASSAGES_DIR}: {len(local_names)}")
        for name in local_names:
            status = "✓" if name in auradb_names else "✗ MISSING"
            print(f"  {status} {name}")
        
        print(f"\nAuraDB PASSAGE nodes: {len(auradb_names)}")
        
        # Find extra nodes in AuraDB
        extra_in_auradb = [n for n in auradb_names if n not in local_names]
        if extra_in_auradb:
            print(f"\n⚠️  EXTRA nodes in AuraDB (not in local files): {len(extra_in_auradb)}")
            for name in extra_in_auradb:
                print(f"    - {name}")
        
        # Find missing nodes
        missing_in_auradb = [n for n in local_names if n not in auradb_names]
        if missing_in_auradb:
            print(f"\n⚠️  MISSING nodes in AuraDB (exist locally): {len(missing_in_auradb)}")
            for name in missing_in_auradb:
                print(f"    - {name}")
        
        print(f"\n=== SUMMARY ===")
        print(f"Local: {len(local_names)}, AuraDB: {len(auradb_names)}")
        print(f"To delete from AuraDB: {len(extra_in_auradb)}")
        print(f"To add to AuraDB: {len(missing_in_auradb)}")
        
    finally:
        driver.close()


if __name__ == "__main__":
    main()
