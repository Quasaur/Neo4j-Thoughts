#!/usr/bin/env python3.11
"""Fix naming mismatches between files and DB"""

import os
import re
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
PASSAGES_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content/PASSAGES"
QUOTES_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content/QUOTES"

driver = GraphDatabase.driver(URI, auth=AUTH)

def extract_name_from_cypher(filepath):
    """Extract the node name from the Cypher CREATE statement"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'CREATE\s*\(\s*\w+\s*:\s*(?:PASSAGE|QUOTE)\s*\{[^}]*name:\s*"([^"]+)"', content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)
    return None

# Get all expected names from files
expected_passages = {}
for filename in os.listdir(PASSAGES_DIR):
    if filename.endswith('.md'):
        filepath = os.path.join(PASSAGES_DIR, filename)
        name = extract_name_from_cypher(filepath)
        if name:
            expected_passages[name] = filepath

expected_quotes = {}
for filename in os.listdir(QUOTES_DIR):
    if filename.endswith('.md'):
        filepath = os.path.join(QUOTES_DIR, filename)
        name = extract_name_from_cypher(filepath)
        if name:
            expected_quotes[name] = filepath

# Get all actual names from DB
with driver.session() as session:
    result = session.run("MATCH (p:PASSAGE) RETURN p.name as name")
    actual_passages = {record["name"] for record in result}
    
    result = session.run("MATCH (q:QUOTE) RETURN q.name as name")
    actual_quotes = {record["name"] for record in result}

print("="*60)
print("NAMING MISMATCH ANALYSIS")
print("="*60)

print("\n📊 PASSAGE NODES:")
print(f"   Expected from files: {len(expected_passages)}")
print(f"   Actual in DB: {len(actual_passages)}")

missing_passages = set(expected_passages.keys()) - actual_passages
extra_passages = actual_passages - set(expected_passages.keys())
in_sync_passages = set(expected_passages.keys()) & actual_passages

if missing_passages:
    print(f"\n   Missing from DB ({len(missing_passages)}):")
    for name in sorted(missing_passages):
        print(f"      - {name}")

if extra_passages:
    print(f"\n   Extra in DB (to delete) ({len(extra_passages)}):")
    for name in sorted(extra_passages):
        print(f"      - {name}")

print(f"\n   In sync: {len(in_sync_passages)}")

print("\n📊 QUOTE NODES:")
print(f"   Expected from files: {len(expected_quotes)}")
print(f"   Actual in DB: {len(actual_quotes)}")

missing_quotes = set(expected_quotes.keys()) - actual_quotes
extra_quotes = actual_quotes - set(expected_quotes.keys())
in_sync_quotes = set(expected_quotes.keys()) & actual_quotes

if missing_quotes:
    print(f"\n   Missing from DB ({len(missing_quotes)}):")
    for name in sorted(missing_quotes):
        print(f"      - {name}")

if extra_quotes:
    print(f"\n   Extra in DB (to delete) ({len(extra_quotes)}):")
    for name in sorted(extra_quotes):
        print(f"      - {name}")

print(f"\n   In sync: {len(in_sync_quotes)}")

# Create missing PASSAGE nodes
print("\n" + "="*60)
print("CREATING MISSING PASSAGE NODES")
print("="*60)

for name in sorted(missing_passages):
    filepath = expected_passages[name]
    print(f"\n  Creating: {name}")
    
    # Extract full cypher
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cypher_match = re.search(r'```[Cc]ypher\s*\n(.*?)```', content, re.DOTALL)
    if cypher_match:
        cypher = cypher_match.group(1).strip()
        try:
            with driver.session() as session:
                session.run(cypher)
            print(f"    ✓ Created")
        except Exception as e:
            print(f"    ✗ Error: {e}")

# Create missing QUOTE nodes
print("\n" + "="*60)
print("CREATING MISSING QUOTE NODES")
print("="*60)

for name in sorted(missing_quotes):
    filepath = expected_quotes[name]
    print(f"\n  Creating: {name}")
    
    # Extract full cypher
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cypher_match = re.search(r'```[Cc]ypher\s*\n(.*?)```', content, re.DOTALL)
    if cypher_match:
        cypher = cypher_match.group(1).strip()
        try:
            with driver.session() as session:
                session.run(cypher)
            print(f"    ✓ Created")
        except Exception as e:
            print(f"    ✗ Error: {e}")

# Delete extra nodes
print("\n" + "="*60)
print("DELETING EXTRA/ORPHANED NODES")
print("="*60)

# Delete extra PASSAGE nodes
for name in sorted(extra_passages):
    print(f"\n  Deleting PASSAGE: {name}")
    try:
        with driver.session() as session:
            session.run("""
                MATCH (p:PASSAGE {name: $name})
                OPTIONAL MATCH (p)-[r1:HAS_CONTENT]->(c:CONTENT)
                OPTIONAL MATCH (parent:TOPIC)-[r2:HAS_PASSAGE]->(p)
                DELETE r1, r2, c, p
            """, {'name': name})
        print(f"    ✓ Deleted")
    except Exception as e:
        print(f"    ✗ Error: {e}")

# Delete extra QUOTE nodes  
for name in sorted(extra_quotes):
    print(f"\n  Deleting QUOTE: {name}")
    try:
        with driver.session() as session:
            session.run("""
                MATCH (q:QUOTE {name: $name})
                OPTIONAL MATCH (q)-[r1:HAS_CONTENT]->(c:CONTENT)
                OPTIONAL MATCH (parent:TOPIC)-[r2:HAS_QUOTE]->(q)
                DELETE r1, r2, c, q
            """, {'name': name})
        print(f"    ✓ Deleted")
    except Exception as e:
        print(f"    ✗ Error: {e}")

# Final count
print("\n" + "="*60)
print("FINAL COUNTS")
print("="*60)

with driver.session() as session:
    passage_count = session.run("MATCH (p:PASSAGE) RETURN count(p) as count").single()["count"]
    quote_count = session.run("MATCH (q:QUOTE) RETURN count(q) as count").single()["count"]

print(f"PASSAGE nodes: {passage_count}")
print(f"QUOTE nodes: {quote_count}")

driver.close()

print("\n✅ Sync complete!")
