#!/usr/bin/env python3.11
"""Check current state of PASSAGE nodes in Neo4j"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

driver = GraphDatabase.driver(URI, auth=AUTH)

with driver.session() as session:
    result = session.run("MATCH (p:PASSAGE) RETURN p.name as name ORDER BY name")
    print("Current PASSAGE nodes in DB:")
    for record in result:
        print(f"  - {record['name']}")
    
    count = session.run("MATCH (p:PASSAGE) RETURN count(p) as count").single()["count"]
    print(f"\nTotal: {count}")

driver.close()
