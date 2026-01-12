#!/usr/bin/env python3
"""
Find and list CONTENT nodes in AuraDB that have placeholder translations.
This helps identify which nodes actually need translation updates.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


def find_placeholder_content():
    """Find all CONTENT nodes with placeholder translations."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Get all CONTENT nodes with placeholder translations
            result = session.run("""
                MATCH (c:CONTENT)
                WHERE c.es_title = 'TITULO DEL PENSAMIENTO'
                   OR c.es_content = 'CONTENIDO DEL PENSAMIENTO'
                   OR c.fr_title = 'TITRE DE LA PENSÉE'
                   OR c.zh_title = 'biāo tí'
                RETURN c.name as name, 
                       c.en_title as en_title, 
                       c.en_content as en_content,
                       c.es_title as es_title
                ORDER BY c.name
            """)
            
            records = list(result)
            
            print(f"Found {len(records)} CONTENT nodes with placeholder translations:\n")
            print("=" * 80)
            
            for idx, record in enumerate(records, 1):
                print(f"[{idx}] {record['name']}")
                print(f"    EN Title:   {record['en_title']}")
                print(f"    EN Content: {record['en_content'][:60]}...")
                print(f"    ES Title:   {record['es_title']}")
                print()
            
            print("=" * 80)
            print(f"Total: {len(records)} nodes need translation updates in AuraDB")
            
            return records
    
    finally:
        driver.close()


if __name__ == "__main__":
    find_placeholder_content()
