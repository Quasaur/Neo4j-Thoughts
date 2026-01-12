#!/usr/bin/env python3
"""
Complete translations for all markdown files with placeholder translations.
Uses Claude AI to generate accurate Spanish, French, Hindi, and Chinese translations.
"""

import os
import re
import sys
from pathlib import Path
import anthropic
import time
from typing import Dict, List, Optional

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

# Get API key from environment or prompt
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("\n" + "="*70)
    print("ANTHROPIC API KEY REQUIRED")
    print("="*70)
    print("Please enter your Anthropic API key.")
    print("You can get one from: https://console.anthropic.com/")
    print("Or set the ANTHROPIC_API_KEY environment variable to skip this prompt.")
    print("-"*70)
    api_key = input("Enter API key: ").strip()
    if not api_key:
        print("ERROR: No API key provided")
        sys.exit(1)

try:
    client = anthropic.Anthropic(api_key=api_key)
except Exception as e:
    print(f"ERROR: Could not initialize Anthropic client: {e}")
    sys.exit(1)


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


def generate_translations(en_title: str, en_content: str) -> Dict[str, str]:
    """Generate translations using Claude AI."""
    
    prompt = f"""Translate this Christian theological thought into Spanish, French, Hindi, and Chinese.

English Title: {en_title}
English Content: {en_content}

Provide translations in this EXACT JSON format:
{{
    "es_title": "Spanish title here",
    "es_content": "Spanish content here",
    "fr_title": "French title here",
    "fr_content": "French content here",
    "hi_title": "Hindi title here",
    "hi_content": "Hindi content here",
    "zh_title": "Chinese Pinyin title here",
    "zh_content": "Chinese Pinyin content here"
}}

Important guidelines:
1. Keep theological terminology accurate
2. Maintain the spiritual and doctrinal meaning
3. For Chinese: Use Pinyin romanization
4. For Hindi: Use Devanagari script
5. Preserve quotes and punctuation appropriately
6. Return ONLY the JSON object, no other text"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        response_text = message.content[0].text.strip()
        
        # Extract JSON from response (may have markdown code blocks)
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()
        
        # Parse JSON
        import json
        translations = json.loads(response_text)
        
        # Validate all required fields
        required = ['es_title', 'es_content', 'fr_title', 'fr_content', 
                   'hi_title', 'hi_content', 'zh_title', 'zh_content']
        if all(k in translations for k in required):
            return translations
        else:
            print(f"  ⚠️  Missing fields in translation response")
            return None
            
    except Exception as e:
        print(f"  ❌ Translation error: {e}")
        return None


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
        if not has_placeholder_translations(content):
            return None  # Already translated
        
        # Extract English content
        english = extract_english_content(content)
        if not english:
            print(f"  ⚠️  Could not extract English content")
            return False
        
        # Generate translations
        print(f"  🔄 Translating: {english['en_title']}")
        translations = generate_translations(english['en_title'], english['en_content'])
        
        if not translations:
            return False
        
        # Update content
        new_content = update_content_node(content, translations)
        if not new_content:
            print(f"  ⚠️  Could not update CONTENT node")
            return False
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Main processing function."""
    print("="*70)
    print("BATCH TRANSLATION PROCESSOR")
    print("="*70)
    
    # Get all markdown files
    all_files = sorted(CYPHER_DIR.glob("*.md"))
    print(f"\nTotal markdown files: {len(all_files)}")
    
    # Filter files that need translation
    files_to_process = []
    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_placeholder_translations(f.read()):
                files_to_process.append(file_path)
    
    print(f"Files needing translation: {len(files_to_process)}")
    print(f"Files already complete: {len(all_files) - len(files_to_process)}")
    
    if not files_to_process:
        print("\n✅ All files already have complete translations!")
        return
    
    print(f"\nStarting translation of {len(files_to_process)} files...")
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
            print(f"  ✅ Successfully translated")
        elif result is False:
            failed += 1
        else:
            skipped += 1
        
        # Rate limiting - small delay between API calls
        if result is not None:
            time.sleep(0.5)
        
        # Progress update every 50 files
        if i % 50 == 0:
            print("\n" + "-"*70)
            print(f"Progress: {i}/{len(files_to_process)} files processed")
            print(f"Success: {processed} | Failed: {failed} | Skipped: {skipped}")
            print("-"*70)
    
    # Final summary
    print("\n" + "="*70)
    print("TRANSLATION COMPLETE!")
    print("="*70)
    print(f"Successfully translated: {processed}")
    print(f"Failed: {failed}")
    print(f"Skipped (already done): {skipped}")
    print(f"Total processed: {len(files_to_process)}")
    print("="*70)


if __name__ == "__main__":
    main()
