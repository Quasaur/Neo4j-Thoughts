#!/usr/bin/env python3
"""
Helper script to prepare translation batches
This script generates the file list and English content for manual translation
"""

import os
import re
from pathlib import Path

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

def has_placeholder(content):
    return "TITULO DEL PENSAMIENTO" in content

def extract_english(content):
    en_title_match = re.search(r'en_title:\s*"([^"]*)"', content)
    en_content_match = re.search(r'en_content:\s*"([^"]*)"', content)
    
    if en_title_match and en_content_match:
        return {
            'title': en_title_match.group(1),
            'content': en_content_match.group(1)
        }
    return None

def main():
    files_to_process = []
    
    for file_path in sorted(CYPHER_DIR.glob("*.md")):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if has_placeholder(content):
                eng = extract_english(content)
                if eng:
                    files_to_process.append({
                        'filename': file_path.name,
                        'en_title': eng['title'],
                        'en_content': eng['content']
                    })
    
    print(f"Total files needing translation: {len(files_to_process)}")
    print("\n" + "="*80)
    print("FILES TO TRANSLATE")
    print("="*80)
    
    for i, file_info in enumerate(files_to_process, 1):
        print(f"\n{i}. {file_info['filename']}")
        print(f"   Title: {file_info['en_title']}")
        print(f"   Content: {file_info['en_content']}")
        print()

if __name__ == "__main__":
    main()
