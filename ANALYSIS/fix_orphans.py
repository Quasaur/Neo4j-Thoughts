#!/usr/bin/env python3
"""
Fix orphaned nodes by updating parent references and creating relationships
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def fix_orphans():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    # Map of incorrect parent names to correct ones
    parent_corrections = {
        "topic.THE-BIBLE": "topic.THE BIBLE",
        "topic.POLITICAL-SCIENCE": "topic.POLITICAL SCIENCE",
        "topic.FIN-GOV": "topic.FIN GOV"
    }
    
    try:
        print("=" * 80)
        print("FIXING ORPHANED NODES")
        print("=" * 80)
        
        with driver.session() as session:
            # Fix THOUGHT nodes
            print("\n  Fixing THOUGHT nodes...")
            thoughts_fixed = 0
            for old_parent, new_parent in parent_corrections.items():
                result = session.run("""
                    MATCH (t:THOUGHT)
                    WHERE t.parent = $old_parent
                    SET t.parent = $new_parent
                    RETURN t.name as name
                """, old_parent=old_parent, new_parent=new_parent)
                
                for record in result:
                    print(f"    Updated: {record['name']} -> parent: {new_parent}")
                    thoughts_fixed += 1
            
            print(f"  Fixed {thoughts_fixed} THOUGHT nodes")
            
            # Fix QUOTE nodes
            print("\n  Fixing QUOTE nodes...")
            quotes_fixed = 0
            for old_parent, new_parent in parent_corrections.items():
                result = session.run("""
                    MATCH (q:QUOTE)
                    WHERE q.parent = $old_parent
                    SET q.parent = $new_parent
                    RETURN q.name as name
                """, old_parent=old_parent, new_parent=new_parent)
                
                for record in result:
                    print(f"    Updated: {record['name']} -> parent: {new_parent}")
                    quotes_fixed += 1
            
            print(f"  Fixed {quotes_fixed} QUOTE nodes")
            
            # Create missing HAS_THOUGHT relationships
            print("\n  Creating missing HAS_THOUGHT relationships...")
            result = session.run("""
                MATCH (t:THOUGHT)
                MATCH (p:TOPIC {name: t.parent})
                WHERE NOT (p)-[:HAS_THOUGHT]->(t)
                MERGE (p)-[r:HAS_THOUGHT]->(t)
                SET r.name = "t.edge." + replace(t.parent, "topic.", "") + "->" + replace(t.name, "thought.", "")
                RETURN t.name as thought, p.name as parent
            """)
            rels_created = 0
            for record in result:
                print(f"    Created: {record['parent']} -> HAS_THOUGHT -> {record['thought']}")
                rels_created += 1
            print(f"  Created {rels_created} HAS_THOUGHT relationships")
            
            # Create missing HAS_QUOTE relationships
            print("\n  Creating missing HAS_QUOTE relationships...")
            result = session.run("""
                MATCH (q:QUOTE)
                MATCH (p:TOPIC {name: q.parent})
                WHERE NOT (p)-[:HAS_QUOTE]->(q)
                MERGE (p)-[r:HAS_QUOTE]->(q)
                SET r.name = "q.edge." + replace(q.parent, "topic.", "") + "->" + replace(q.name, "quote.", "")
                RETURN q.name as quote, p.name as parent
            """)
            rels_created = 0
            for record in result:
                print(f"    Created: {record['parent']} -> HAS_QUOTE -> {record['quote']}")
                rels_created += 1
            print(f"  Created {rels_created} HAS_QUOTE relationships")
            
            # Verify no more orphans
            print("\n  Verifying fix...")
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE NOT (t)<-[:HAS_THOUGHT]-(:TOPIC)
                RETURN count(t) as count
            """)
            orphaned_thoughts = result.single()["count"]
            
            result = session.run("""
                MATCH (q:QUOTE)
                WHERE NOT (q)<-[:HAS_QUOTE]-(:TOPIC)
                RETURN count(q) as count
            """)
            orphaned_quotes = result.single()["count"]
            
            print(f"  Remaining orphaned THOUGHTs: {orphaned_thoughts}")
            print(f"  Remaining orphaned QUOTEs: {orphaned_quotes}")
            
    finally:
        driver.close()

if __name__ == "__main__":
    fix_orphans()
