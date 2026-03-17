#!/usr/bin/env python3.11
"""Clean up duplicate PASSAGE nodes with underscores"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

driver = GraphDatabase.driver(URI, auth=AUTH)

# Nodes with underscores to delete (duplicates)
underscore_names = [
    "passage.DISCIPLINE_AND_REBUKE",
    "passage.FATE_OF_THE_WICKED", 
    "passage.FREEDOM_OF_DEATH",
    "passage.MAN_OF_VIOLENCE",
    "passage.PROTECTION_FROM_EVIL"
]

# Also handle passage.SECURITY (2) duplicate
with driver.session() as session:
    print("Cleaning up duplicate PASSAGE nodes...")
    
    # Delete underscore versions
    for name in underscore_names:
        result = session.run("""
            MATCH (p:PASSAGE {name: $name})
            OPTIONAL MATCH (p)-[r1:HAS_CONTENT]->(c:CONTENT)
            OPTIONAL MATCH (parent:TOPIC)-[r2:HAS_PASSAGE]->(p)
            DELETE r1, r2, c, p
        """, {'name': name})
        print(f"  Deleted: {name}")
    
    # Delete the passage.SECURITY (2) duplicate
    result = session.run("""
        MATCH (p:PASSAGE {name: "passage.SECURITY (2)"})
        OPTIONAL MATCH (p)-[r1:HAS_CONTENT]->(c:CONTENT)
        OPTIONAL MATCH (parent:TOPIC)-[r2:HAS_PASSAGE]->(p)
        DELETE r1, r2, c, p
    """)
    print("  Deleted: passage.SECURITY (2)")
    
    # Count remaining
    count = session.run("MATCH (p:PASSAGE) RETURN count(p) as count").single()["count"]
    print(f"\nFinal PASSAGE count: {count}")
    
    # List remaining
    print("\nRemaining PASSAGE nodes:")
    result = session.run("MATCH (p:PASSAGE) RETURN p.name as name ORDER BY name")
    for record in result:
        print(f"  - {record['name']}")

driver.close()
print("\n✓ Cleanup complete!")
