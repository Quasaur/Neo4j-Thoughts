#!/usr/bin/env python3
"""
Execute edge name property corrections in Neo4j AuraDB.
Reads the generated Cypher script and applies all corrections to the database.
"""

import re
from pathlib import Path
from neo4j import GraphDatabase

# Neo4j connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def parse_cypher_script(script_path):
    """Parse the Cypher script and extract executable statements."""
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    statements = []
    current_comment = None
    
    # Split by lines and process
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and section headers
        if not line or line.startswith('//') and ('====' in line or 'Neo4j' in line or 'NOTE:' in line or 'Execute' in line):
            continue
        
        # Capture comment describing the fix
        if line.startswith('// Fix:'):
            current_comment = line
            continue
        
        # Capture MATCH...SET statement pairs
        if line.startswith('MATCH'):
            # Get the next line which should be the SET
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('SET'):
                    full_statement = f"{line}\n{next_line}"
                    statements.append({
                        'comment': current_comment,
                        'statement': full_statement
                    })
                    current_comment = None
    
    return statements

def execute_corrections(statements):
    """Execute correction statements in Neo4j."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    results = {
        'successful': [],
        'failed': []
    }
    
    try:
        with driver.session() as session:
            for idx, item in enumerate(statements, 1):
                comment = item['comment']
                statement = item['statement']
                
                print(f"[{idx}/{len(statements)}] {comment}")
                
                try:
                    result = session.run(statement)
                    summary = result.consume()
                    
                    # Check if any relationships were updated
                    if summary.counters.properties_set > 0:
                        print(f"  ✅ Updated {summary.counters.properties_set} relationship(s)")
                        results['successful'].append({
                            'comment': comment,
                            'updated': summary.counters.properties_set
                        })
                    else:
                        print(f"  ⚠️  No relationships found to update")
                        results['successful'].append({
                            'comment': comment,
                            'updated': 0
                        })
                
                except Exception as e:
                    print(f"  ❌ Error: {str(e)}")
                    results['failed'].append({
                        'comment': comment,
                        'error': str(e)
                    })
    
    finally:
        driver.close()
    
    return results

def main():
    script_path = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/CYPHER/CORRECTIONS/neo4j_edge_corrections.cypher")
    
    print("=" * 80)
    print("EXECUTING NEO4J AURADB EDGE CORRECTIONS")
    print("=" * 80)
    print()
    
    # Parse script
    print(f"📖 Reading Cypher script: {script_path.name}")
    statements = parse_cypher_script(script_path)
    print(f"   Found {len(statements)} correction statements")
    print()
    
    # Execute corrections
    print("🔧 Executing corrections...")
    print()
    results = execute_corrections(statements)
    
    # Summary
    print()
    print("=" * 80)
    print("EXECUTION SUMMARY")
    print("=" * 80)
    print(f"Total statements executed: {len(statements)}")
    print(f"Successful: {len(results['successful'])}")
    print(f"Failed: {len(results['failed'])}")
    
    # Count total relationships updated
    total_updated = sum(item.get('updated', 0) for item in results['successful'])
    print(f"Total relationships updated: {total_updated}")
    print("=" * 80)
    
    if results['failed']:
        print()
        print("❌ FAILED STATEMENTS:")
        for item in results['failed']:
            print(f"  {item['comment']}")
            print(f"  Error: {item['error']}")
        print()
    
    # Save results
    results_path = script_path.parent / "execution_results.txt"
    with open(results_path, 'w', encoding='utf-8') as f:
        f.write("NEO4J AURADB EDGE CORRECTIONS - EXECUTION RESULTS\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total statements: {len(statements)}\n")
        f.write(f"Successful: {len(results['successful'])}\n")
        f.write(f"Failed: {len(results['failed'])}\n")
        f.write(f"Total relationships updated: {total_updated}\n\n")
        
        if results['failed']:
            f.write("\nFAILED STATEMENTS:\n")
            f.write("-" * 80 + "\n")
            for item in results['failed']:
                f.write(f"{item['comment']}\n")
                f.write(f"Error: {item['error']}\n\n")
    
    print(f"📝 Results saved to: {results_path}")

if __name__ == '__main__':
    main()
