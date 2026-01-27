#!/usr/bin/env python3
"""
Convert Chinese characters to Pinyin romanization for PASSAGE files.
"""

import re
import json
from pathlib import Path

try:
    from pypinyin import pinyin, Style
    PINYIN_AVAILABLE = True
except ImportError:
    PINYIN_AVAILABLE = False
    print("❌ pypinyin not available!")
    print("Install with: pip3 install --break-system-packages pypinyin")
    exit(1)

PASSAGES_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/PASSAGES")

# The 12 PASSAGE files that were just translated
PASSAGES_TO_FIX = [
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


def chinese_to_pinyin(text: str) -> str:
    """Convert Chinese characters to Pinyin romanization."""
    # Check if text contains Chinese characters
    if not re.search(r'[\u4e00-\u9fff]', text):
        return text  # No Chinese characters, return as-is
    
    # Convert to pinyin with tone marks
    result = pinyin(text, style=Style.TONE)
    # Join the pinyin syllables with spaces
    pinyin_text = ' '.join([''.join(word) for word in result])
    return pinyin_text


def fix_passage_file(file_path: Path) -> bool:
    """Fix Chinese translations in a PASSAGE file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find zh_title and zh_content
        zh_title_match = re.search(r'zh_title:\s*"([^"]+)"', content)
        zh_content_match = re.search(r'zh_content:\s*"([^"]+)"', content, re.DOTALL)
        
        if not zh_title_match or not zh_content_match:
            print(f"  ⚠️  Could not find Chinese translations")
            return False
        
        old_zh_title = zh_title_match.group(1)
        old_zh_content = zh_content_match.group(1)
        
        # Convert to Pinyin
        new_zh_title = chinese_to_pinyin(old_zh_title)
        new_zh_content = chinese_to_pinyin(old_zh_content)
        
        print(f"  Title: {old_zh_title} → {new_zh_title}")
        print(f"  Content: {old_zh_content[:50]}... → {new_zh_content[:50]}...")
        
        # Replace in content
        updated_content = content.replace(
            f'zh_title: "{old_zh_title}"',
            f'zh_title: "{new_zh_title}"'
        )
        updated_content = updated_content.replace(
            f'zh_content: "{old_zh_content}"',
            f'zh_content: "{new_zh_content}"'
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Main function."""
    print("=" * 80)
    print("Converting Chinese Characters to Pinyin Romanization")
    print("=" * 80)
    
    if not PINYIN_AVAILABLE:
        return
    
    success_count = 0
    failed_count = 0
    
    for i, relative_path in enumerate(PASSAGES_TO_FIX, 1):
        file_path = PASSAGES_DIR / relative_path
        print(f"\n[{i}/{len(PASSAGES_TO_FIX)}] {relative_path}")
        
        if fix_passage_file(file_path):
            print(f"  ✅ Converted to Pinyin")
            success_count += 1
        else:
            failed_count += 1
    
    print("\n" + "=" * 80)
    print("CONVERSION COMPLETE!")
    print("=" * 80)
    print(f"Successfully converted: {success_count}")
    print(f"Failed: {failed_count}")
    print("=" * 80)
    
    # Also update the translations JSON for Neo4j updates
    print("\nUpdating translations JSON for Neo4j...")
    translations_file = Path("ANALYSIS/passage_translations.json")
    
    if translations_file.exists():
        with open(translations_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
        
        for result in results:
            if 'zh_title' in result['translations']:
                old_title = result['translations']['zh_title']
                result['translations']['zh_title'] = chinese_to_pinyin(old_title)
            
            if 'zh_content' in result['translations']:
                old_content = result['translations']['zh_content']
                result['translations']['zh_content'] = chinese_to_pinyin(old_content)
        
        with open(translations_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Updated {translations_file}")


if __name__ == "__main__":
    main()
