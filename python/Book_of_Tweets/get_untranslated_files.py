#!/usr/bin/env python3
"""
Get exact list of files that still have placeholder translations.
"""

import re
from pathlib import Path

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

def has_placeholder_translations(content: str) -> bool:
    """Check if file has placeholder translations - be more specific."""
    placeholders = [
        "TITULO DEL PENSAMIENTO",
        "TITRE DE LA PENSÉE",
        "biāo tí",
        "nèi róng",
        'es_title: "TITULO"',
        'fr_title: "TITRE"',
        'hi_title: "SHIRSHAK"',
        "CONTENIDO DEL PENSAMIENTO",
        "CONTENU DE LA PENSÉE",
        'es_content: "CONTENIDO"',
        'fr_content: "CONTENU"',
        'hi_content: "SAMAGRI"'
    ]
    return any(p in content for p in placeholders)

def main():
    all_files = sorted(CYPHER_DIR.glob("*.md"))
    
    files_to_translate = []
    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_placeholder_translations(f.read()):
                files_to_translate.append(file_path.name)
    
    print(f"Files needing translation: {len(files_to_translate)}\n")
    for name in files_to_translate:
        print(name)

if __name__ == "__main__":
    main()
