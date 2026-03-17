#!/usr/bin/env python3
"""Debug PRIDE passage nodes"""
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def main():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Check for passage.PRIDE nodes
            result = session.run("""
                MATCH (p:PASSAGE)
                WHERE p.name CONTAINS 'PRIDE'
                RETURN p.name as name
            """)
            print("PASSAGE nodes with 'PRIDE' in name:")
            for record in result:
                print(f"  - '{record['name']}'")
            
            # Check if passage.PRIDE AS EVIL exists
            result = session.run("""
                MATCH (p:PASSAGE {name: 'passage.PRIDE AS EVIL'})
                RETURN p.name as name
            """)
            print("\nLooking for 'passage.PRIDE AS EVIL':")
            found = False
            for record in result:
                print(f"  FOUND: '{record['name']}'")
                found = True
            if not found:
                print("  NOT FOUND")
            
            # Check if passage.PRIDE-AS-EVIL exists
            result = session.run("""
                MATCH (p:PASSAGE {name: 'passage.PRIDE-AS-EVIL'})
                RETURN p.name as name
            """)
            print("\nLooking for 'passage.PRIDE-AS-EVIL':")
            found = False
            for record in result:
                print(f"  FOUND: '{record['name']}'")
                found = True
            if not found:
                print("  NOT FOUND")
                
    finally:
        driver.close()

if __name__ == "__main__":
    main()
