#!/usr/bin/env python3
"""
Execute Cypher UPDATE queries on Neo4j AuraDB to add missing PASSAGE translations.
"""

from neo4j import GraphDatabase
from pathlib import Path

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


def execute_cypher_updates():
    """Execute Cypher UPDATE queries on Neo4j."""
    
    cypher_file = Path("CYPHER/UPDATES/passage_translations_update.cypher")
    
    if not cypher_file.exists():
        print(f"❌ Cypher file not found: {cypher_file}")
        return
    
    # Read the Cypher file
    with open(cypher_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
    
    # Split into individual queries (separated by double newlines)
    queries = []
    current_query = []
    
    for line in full_content.split('\n'):
        if line.strip().startswith('//'):
            continue  # Skip comments
        
        if line.strip():
            current_query.append(line)
        elif current_query:
            query_text = '\n'.join(current_query)
            if 'MATCH' in query_text:  # Only add actual queries
                queries.append(query_text)
            current_query = []
    
    # Add last query if exists
    if current_query:
        query_text = '\n'.join(current_query)
        if 'MATCH' in query_text:
            queries.append(query_text)
    
    print("=" * 80)
    print("Executing Cypher UPDATE Queries on Neo4j AuraDB")
    print("=" * 80)
    print(f"Total queries to execute: {len(queries)}")
    print()
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            success_count = 0
            failed_count = 0
            
            for i, query in enumerate(queries, 1):
                # Skip verification query (last one)
                if 'WHERE c.es_title IS NULL' in query:
                    print(f"\n[VERIFICATION] Running final verification query...")
                    result = session.run(query)
                    records = list(result)
                    
                    if len(records) == 0:
                        print("✅ All PASSAGE CONTENT nodes have complete translations!")
                    else:
                        print(f"⚠️  Found {len(records)} PASSAGE(s) still missing translations:")
                        for record in records:
                            print(f"  - {record['passage_name']}")
                    continue
                
                try:
                    result = session.run(query)
                    record = result.single()
                    
                    if record:
                        print(f"[{i}/{len(queries)-1}] ✅ Updated: {record['updated']}")
                        success_count += 1
                    else:
                        print(f"[{i}/{len(queries)-1}] ⚠️  No record returned")
                        failed_count += 1
                        
                except Exception as e:
                    print(f"[{i}/{len(queries)-1}] ❌ Error: {e}")
                    failed_count += 1
            
            print("\n" + "=" * 80)
            print("NEO4J UPDATE COMPLETE!")
            print("=" * 80)
            print(f"Successfully updated: {success_count}")
            print(f"Failed: {failed_count}")
            print("=" * 80)
            
    finally:
        driver.close()


if __name__ == "__main__":
    execute_cypher_updates()
