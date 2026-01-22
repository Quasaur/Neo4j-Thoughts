#!/usr/bin/env python3
"""
Script to identify all THOUGHT files with populated ptopic field in Book_of_Tweets folder
"""
import os
import re
from pathlib import Path

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
        if value and value not in ['""', "''", '']:
            return value
    return None

def find_files_with_ptopic(base_dir):
    """Find all markdown files with non-empty ptopic value"""
    files_with_ptopic = []
    
    base_path = Path(base_dir)
    for md_file in base_path.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter = extract_frontmatter(content)
            if frontmatter:
                ptopic = get_ptopic_value(frontmatter)
                if ptopic:
                    # Extract parent value too for verification
                    parent_match = re.search(r'^parent:\s*(.+)$', frontmatter, re.MULTILINE)
                    parent = parent_match.group(1).strip() if parent_match else 'N/A'
                    
                    files_with_ptopic.append({
                        'file': str(md_file),
                        'name': md_file.name,
                        'ptopic': ptopic,
                        'parent': parent
                    })
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    return files_with_ptopic

if __name__ == '__main__':
    book_of_tweets_dir = '/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets'
    
    print("Scanning for files with populated ptopic field...")
    files = find_files_with_ptopic(book_of_tweets_dir)
    
    print(f"\nFound {len(files)} files with populated ptopic field:\n")
    print("="*80)
    
    for item in sorted(files, key=lambda x: x['name']):
        print(f"File: {item['name']}")
        print(f"  Parent: {item['parent']}")
        print(f"  Ptopic: {item['ptopic']}")
        print(f"  Path: {item['file']}")
        print("-"*80)
    
    print(f"\nTotal files to process: {len(files)}")
