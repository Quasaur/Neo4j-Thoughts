#!/usr/bin/env python3
"""
AI-Powered Translation Script for Obsidian-Cypher Files
This script processes files and uses AI (via external call) to translate content.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, Tuple, Optional

# Directory to process
CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")


def has_placeholders(file_path: Path) -> bool:
    """Check if file contains placeholder text."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return 'TITULO DEL PENSAMIENTO' in content
    except Exception:
        return False


def extract_english_content(file_path: Path) -> Tuple[Optional[str], Optional[str]]:
    """Extract English title and content from Cypher code block."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract en_title
        title_match = re.search(r'en_title:\s*"([^"]+)"', content)
        en_title = title_match.group(1) if title_match else None
        
        # Extract en_content - handle escaped quotes
        content_match = re.search(r'en_content:\s*"([^"]+(?:\\"[^"]*)*)"', content)
        if not content_match:
            # Try simpler pattern
            content_match = re.search(r'en_content:\s*"(.+?)"(?=,|\s*\n)', content, re.DOTALL)
        en_content = content_match.group(1) if content_match else None
        
        return en_title, en_content
    except Exception as e:
        print(f"Error extracting content from {file_path}: {e}")
        return None, None


def get_files_needing_translation(limit: int = None) -> list:
    """Get list of files that need translation."""
    md_files = sorted(CYPHER_DIR.glob("*.md"))
    files_to_process = []
    
    for md_file in md_files:
        if limit and len(files_to_process) >= limit:
            break
        
        if has_placeholders(md_file):
            en_title, en_content = extract_english_content(md_file)
            if en_title and en_content:
                files_to_process.append({
                    'file': str(md_file),
                    'name': md_file.name,
                    'en_title': en_title,
                    'en_content': en_content
                })
    
    return files_to_process


def update_file_with_translations(file_path: str, translations: Dict[str, str]) -> bool:
    """Update a file with real translations."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Escape special characters in translations for regex
        def escape_for_replacement(text):
            return text.replace('\\', '\\\\').replace('"', '\\"')
        
        # Replace placeholders with actual translations
        updated = content
        updated = updated.replace(
            'es_title: "TITULO DEL PENSAMIENTO"',
            f'es_title: "{escape_for_replacement(translations["es_title"])}"'
        )
        updated = updated.replace(
            'es_content: "CONTENIDO DEL PENSAMIENTO"',
            f'es_content: "{escape_for_replacement(translations["es_content"])}"'
        )
        updated = updated.replace(
            'fr_title: "TITRE DE LA PENSÉE"',
            f'fr_title: "{escape_for_replacement(translations["fr_title"])}"'
        )
        updated = updated.replace(
            'fr_content: "CONTENU DE LA PENSÉE"',
            f'fr_content: "{escape_for_replacement(translations["fr_content"])}"'
        )
        updated = updated.replace(
            'hi_title: "शिखा"',
            f'hi_title: "{escape_for_replacement(translations["hi_title"])}"'
        )
        updated = updated.replace(
            'hi_content: "सामग्री"',
            f'hi_content: "{escape_for_replacement(translations["hi_content"])}"'
        )
        updated = updated.replace(
            'zh_title: "biāo tí"',
            f'zh_title: "{escape_for_replacement(translations["zh_title"])}"'
        )
        updated = updated.replace(
            'zh_content: "nèi róng"',
            f'zh_content: "{escape_for_replacement(translations["zh_content"])}"'
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False


def main():
    """Main entry point."""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        # List mode - output JSON of files needing translation
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
        files = get_files_needing_translation(limit=limit)
        print(json.dumps(files, indent=2, ensure_ascii=False))
    elif len(sys.argv) > 1 and sys.argv[1] == 'update':
        # Update mode - read translations JSON from stdin and update files
        if len(sys.argv) < 3:
            print("Usage: translate_with_ai.py update <translations_json_file>")
            sys.exit(1)
        
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            updates = json.load(f)
        
        success = 0
        failed = 0
        
        for update in updates:
            file_path = update['file']
            translations = update['translations']
            
            if update_file_with_translations(file_path, translations):
                print(f"✅ Updated: {Path(file_path).name}")
                success += 1
            else:
                failed += 1
        
        print(f"\n{'='*60}")
        print(f"Updated: {success} files")
        print(f"Failed: {failed} files")
        print(f"{'='*60}")
    else:
        print("Usage:")
        print("  List files:    translate_with_ai.py list [limit]")
        print("  Update files:  translate_with_ai.py update <translations.json>")


if __name__ == "__main__":
    main()
