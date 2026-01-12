#!/usr/bin/env python3
"""
Free Translation Script - Uses free translation services instead of paid APIs.
This script translates the remaining files using Google Translate and other free services.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, Optional
import time
import random

# Try different free translation libraries
try:
    from googletrans import Translator as GoogleTranslator
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

try:
    from translatepy import Translator as TranslatePyTranslator
    TRANSLATEPY_AVAILABLE = True
except ImportError:
    TRANSLATEPY_AVAILABLE = False

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

def has_placeholders(content: str) -> bool:
    """Check if file has placeholder translations."""
    placeholders = [
        "TITULO DEL PENSAMIENTO", "CONTENIDO DEL PENSAMIENTO",
        "TITRE DE LA PENSÉE", "CONTENU DE LA PENSÉE",
        "TITULO", "CONTENIDO",
        "TITRE", "CONTENU",
        "SHIRSHAK", "SAMAGRI",
        "biāo tí", "nèi róng"
    ]
    return any(placeholder in content for placeholder in placeholders)


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


def translate_with_google(text: str, target_lang: str) -> str:
    """Translate using Google Translate (free)."""
    if not GOOGLE_AVAILABLE:
        return None

    try:
        translator = GoogleTranslator()
        result = translator.translate(text, dest=target_lang)
        return result.text
    except Exception as e:
        print(f"  Google Translate error: {e}")
        return None


def translate_with_translatepy(text: str, target_lang: str) -> str:
    """Translate using TranslatePy (free, multiple services)."""
    if not TRANSLATEPY_AVAILABLE:
        return None

    try:
        translator = TranslatePyTranslator()
        result = translator.translate(text, destination_language=target_lang)
        return result.result
    except Exception as e:
        print(f"  TranslatePy error: {e}")
        return None


def translate_text(text: str, target_lang: str) -> str:
    """Translate text using available free services."""
    # Try Google Translate first
    result = translate_with_google(text, target_lang)
    if result:
        return result

    # Fallback to TranslatePy
    result = translate_with_translatepy(text, target_lang)
    if result:
        return result

    return None


def generate_free_translations(en_title: str, en_content: str) -> Dict[str, str]:
    """Generate translations using free services."""

    translations = {}

    # Language mappings
    lang_map = {
        'es': 'es',  # Spanish
        'fr': 'fr',  # French
        'hi': 'hi',  # Hindi
        'zh': 'zh-cn'  # Chinese (Simplified)
    }

    print(f"  Translating title: {en_title}")
    print(f"  Translating content: {en_content[:50]}...")

    for lang_code, service_code in lang_map.items():
        print(f"    {lang_code.upper()}: ", end="")

        # Translate title
        title_translation = translate_text(en_title, service_code)
        if title_translation:
            translations[f'{lang_code}_title'] = title_translation
            print(f"Title ✓ ", end="")
        else:
            print(f"Title ✗ ", end="")
            continue

        # Translate content
        content_translation = translate_text(en_content, service_code)
        if content_translation:
            translations[f'{lang_code}_content'] = content_translation
            print("Content ✓")
        else:
            print("Content ✗")
            # Remove title if content failed
            del translations[f'{lang_code}_title']

        # Rate limiting
        time.sleep(1)

    return translations


def update_content_node(content: str, translations: Dict[str, str]) -> str:
    """Update the CONTENT node with new translations."""

    # Find the CONTENT node
    content_match = re.search(r'(CREATE \(c:CONTENT \{[^}]+\}\);)', content, re.DOTALL)
    if not content_match:
        return None

    old_content_node = content_match.group(1)

    # Replace each translation field
    new_content_node = old_content_node

    for key, value in translations.items():
        # Escape quotes in the value
        escaped_value = value.replace('"', '\\"')

        # Replace the field
        pattern = rf'{key}:\s*"[^"]*"'
        replacement = f'{key}: "{escaped_value}"'
        new_content_node = re.sub(pattern, replacement, new_content_node)

    # Replace in full content
    return content.replace(old_content_node, new_content_node)


def process_file(file_path: Path) -> bool:
    """Process a single file."""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if it needs translation
        if not has_placeholders(content):
            return None  # Already translated

        # Extract English content
        english = extract_english_content(content)
        if not english:
            print(f"  ⚠️  Could not extract English content")
            return False

        # Generate translations using free services
        print(f"Processing: {file_path.name}")
        translations = generate_free_translations(english['en_title'], english['en_content'])

        if not translations:
            print(f"  ❌ No translations generated")
            return False

        # Update content
        new_content = update_content_node(content, translations)
        if not new_content:
            print(f"  ⚠️  Could not update CONTENT node")
            return False

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ Successfully translated with {len(translations)//2} languages")
        return True

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Main processing function."""
    print("="*70)
    print("FREE TRANSLATION SCRIPT")
    print("="*70)

    if not GOOGLE_AVAILABLE and not TRANSLATEPY_AVAILABLE:
        print("❌ No free translation libraries available!")
        print("Please install: pip install googletrans translatepy")
        return

    print(f"Available services:")
    if GOOGLE_AVAILABLE:
        print("  ✓ Google Translate")
    if TRANSLATEPY_AVAILABLE:
        print("  ✓ TranslatePy (multiple services)")

    # Get all markdown files
    all_files = sorted(CYPHER_DIR.glob("*.md"))
    print(f"\nTotal markdown files: {len(all_files)}")

    # Filter files that need translation
    files_to_process = []
    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_placeholders(f.read()):
                files_to_process.append(file_path)

    print(f"Files needing translation: {len(files_to_process)}")

    if not files_to_process:
        print("\n✅ All files already have complete translations!")
        return

    print(f"\nStarting free translation of {len(files_to_process)} files...")
    print("="*70)

    # Process each file
    processed = 0
    failed = 0
    skipped = 0

    for i, file_path in enumerate(files_to_process, 1):
        print(f"\n[{i}/{len(files_to_process)}] {file_path.name}")

        result = process_file(file_path)

        if result is True:
            processed += 1
        elif result is False:
            failed += 1
        else:
            skipped += 1

        # Progress update every 10 files
        if i % 10 == 0:
            print("\n" + "-"*70)
            print(f"Progress: {i}/{len(files_to_process)} files processed")
            print(f"Success: {processed} | Failed: {failed} | Skipped: {skipped}")
            print("-"*70)

    # Final summary
    print("\n" + "="*70)
    print("FREE TRANSLATION COMPLETE!")
    print("="*70)
    print(f"Successfully translated: {processed}")
    print(f"Failed: {failed}")
    print(f"Skipped (already done): {skipped}")
    print(f"Total processed: {len(files_to_process)}")
    print("="*70)


if __name__ == "__main__":
    main()