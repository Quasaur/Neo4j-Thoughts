#!/usr/bin/env python3
"""
Apply Translations - Takes a completed translations JSON and updates all files
"""

import json
import re
from pathlib import Path


def apply_translation(file_path: str, translations: dict) -> bool:
    """Apply translations to a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace placeholders
        updated = content
        updated = updated.replace(
            'es_title: "TITULO DEL PENSAMIENTO"',
            f'es_title: "{translations["es_title"]}"'
        )
        updated = updated.replace(
            'es_content: "CONTENIDO DEL PENSAMIENTO"',
            f'es_content: "{translations["es_content"]}"'
        )
        updated = updated.replace(
            'fr_title: "TITRE DE LA PENSÉE"',
            f'fr_title: "{translations["fr_title"]}"'
        )
        updated = updated.replace(
            'fr_content: "CONTENU DE LA PENSÉE"',
            f'fr_content: "{translations["fr_content"]}"'
        )
        updated = updated.replace(
            'hi_title: "शिखा"',
            f'hi_title: "{translations["hi_title"]}"'
        )
        updated = updated.replace(
            'hi_content: "सामग्री"',
            f'hi_content: "{translations["hi_content"]}"'
        )
        updated = updated.replace(
            'zh_title: "biāo tí"',
            f'zh_title: "{translations["zh_title"]}"'
        )
        updated = updated.replace(
            'zh_content: "nèi róng"',
            f'zh_content: "{translations["zh_content"]}"'
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        return True
    except Exception as e:
        print(f"❌ Error updating {Path(file_path).name}: {e}")
        return False


def main():
    """Apply all translations."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: apply_translations.py <translations_file.json>")
        sys.exit(1)
    
    translations_file = Path(sys.argv[1])
    
    with open(translations_file, 'r', encoding='utf-8') as f:
        items = json.load(f)
    
    print(f"Applying translations to {len(items)} files...")
    print("=" * 60)
    
    success = 0
    failed = 0
    
    for idx, item in enumerate(items, 1):
        if 'translations' not in item:
            print(f"[{idx}/{len(items)}] ⚠️  Skipping {item['name']} - no translations found")
            continue
        
        if apply_translation(item['file'], item['translations']):
            print(f"[{idx}/{len(items)}] ✅ {item['name']}")
            success += 1
        else:
            failed += 1
    
    print("=" * 60)
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print(f"Skipped: {len(items) - success - failed}")


if __name__ == "__main__":
    main()
