#!/usr/bin/env python3
"""
Bulk insert THOUGHTS from Book_of_Tweets into Neo4j AuraDB
Process files with populated ptopic values, insert into Neo4j, move to content/THOUGHTS,
and update neo4j property from false to true.
"""
import os
import re
import shutil
from pathlib import Path
from neo4j import GraphDatabase

# Neo4j connection details
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Paths
BOOK_OF_TWEETS_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets")
CONTENT_THOUGHTS_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS")

# Files to exclude (empty ptopic values)
EXCLUDE_FILES = [
    "DIVINE-GOODNESS.md",
    "INFINITE-GOD.md",
    "TERROR-TO-ENEMIES.md"
]

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown file"""
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def get_ptopic_value(frontmatter):
    """Extract ptopic value from frontmatter"""
    match = re.search(r'^ptopic:\s*(.+)$', frontmatter, re.MULTILINE)
    if match:
        value = match.group(1).strip()
        # Check if it's not empty (not just quotes or whitespace)
        if value and value not in ['""', "''", '', 'type: THOUGHT']:
            return value
    return None

def extract_cypher(content):
    """Extract Cypher query from markdown code block"""
    match = re.search(r'```Cypher\s*(.*?)\s*```', content, re.DOTALL | re.IGNORECASE)
    if match:
        cypher = match.group(1).strip()
        # Fix quoted property keys in relationships
        cypher = re.sub(r'\{\s*"name":\s*', '{ name: ', cypher)
        return cypher
    return None

def execute_cypher(cypher):
    """Execute Cypher query in Neo4j AuraDB"""
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

def update_neo4j_property(content):
    """Update neo4j property from false to true"""
    updated = re.sub(r'neo4j:\s*false', 'neo4j: true', content)
    return updated

def find_files_with_ptopic(base_dir):
    """Find all markdown files with non-empty ptopic value"""
    files_with_ptopic = []
    
    base_path = Path(base_dir)
    for md_file in base_path.rglob('*.md'):
        # Skip excluded files
        if md_file.name in EXCLUDE_FILES:
            continue
            
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter = extract_frontmatter(content)
            if frontmatter:
                ptopic = get_ptopic_value(frontmatter)
                if ptopic:
                    files_with_ptopic.append({
                        'path': md_file,
                        'name': md_file.name,
                        'content': content,
                        'ptopic': ptopic
                    })
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    return files_with_ptopic

def main():
    print("="*80)
    print("BULK INSERT THOUGHTS INTO NEO4J AURADB")
    print("="*80)
    print()
    
    # Find all files with populated ptopic
    print("Scanning for files with populated ptopic field...")
    files = find_files_with_ptopic(BOOK_OF_TWEETS_DIR)
    print(f"Found {len(files)} files to process")
    print()
    
    successful = []
    failed = []
    
    for idx, file_info in enumerate(files, 1):
        file_path = file_info['path']
        file_name = file_info['name']
        content = file_info['content']
        
        print(f"[{idx}/{len(files)}] Processing {file_name}...", end=" ")
        
        # Extract Cypher query
        cypher = extract_cypher(content)
        if not cypher:
            print("❌ FAILED - No Cypher block found")
            failed.append({
                'file': file_name,
                'error': 'No Cypher block found in file'
            })
            continue
        
        # Execute Cypher query
        success, error = execute_cypher(cypher)
        if not success:
            print(f"❌ FAILED - {error}")
            failed.append({
                'file': file_name,
                'error': error
            })
            continue
        
        # Update neo4j property
        updated_content = update_neo4j_property(content)
        
        # Write updated content to destination
        dest_path = CONTENT_THOUGHTS_DIR / file_name
        try:
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            # Remove original file
            file_path.unlink()
            
            print("✅ SUCCESS")
            successful.append(file_name)
        except Exception as e:
            print(f"❌ FAILED - Error moving file: {e}")
            failed.append({
                'file': file_name,
                'error': f'File operation error: {e}'
            })
    
    # Summary
    print()
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total files processed: {len(files)}")
    print(f"Successfully inserted: {len(successful)}")
    print(f"Failed: {len(failed)}")
    print()
    
    if successful:
        print("✅ SUCCESSFUL INSERTIONS:")
        for file_name in sorted(successful):
            print(f"  - {file_name}")
        print()
    
    if failed:
        print("❌ FAILED INSERTIONS:")
        for item in failed:
            print(f"  - {item['file']}")
            print(f"    Error: {item['error']}")
        print()
    
    print("="*80)

if __name__ == '__main__':
    main()
