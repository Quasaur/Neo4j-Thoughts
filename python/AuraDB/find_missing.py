#!/usr/bin/env python3.11
"""Find which PASSAGE file is missing from the database"""

import os
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
PASSAGES_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content/PASSAGES"

driver = GraphDatabase.driver(URI, auth=AUTH)

# Get all file names (converting filename to node name format)
file_names = set()
for filename in os.listdir(PASSAGES_DIR):
    if filename.endswith('.md'):
        name_part = filename[8:-3]  # Remove 'passage-' and '.md'
        node_name = "passage." + name_part.replace('-', ' ')
        file_names.add(node_name)

# Get all DB names
with driver.session() as session:
    result = session.run("MATCH (p:PASSAGE) RETURN p.name as name")
    db_names = {record["name"] for record in result}

driver.close()

print("Files not in DB:")
missing = file_names - db_names
for name in sorted(missing):
    print(f"  - {name}")

print(f"\nTotal files: {len(file_names)}")
print(f"Total in DB: {len(db_names)}")
print(f"Missing: {len(missing)}")
