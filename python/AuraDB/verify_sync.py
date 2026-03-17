#!/usr/bin/env python3
"""
Verify Neo4j AuraDB synchronization results
"""

import json
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def verify():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        print("=" * 80)
        print("POST-SYNC VERIFICATION")
        print("=" * 80)
        
        with driver.session() as session:
            # Count nodes after sync
            labels = ["TOPIC", "DESCRIPTION"]
            for label in labels:
                result = session.run(f"MATCH (n:{label}) RETURN count(n) as count")
                count = result.single()["count"]
                print(f"  {label} nodes: {count}")
            
            # Verify all expected TOPICs exist
            print("\n  Verifying all 59 TOPIC nodes...")
            result = session.run("""
                MATCH (t:TOPIC)
                RETURN t.name as name
                ORDER BY t.name
            """)
            topics = [r["name"] for r in result]
            print(f"  Found {len(topics)} TOPIC nodes")
            
            # Check for new topics
            expected_new = ["topic.APOCALYPSE", "topic.BEAUTY", "topic.ECONOMICS", 
                           "topic.ENTITLEMENT", "topic.EVANGELISM", "topic.FIN GOV",
                           "topic.NULL TOPIC", "topic.POLITICAL SCIENCE", "topic.THE BIBLE"]
            
            for topic in expected_new:
                if topic in topics:
                    print(f"    ✓ {topic}")
                else:
                    print(f"    ✗ MISSING: {topic}")
            
            # Verify DESCRIPTION nodes
            print("\n  Verifying DESCRIPTION nodes...")
            result = session.run("""
                MATCH (d:DESCRIPTION)
                RETURN d.name as name
                ORDER BY d.name
            """)
            descs = [r["name"] for r in result]
            print(f"  Found {len(descs)} DESCRIPTION nodes")
            
            # Check relationships
            print("\n  Verifying relationships...")
            result = session.run("""
                MATCH ()-[r:HAS_DESCRIPTION]->()
                RETURN count(r) as count
            """)
            has_desc = result.single()["count"]
            print(f"  HAS_DESCRIPTION relationships: {has_desc}")
            
            result = session.run("""
                MATCH ()-[r:HAS_CHILD]->()
                RETURN count(r) as count
            """)
            has_child = result.single()["count"]
            print(f"  HAS_CHILD relationships: {has_child}")
            
            # Verify THOUGHT nodes still reference valid TOPICs
            print("\n  Verifying THOUGHT parent references...")
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE NOT t.parent STARTS WITH 'topic.'
                RETURN t.name as name, t.parent as parent
                LIMIT 10
            """)
            invalid_parents = list(result)
            if invalid_parents:
                print(f"  Found {len(invalid_parents)} THOUGHTs with invalid parent format")
                for item in invalid_parents:
                    print(f"    - {item['name']}: {item['parent']}")
            else:
                print("  All THOUGHT nodes have valid parent format")
            
            # Check for orphaned THOUGHTs
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE NOT (t)<-[:HAS_THOUGHT]-(:TOPIC)
                RETURN count(t) as count
            """)
            orphaned = result.single()["count"]
            print(f"  Orphaned THOUGHT nodes: {orphaned}")
            
    finally:
        driver.close()

if __name__ == "__main__":
    verify()
