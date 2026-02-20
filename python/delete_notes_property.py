#!/usr/bin/env python3
"""
Delete the 'notes' property from Topics, Thoughts, Quotes, and Passages nodes in AuraDB.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


def delete_notes_property():
    """Query and delete the 'notes' property from specified node types."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    node_types = ["TOPIC", "THOUGHT", "QUOTE", "PASSAGE"]
    
    try:
        with driver.session() as session:
            print("=" * 70)
            print("Scanning for 'notes' property in AuraDB nodes...")
            print("=" * 70)
            
            total_affected = 0
            
            for node_type in node_types:
                # First, count nodes with the 'notes' property
                count_query = f"""
                    MATCH (n:{node_type})
                    WHERE n.notes IS NOT NULL
                    RETURN count(n) as count
                """
                result = session.run(count_query)
                count = result.single()['count']
                print(f"\n{node_type} nodes with 'notes' property: {count}")
                
                if count > 0:
                    # Sample a few to show what we're deleting
                    sample_query = f"""
                        MATCH (n:{node_type})
                        WHERE n.notes IS NOT NULL
                        RETURN n.name as name, n.notes as notes
                        LIMIT 3
                    """
                    result = session.run(sample_query)
                    print(f"  Sample values:")
                    for record in result:
                        notes_preview = str(record['notes'])[:80] + "..." if len(str(record['notes'])) > 80 else str(record['notes'])
                        print(f"    - {record['name']}: {notes_preview}")
                    
                    # Delete the property
                    delete_query = f"""
                        MATCH (n:{node_type})
                        WHERE n.notes IS NOT NULL
                        REMOVE n.notes
                        RETURN count(n) as deleted
                    """
                    result = session.run(delete_query)
                    deleted = result.single()['deleted']
                    print(f"  ✅ Deleted 'notes' property from {deleted} {node_type} nodes")
                    total_affected += deleted
                else:
                    print(f"  (No nodes with 'notes' property)")
            
            print("\n" + "=" * 70)
            print(f"COMPLETE! Total nodes updated: {total_affected}")
            print("=" * 70)
    
    finally:
        driver.close()


if __name__ == "__main__":
    delete_notes_property()
