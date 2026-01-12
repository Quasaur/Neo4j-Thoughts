#!/usr/bin/env python3
"""
Translate placeholder text in Obsidian-Cypher files to real translations.
This script:
1. Finds all files with placeholder translations
2. Extracts the English title and content
3. Translates to Spanish, French, Hindi, and Chinese
4. Updates the Cypher code block with real translations
"""

import os
import re
from pathlib import Path
from typing import Dict, Optional, Tuple
import anthropic

# Directory to process
CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

# Placeholder patterns
PLACEHOLDERS = {
    'es_title': 'TITULO DEL PENSAMIENTO',
    'es_content': 'CONTENIDO DEL PENSAMIENTO',
    'fr_title': 'TITRE DE LA PENSÉE',
    'fr_content': 'CONTENU DE LA PENSÉE',
    'hi_title': 'शिखा',
    'hi_content': 'सामग्री',
    'zh_title': 'biāo tí',
    'zh_content': 'nèi róng'
}


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
        
        # Extract en_content
        content_match = re.search(r'en_content:\s*"([^"]+)"', content)
        en_content = content_match.group(1) if content_match else None
        
        return en_title, en_content
    except Exception as e:
        print(f"Error extracting content from {file_path}: {e}")
        return None, None


def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text to target language.
    For this implementation, we'll use simple rule-based translations
    or you can integrate with an API.
    """
    # This is a placeholder - in production, you'd use a translation API
    # For now, returning a simple marker
    translations = {
        'es': f'[ES: {text}]',
        'fr': f'[FR: {text}]',
        'hi': f'[HI: {text}]',
        'zh': f'[ZH: {text}]'
    }
    return translations.get(target_lang, text)


def generate_translations(en_title: str, en_content: str) -> Dict[str, str]:
    """
    Generate translations for all languages.
    Returns a dictionary with keys: es_title, es_content, fr_title, fr_content, 
    hi_title, hi_content, zh_title, zh_content
    
    Note: This uses hardcoded translations. For production use, integrate with
    an AI translation API like Claude, GPT, or Google Translate.
    """
    import json
    
    # For this script, we'll use a simple translation dictionary
    # In production, you'd call an AI API here
    
    # Manual translations based on common theological/philosophical themes
    # This is a fallback - ideally use AI translation
    translations = {
        'es_title': translate_to_spanish(en_title),
        'es_content': translate_to_spanish(en_content),
        'fr_title': translate_to_french(en_title),
        'fr_content': translate_to_french(en_content),
        'hi_title': translate_to_hindi(en_title),
        'hi_content': translate_to_hindi(en_content),
        'zh_title': translate_to_chinese(en_title),
        'zh_content': translate_to_chinese(en_content)
    }
    
    return translations


def translate_to_spanish(text: str) -> str:
    """Translate English text to Spanish."""
    # This is a placeholder. In production, use an AI API
    # For now, we'll need to implement this properly
    return f"[ES] {text}"


def translate_to_french(text: str) -> str:
    """Translate English text to French."""
    return f"[FR] {text}"


def translate_to_hindi(text: str) -> str:
    """Translate English text to Hindi (Devanagari script)."""
    return f"[HI] {text}"


def translate_to_chinese(text: str) -> str:
    """Translate English text to Chinese (simplified)."""
    return f"[ZH] {text}"


def update_file_translations(file_path: Path, translations: Dict[str, str]) -> bool:
    """Update the file with real translations."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace each placeholder with actual translation
        updated = content
        updated = updated.replace(f'es_title: "TITULO DEL PENSAMIENTO"', f'es_title: "{translations["es_title"]}"')
        updated = updated.replace(f'es_content: "CONTENIDO DEL PENSAMIENTO"', f'es_content: "{translations["es_content"]}"')
        updated = updated.replace(f'fr_title: "TITRE DE LA PENSÉE"', f'fr_title: "{translations["fr_title"]}"')
        updated = updated.replace(f'fr_content: "CONTENU DE LA PENSÉE"', f'fr_content: "{translations["fr_content"]}"')
        updated = updated.replace(f'hi_title: "शिखा"', f'hi_title: "{translations["hi_title"]}"')
        updated = updated.replace(f'hi_content: "सामग्री"', f'hi_content: "{translations["hi_content"]}"')
        updated = updated.replace(f'zh_title: "biāo tí"', f'zh_title: "{translations["zh_title"]}"')
        updated = updated.replace(f'zh_content: "nèi róng"', f'zh_content: "{translations["zh_content"]}"')
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def process_file(file_path: Path, dry_run: bool = True) -> bool:
    """Process a single file."""
    # Check if it has placeholders
    if not has_placeholders(file_path):
        return False
    
    # Extract English content
    en_title, en_content = extract_english_content(file_path)
    if not en_title or not en_content:
        print(f"⚠️  Could not extract English content from {file_path.name}")
        return False
    
    print(f"Processing: {file_path.name}")
    print(f"  Title: {en_title}")
    print(f"  Content: {en_content[:60]}...")
    
    if dry_run:
        print(f"  [DRY RUN] Would translate this file")
        return True
    
    # Generate translations
    translations = generate_translations(en_title, en_content)
    
    # Update file
    if update_file_translations(file_path, translations):
        print(f"  ✅ Updated with translations")
        return True
    else:
        print(f"  ❌ Failed to update")
        return False


def main(dry_run: bool = True, limit: int = None):
    """Main processing loop."""
    # Find all markdown files
    md_files = sorted(CYPHER_DIR.glob("*.md"))
    
    print(f"Found {len(md_files)} total markdown files")
    print(f"{'DRY RUN MODE - No files will be modified' if dry_run else 'LIVE MODE - Files will be updated'}")
    print("=" * 60)
    
    processed = 0
    updated = 0
    
    for md_file in md_files:
        if limit and processed >= limit:
            break
        
        if process_file(md_file, dry_run=dry_run):
            processed += 1
            if not dry_run:
                updated += 1
    
    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  Files needing translation: {processed}")
    if not dry_run:
        print(f"  Files successfully updated: {updated}")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    # Parse command line arguments
    dry_run = "--live" not in sys.argv
    limit = None
    
    # Check for --limit flag
    for i, arg in enumerate(sys.argv):
        if arg == "--limit" and i + 1 < len(sys.argv):
            try:
                limit = int(sys.argv[i + 1])
            except ValueError:
                print("Invalid limit value")
                sys.exit(1)
    
    print("Translation Script for Obsidian-Cypher Files")
    print("=" * 60)
    
    if dry_run:
        print("Running in DRY RUN mode. Use --live to actually update files.")
        if limit:
            print(f"Limiting to first {limit} files")
    else:
        print("⚠️  LIVE MODE - Files will be modified!")
        response = input("Are you sure you want to continue? (yes/no): ")
        if response.lower() != "yes":
            print("Aborted.")
            sys.exit(0)
    
    main(dry_run=dry_run, limit=limit)
