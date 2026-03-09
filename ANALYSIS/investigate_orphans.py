#!/usr/bin/env python3
"""
Investigate orphaned nodes and sync relationships
"""

from neo4j import GraphDatabase
from pathlib import Path
import re

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

TOPICS_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/content/TOPICS")

def investigate():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        print("=" * 80)
        print("INVESTIGATING ORPHANED NODES")
        print("=" * 80)
        
        with driver.session() as session:
            # Find orphaned THOUGHTs
            print("\n  Orphaned THOUGHT nodes:")
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE NOT (t)<-[:HAS_THOUGHT]-(:TOPIC)
                RETURN t.name as name, t.parent as parent
            """)
            for record in result:
                print(f"    - {record['name']} (parent: {record['parent']})")
            
            # Find orphaned QUOTEs
            print("\n  Orphaned QUOTE nodes:")
            result = session.run("""
                MATCH (q:QUOTE)
                WHERE NOT (q)<-[:HAS_QUOTE]-(:TOPIC)
                RETURN q.name as name, q.parent as parent
            """)
            for record in result:
                print(f"    - {record['name']} (parent: {record['parent']})")
            
            # Find orphaned PASSAGEs
            print("\n  Orphaned PASSAGE nodes:")
            result = session.run("""
                MATCH (p:PASSAGE)
                WHERE NOT (p)<-[:HAS_PASSAGE]-(:TOPIC)
                RETURN p.name as name, p.parent as parent
            """)
            for record in result:
                print(f"    - {record['name']} (parent: {record['parent']})")
            
            # Find topics with missing children
            print("\n  TOPIC nodes with missing HAS_CHILD relationships:")
            result = session.run("""
                MATCH (t:TOPIC)
                WHERE t.parent IS NOT NULL AND t.parent <> 'no parent'
                AND NOT (:TOPIC)-[:HAS_CHILD]->(t)
                RETURN t.name as name, t.parent as parent
            """)
            for record in result:
                print(f"    - {record['name']} (should have parent: {record['parent']})")
                
    finally:
        driver.close()

if __name__ == "__main__":
    investigate()
