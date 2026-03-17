#!/usr/bin/env python3.11
"""Create missing QUOTE nodes with multi-statement Cypher handling"""

import os
import re
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
QUOTES_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content/QUOTES"

driver = GraphDatabase.driver(URI, auth=AUTH)

# Missing QUOTE files
missing_files = [
    "quote-ADOPTION-2.md",
    "quote-CONSEQUENCES-2.md",
    "quote-HEIR-OF-GOD.md",
    "quote-MIRACLES-2.md",
    "quote-WHERE-IS-GOD.md"
]

print("="*60)
print("CREATING MISSING QUOTE NODES")
print("="*60)

for filename in missing_files:
    filepath = os.path.join(QUOTES_DIR, filename)
    print(f"\n  Processing: {filename}")
    
    # Extract full cypher
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cypher_match = re.search(r'```[Cc]ypher\s*\n(.*?)```', content, re.DOTALL)
    if not cypher_match:
        print(f"    ✗ No Cypher block found")
        continue
    
    cypher = cypher_match.group(1).strip()
    
    # Split by semicolons to get individual statements
    statements = [s.strip() for s in cypher.split(';') if s.strip()]
    
    try:
        with driver.session() as session:
            for stmt in statements:
                # Skip comment-only lines
                if stmt.startswith('//') and '\n' not in stmt:
                    continue
                # Remove leading comments from the statement for execution
                stmt_clean = re.sub(r'^\s*//.*\n', '', stmt, flags=re.MULTILINE).strip()
                if stmt_clean:
                    session.run(stmt_clean)
        print(f"    ✓ Created")
    except Exception as e:
        print(f"    ✗ Error: {e}")

# Final count
print("\n" + "="*60)
print("FINAL QUOTE COUNT")
print("="*60)

with driver.session() as session:
    quote_count = session.run("MATCH (q:QUOTE) RETURN count(q) as count").single()["count"]
    print(f"QUOTE nodes: {quote_count}")

driver.close()

print("\n✅ QUOTE creation complete!")
