#!/usr/bin/env python3
"""
Direct translation script - processes files in batches of 10
Generates translations directly without API calls
"""

import os
import re
from pathlib import Path
from typing import Dict, List

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

def has_placeholder(content: str) -> bool:
    """Check if file has placeholder translations."""
    return "TITULO DEL PENSAMIENTO" in content

def extract_english(content: str) -> Dict[str, str]:
    """Extract en_title and en_content."""
    en_title_match = re.search(r'en_title:\s*"([^"]*)"', content)
    en_content_match = re.search(r'en_content:\s*"([^"]*)"', content)
    
    if en_title_match and en_content_match:
        return {
            'en_title': en_title_match.group(1),
            'en_content': en_content_match.group(1)
        }
    return None

def get_files_needing_translation() -> List[Path]:
    """Get list of all files that need translation."""
    files = []
    for file_path in sorted(CYPHER_DIR.glob("*.md")):
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_placeholder(f.read()):
                files.append(file_path)
    return files

def main():
    files = get_files_needing_translation()
    print(f"Found {len(files)} files needing translation")
    print("\nFiles to process:")
    for i, f in enumerate(files[:50], 1):  # Show first 50
        eng = extract_english(open(f, 'r', encoding='utf-8').read())
        if eng:
            print(f"{i}. {f.name}")
            print(f"   Title: {eng['en_title']}")
            print(f"   Content: {eng['en_content'][:80]}...")
    
    if len(files) > 50:
        print(f"\n... and {len(files) - 50} more files")

if __name__ == "__main__":
    main()
