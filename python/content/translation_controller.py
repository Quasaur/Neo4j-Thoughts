#!/usr/bin/env python3
"""
Translation Controller - Batch translate using AI
This script coordinates the translation process by:
1. Getting files that need translation
2. Calling AI to translate each batch
3. Updating files with translations
"""

import json
import subprocess
import sys
from pathlib import Path

def translate_batch(items: list) -> list:
    """
    Translate a batch of items using AI.
    Each item has: file, name, en_title, en_content
    Returns same items with 'translations' added.
    """
    print(f"\n🔄 Translating batch of {len(items)} items...")
    
    results = []
    for idx, item in enumerate(items, 1):
        print(f"\n[{idx}/{len(items)}] {item['name']}")
        print(f"  Title: {item['en_title']}")
        print(f"  Content: {item['en_content'][:60]}...")
        
        # Here we would call the AI translation
        # For now, creating a translation request
        translations = translate_single(item['en_title'], item['en_content'])
        
        item['translations'] = translations
        results.append(item)
        
        print(f"  ✅ Translated")
    
    return results


def translate_single(en_title: str, en_content: str) -> dict:
    """
    Translate a single title/content pair to all target languages.
    This is where AI translation happens.
    """
    # Prepare the translation prompt
    prompt = f"""Translate the following English title and content into Spanish, French, Hindi (Devanagari script), and Chinese (simplified characters).

**Title:** {en_title}
**Content:** {en_content}

Provide ONLY a JSON response with no additional text, in this exact format:
{{
  "es_title": "Spanish title",
  "es_content": "Spanish content",
  "fr_title": "French title",
  "fr_content": "French content",
  "hi_title": "Hindi title in Devanagari",
  "hi_content": "Hindi content in Devanagari",
  "zh_title": "Simplified Chinese title",
  "zh_content": "Simplified Chinese content"
}}"""
    
    # NOTE: This is where you would integrate with an AI API
    # For demonstration, returning a structured placeholder
    # In production, call Claude API, GPT API, etc.
    
    # Placeholder translations (would be replaced by actual AI call)
    return {
        "es_title": f"[ES] {en_title}",
        "es_content": f"[ES] {en_content}",
        "fr_title": f"[FR] {en_title}",
        "fr_content": f"[FR] {en_content}",
        "hi_title": f"[HI] {en_title}",
        "hi_content": f"[HI] {en_content}",
        "zh_title": f"[ZH] {en_title}",
        "zh_content": f"[ZH] {en_content}"
    }


def main():
    """Main translation workflow."""
    # Get batch size from command line
    batch_size = 10 if len(sys.argv) < 2 else int(sys.argv[1])
    
    print("=" * 60)
    print("AI Translation Controller")
    print("=" * 60)
    print(f"Batch size: {batch_size}")
    
    # Step 1: Get files needing translation
    print("\n📋 Getting files that need translation...")
    result = subprocess.run(
        ['python3', 'translate_with_ai.py', 'list', str(batch_size)],
        capture_output=True,
        text=True,
        cwd='/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/python'
    )
    
    if result.returncode != 0:
        print(f"❌ Error getting file list: {result.stderr}")
        sys.exit(1)
    
    files = json.loads(result.stdout)
    print(f"Found {len(files)} files needing translation")
    
    if not files:
        print("No files need translation!")
        return
    
    # Step 2: Translate batch
    translated = translate_batch(files)
    
    # Step 3: Save translations to file
    output_file = Path('/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/python/translations_batch.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Saved translations to {output_file}")
    
    # Step 4: Apply translations
    print("\n📝 Applying translations to files...")
    result = subprocess.run(
        ['python3', 'translate_with_ai.py', 'update', str(output_file)],
        cwd='/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/python'
    )
    
    if result.returncode != 0:
        print("❌ Error applying translations")
        sys.exit(1)
    
    print("\n✅ Translation batch complete!")


if __name__ == "__main__":
    main()
