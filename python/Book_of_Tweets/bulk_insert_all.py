#!/usr/bin/env python3
"""
Bulk insert nodes from Book_of_Tweets into Neo4j AuraDB.
Process ONLY files with properly populated ptopic values (quoted strings).
"""
import os
import re
from pathlib import Path
from neo4j import GraphDatabase

# Neo4j connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Directories
BOOK_OF_TWEETS_BASE = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets")
CONTENT_THOUGHTS_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS")
CONTENT_PASSAGES_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/PASSAGES")

def has_valid_ptopic(content):
    """Check if file has a properly populated ptopic value (not empty, not just quotes)."""
    match = re.search(r'^ptopic:\s*"(.+)"', content, re.MULTILINE)
    if match:
        value = match.group(1).strip()
        # Must have actual content (not empty brackets or invalid values)
        if value and value not in ['', '[[]]', 'type: THOUGHT', 'type: PASSAGE']:
            return True
    return False

def extract_cypher(content):
    """Extract Cypher query from markdown code block."""
    match = re.search(r'```[Cc]ypher\s*(.*?)\s*```', content, re.DOTALL)
    if match:
        cypher = match.group(1).strip()
        # Fix quoted property keys
        cypher = re.sub(r'\{\s*"name":\s*', '{ name: ', cypher)
        return cypher
    return None

def execute_cypher(cypher):
    """Execute Cypher statements in Neo4j."""
    statements = [s.strip() for s in cypher.split('\n\n') if s.strip() and not s.strip().startswith('//')]
    driver = GraphDatabase.driver(URI, auth=AUTH)
    try:
        with driver.session() as session:
            for stmt in statements:
                if stmt:
                    session.run(stmt)
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        driver.close()

def update_and_move_file(file_path, content, dest_dir):
    """Update neo4j property and move file to destination."""
    updated_content = re.sub(r'neo4j:\s*false', 'neo4j: true', content)
    dest_path = dest_dir / file_path.name
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    file_path.unlink()  # Remove from Book_of_Tweets
    return dest_path

def process_directory(dir_path, node_type, dest_dir):
    """Process all files in directory with valid ptopic."""
    results = {'successful': [], 'failed': []}
    
    if not dir_path.exists():
        print(f"⚠️  Directory not found: {dir_path}")
        return results
    
    files = sorted(dir_path.rglob('*.md'))
    valid_files = []
    
    # First pass: identify valid files
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if has_valid_ptopic(content):
            valid_files.append((file_path, content))
    
    print(f"\n{'='*80}")
    print(f"Processing {node_type} files from {dir_path.name}/")
    print(f"{'='*80}")
    print(f"Found {len(valid_files)} files with valid ptopic values\n")
    
    # Second pass: process each valid file
    for idx, (file_path, content) in enumerate(valid_files, 1):
        file_name = file_path.name
        print(f"[{idx}/{len(valid_files)}] {file_name}...", end=" ")
        
        cypher = extract_cypher(content)
        if not cypher:
            print("❌ No Cypher block")
            results['failed'].append({'file': file_name, 'error': 'No Cypher block'})
            continue
        
        success, error = execute_cypher(cypher)
        if not success:
            print(f"❌ Insert failed: {error}")
            results['failed'].append({'file': file_name, 'error': error})
            continue
        
        try:
            dest_path = update_and_move_file(file_path, content, dest_dir)
            print("✅ SUCCESS")
            results['successful'].append(file_name)
        except Exception as e:
            print(f"❌ File move failed: {e}")
            results['failed'].append({'file': file_name, 'error': str(e)})
    
    return results

def main():
    print("\n" + "="*80)
    print("BULK INSERT BOOK OF TWEETS INTO NEO4J AURADB")
    print("="*80)
    
    all_results = {'successful': [], 'failed': []}
    
    # Process THOUGHTS
    thoughts_dir = BOOK_OF_TWEETS_BASE / "THOUGHTS"
    thoughts_results = process_directory(thoughts_dir, "THOUGHT", CONTENT_THOUGHTS_DIR)
    all_results['successful'].extend(thoughts_results['successful'])
    all_results['failed'].extend(thoughts_results['failed'])
    
    # Process BIBLE (PASSAGES)
    bible_dir = BOOK_OF_TWEETS_BASE / "BIBLE"
    passages_results = process_directory(bible_dir, "PASSAGE", CONTENT_PASSAGES_DIR)
    all_results['successful'].extend(passages_results['successful'])
    all_results['failed'].extend(passages_results['failed'])
    
    # Final Summary
    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    print(f"Total successful: {len(all_results['successful'])}")
    print(f"Total failed: {len(all_results['failed'])}")
    print("="*80)
    
    if all_results['failed']:
        print("\n❌ FAILED FILES:")
        for item in all_results['failed']:
            print(f"  - {item['file']}: {item['error']}")

if __name__ == '__main__':
    main()
