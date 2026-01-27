#!/usr/bin/env python3
"""
Free Translation Script for PASSAGE Files
Translates PASSAGE entries using free Google Translate service.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, Optional, List
import time
import json

# Try to import deep-translator
try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    print("❌ deep-translator not available!")
    print("Install with: pip3 install --break-system-packages deep-translator")
    sys.exit(1)

PASSAGES_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/PASSAGES")

# The 12 PASSAGE files that need translations
PASSAGES_TO_TRANSLATE = [
    "Prov/01/FAITHLESSNESS.md",
    "Prov/02/FATE-OF-THE-WICKED.md",
    "Prov/02/PROTECTIION-FROM-EVIL.md",
    "Prov/03/DISCIPLINE-REBUKE.md",
    "Prov/03/MAN-OF-VIOLENCE.md",
    "Prov/03/NEIGHBORS.md",
    "Prov/03/OBLIGATION.md",
    "Prov/03/PRIDE-AS-EVIL.md",
    "Prov/03/SCORNERS.md",
    "Prov/03/TRUST-THE-LORD.md",
    "Roma/FREEDOM-OF-DEATH.md",
    "Roma/NOT-OF-FAITH.md"
]


def extract_english_from_passage(content: str) -> Optional[Dict[str, str]]:
    """Extract en_title and en_content from PASSAGE file."""
    # Look for en_title in the CONTENT node
    en_title_match = re.search(r'en_title:\s*"([^"]+)"', content)
    
    # Look for en_content - may be multi-line
    en_content_match = re.search(r'en_content:\s*"([^"]+)"', content, re.DOTALL)
    
    if en_title_match and en_content_match:
        return {
            'en_title': en_title_match.group(1).strip(),
            'en_content': en_content_match.group(1).strip()
        }
    return None


def translate_text(text: str, target_lang: str) -> Optional[str]:
    """Translate text using Google Translate via deep-translator."""
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        result = translator.translate(text)
        return result
    except Exception as e:
        print(f"    Translation error: {e}")
        return None


def generate_translations(en_title: str, en_content: str) -> Dict[str, str]:
    """Generate translations for all 4 languages."""
    translations = {}
    
    # Language mappings for deep-translator
    lang_map = {
        'es': 'es',      # Spanish
        'fr': 'fr',      # French
        'hi': 'hi',      # Hindi
        'zh': 'zh-CN'    # Chinese (Simplified)
    }
    
    print(f"  Translating: {en_title}")
    
    for lang_code, service_code in lang_map.items():
        print(f"    {lang_code.upper()}: ", end="", flush=True)
        
        # Translate title
        title_translation = translate_text(en_title, service_code)
        if not title_translation:
            print("Title ✗")
            continue
        
        translations[f'{lang_code}_title'] = title_translation
        
        # Translate content
        content_translation = translate_text(en_content, service_code)
        if not content_translation:
            print("Content ✗")
            del translations[f'{lang_code}_title']
            continue
        
        translations[f'{lang_code}_content'] = content_translation
        print("✓")
        
        # Rate limiting to avoid being blocked
        time.sleep(1.5)
    
    return translations


def update_passage_file(file_path: Path, translations: Dict[str, str]) -> bool:
    """Update PASSAGE file with translations."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the CREATE (c:CONTENT { block
        content_match = re.search(
            r'(CREATE \(c:CONTENT \{[^}]+\}\);)',
            content,
            re.DOTALL
        )
        
        if not content_match:
            print(f"  ⚠️  Could not find CONTENT node")
            return False
        
        old_content_node = content_match.group(1)
        new_content_node = old_content_node
        
        # Add each translation field before the closing });
        # First, find where to insert (before the closing });)
        insert_pos = new_content_node.rfind('});')
        
        if insert_pos == -1:
            print(f"  ⚠️  Could not find closing }});")
            return False
        
        # Build the translation fields
        translation_lines = []
        for key in ['es_title', 'es_content', 'fr_title', 'fr_content', 
                    'hi_title', 'hi_content', 'zh_title', 'zh_content']:
            if key in translations:
                # Escape quotes and backslashes
                value = translations[key].replace('\\', '\\\\').replace('"', '\\"')
                translation_lines.append(f' {key}: "{value}",')
        
        # Insert before the closing });
        before_close = new_content_node[:insert_pos].rstrip()
        if not before_close.endswith(','):
            before_close += ','
        
        new_content_node = before_close + '\n' + '\n'.join(translation_lines) + '\n});'
        
        # Replace in full content
        updated_content = content.replace(old_content_node, new_content_node)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error updating file: {e}")
        return False


def process_passage(relative_path: str) -> Optional[Dict]:
    """Process a single PASSAGE file."""
    file_path = PASSAGES_DIR / relative_path
    
    if not file_path.exists():
        print(f"  ⚠️  File not found: {file_path}")
        return None
    
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract English content
        english = extract_english_from_passage(content)
        if not english:
            print(f"  ⚠️  Could not extract English content")
            return None
        
        # Generate translations
        translations = generate_translations(english['en_title'], english['en_content'])
        
        if len(translations) < 8:  # Should have 4 languages * 2 fields = 8
            print(f"  ⚠️  Only got {len(translations)//2} complete language(s)")
            return None
        
        # Update file
        if update_passage_file(file_path, translations):
            print(f"  ✅ File updated with {len(translations)//2} languages")
            
            # Extract passage name for Neo4j update
            name_match = re.search(r'^name:\s*["\']?([^"\'\\n]+)["\']?', content, re.MULTILINE)
            passage_name = name_match.group(1).strip() if name_match else None
            
            return {
                'file': str(relative_path),
                'passage_name': passage_name,
                'translations': translations
            }
        else:
            return None
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None


def main():
    """Main processing function."""
    print("=" * 80)
    print("PASSAGE TRANSLATION SCRIPT (Free Google Translate)")
    print("=" * 80)
    
    if not TRANSLATOR_AVAILABLE:
        return
    
    print(f"\nProcessing {len(PASSAGES_TO_TRANSLATE)} PASSAGE files...")
    print("=" * 80)
    
    results = []
    success_count = 0
    failed_count = 0
    
    for i, relative_path in enumerate(PASSAGES_TO_TRANSLATE, 1):
        print(f"\n[{i}/{len(PASSAGES_TO_TRANSLATE)}] {relative_path}")
        
        result = process_passage(relative_path)
        
        if result:
            results.append(result)
            success_count += 1
        else:
            failed_count += 1
        
        # Progress update
        if i % 5 == 0:
            print("\n" + "-" * 80)
            print(f"Progress: {i}/{len(PASSAGES_TO_TRANSLATE)}")
            print(f"Success: {success_count} | Failed: {failed_count}")
            print("-" * 80)
    
    # Save results for Neo4j update script
    output_file = Path("ANALYSIS/passage_translations.json")
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Final summary
    print("\n" + "=" * 80)
    print("TRANSLATION COMPLETE!")
    print("=" * 80)
    print(f"Successfully translated: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Total: {len(PASSAGES_TO_TRANSLATE)}")
    print(f"\n📄 Results saved to: {output_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()
