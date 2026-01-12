#!/usr/bin/env python3
"""
Smart Batch Translator
Extracts English content, generates a translation workbook for AI to process.
"""

import re
import json
from pathlib import Path

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")


def extract_content_from_file(file_path: Path):
    """Extract English title and content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract from Cypher block
        en_title_match = re.search(r'en_title:\s*"([^"]+)"', content)
        en_content_match = re.search(r'en_content:\s*"((?:[^"\\]|\\.)*)"\s*,', content)
        
        if en_title_match and en_content_match:
            return {
                'file': str(file_path),
                'name': file_path.name,
                'en_title': en_title_match.group(1),
                'en_content': en_content_match.group(1).replace('\\"', '"')
            }
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
    
    return None


def main():
    """Generate translation workbook."""
    md_files = sorted(CYPHER_DIR.glob("*.md"))
    workbook = []
    
    print(f"Processing {len(md_files)} files...")
    
    for md_file in md_files:
        # Check if has placeholders
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                if 'TITULO DEL PENSAMIENTO' in f.read():
                    item = extract_content_from_file(md_file)
                    if item:
                        workbook.append(item)
        except:
            continue
    
    print(f"Found {len(workbook)} files needing translation")
    
    # Save workbook
    output_file = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/python/translation_workbook.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(workbook, f, indent=2, ensure_ascii=False)
    
    print(f"Saved workbook to {output_file}")
    print(f"\nFirst 5 items:")
    for item in workbook[:5]:
        print(f"  - {item['name']}: {item['en_title']}")


if __name__ == "__main__":
    main()
