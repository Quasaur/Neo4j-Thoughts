#!/usr/bin/env python3
"""
Process a batch of files - extract English content for translation.
This script prepares files for translation and can apply translations.
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")


def has_placeholder_translations(content: str) -> bool:
    """Check if file has placeholder translations."""
    return "TITULO DEL PENSAMIENTO" in content or "TITRE DE LA PENSÉE" in content


def extract_english_content(content: str) -> Optional[Dict[str, str]]:
    """Extract en_title and en_content from file content."""
    en_title_match = re.search(r'en_title:\s*"([^"]*)"', content)
    en_content_match = re.search(r'en_content:\s*"([^"]*)"', content)
    
    if en_title_match and en_content_match:
        return {
            'en_title': en_title_match.group(1),
            'en_content': en_content_match.group(1)
        }
    return None


def get_files_needing_translation() -> List[Path]:
    """Get list of files that need translation."""
    files_to_process = []
    all_files = sorted(CYPHER_DIR.glob("*.md"))
    
    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_placeholder_translations(f.read()):
                files_to_process.append(file_path)
    
    return files_to_process


def extract_batch(start: int, count: int) -> List[Dict]:
    """Extract a batch of files for translation."""
    files = get_files_needing_translation()
    batch = files[start:start+count]
    
    result = []
    for file_path in batch:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        english = extract_english_content(content)
        if english:
            result.append({
                'filename': file_path.name,
                'filepath': str(file_path),
                'en_title': english['en_title'],
                'en_content': english['en_content']
            })
    
    return result


def apply_translations(filepath: str, translations: Dict[str, str]) -> bool:
    """Apply translations to a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and update each translation field
        for key, value in translations.items():
            # Escape special characters for regex
            escaped_value = value.replace('\\', '\\\\').replace('"', '\\"')
            
            # Pattern to match the field
            pattern = rf'({key}:)\s*"[^"]*"'
            replacement = rf'\1 "{escaped_value}"'
            
            content = re.sub(pattern, replacement, content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error applying translations: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 process_batch.py count           # Show how many files need translation")
        print("  python3 process_batch.py extract START COUNT   # Extract batch for translation")
        print("  python3 process_batch.py apply FILE TRANSLATIONS_JSON  # Apply translations")
        return
    
    command = sys.argv[1]
    
    if command == "count":
        files = get_files_needing_translation()
        print(f"{len(files)}")
    
    elif command == "extract":
        if len(sys.argv) < 4:
            print("Usage: python3 process_batch.py extract START COUNT")
            return
        
        start = int(sys.argv[2])
        count = int(sys.argv[3])
        
        batch = extract_batch(start, count)
        print(json.dumps(batch, indent=2, ensure_ascii=False))
    
    elif command == "apply":
        if len(sys.argv) < 4:
            print("Usage: python3 process_batch.py apply FILEPATH '{\"es_title\":\"...\", ...}'")
            return
        
        filepath = sys.argv[2]
        translations = json.loads(sys.argv[3])
        
        if apply_translations(filepath, translations):
            print("✅ Translations applied successfully")
        else:
            print("❌ Failed to apply translations")


if __name__ == "__main__":
    main()
