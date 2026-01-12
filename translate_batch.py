#!/usr/bin/env python3
"""
Simple script to list files needing translation for manual processing.
"""

import re
from pathlib import Path

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

def has_placeholder_translations(content: str) -> bool:
    """Check if file has placeholder translations."""
    return "TITULO DEL PENSAMIENTO" in content or "TITRE DE LA PENSÉE" in content or "biāo tí" in content

def main():
    all_files = sorted(CYPHER_DIR.glob("*.md"))
    
    files_to_translate = []
    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_placeholder_translations(f.read()):
                files_to_translate.append(file_path.name)
    
    print(f"Total files: {len(all_files)}")
    print(f"Files needing translation: {len(files_to_translate)}")
    print("\nFiles to translate:")
    for name in files_to_translate[:20]:  # Show first 20
        print(f"  {name}")
    
    if len(files_to_translate) > 20:
        print(f"  ... and {len(files_to_translate) - 20} more")

if __name__ == "__main__":
    main()
