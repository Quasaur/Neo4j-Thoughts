#!/usr/bin/env python3
"""
Convert Chinese characters to Pinyin romanization for THOUGHT files in Book_of_Tweets.
Adapted from convert_chinese_to_pinyin.py
"""

import re
from pathlib import Path

try:
    from pypinyin import pinyin, Style
    PINYIN_AVAILABLE = True
except ImportError:
    PINYIN_AVAILABLE = False
    print("❌ pypinyin not available!")
    print("Install with: pip3 install --break-system-packages pypinyin")
    exit(1)

THOUGHTS_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/THOUGHTS")


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


def has_chinese_in_zh_fields(content: str) -> bool:
    """Check if content has Chinese characters in zh_title or zh_content fields."""
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    for line in content.split('\n'):
        if ('zh_title:' in line or 'zh_content:' in line) and chinese_pattern.search(line):
            return True
    return False


def fix_thought_file(file_path: Path, dry_run: bool = False) -> bool:
    """Fix Chinese translations in a THOUGHT file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file needs fixing
        if not has_chinese_in_zh_fields(content):
            return False
        
        # Find zh_title and zh_content in the Cypher block
        zh_title_match = re.search(r'(\s+zh_title:\s*)"([^"]+)"', content)
        zh_content_match = re.search(r'(\s+zh_content:\s*)"([^"]+)"', content, re.DOTALL)
        
        if not zh_title_match and not zh_content_match:
            print(f"  ⚠️  Could not find Chinese translations in expected format")
            return False
        
        updated_content = content
        changes_made = False
        
        # Fix zh_title if it has Chinese
        if zh_title_match:
            indent = zh_title_match.group(1)
            old_zh_title = zh_title_match.group(2)
            
            if re.search(r'[\u4e00-\u9fff]', old_zh_title):
                new_zh_title = chinese_to_pinyin(old_zh_title)
                print(f"  📝 Title: {old_zh_title}")
                print(f"     → {new_zh_title}")
                
                updated_content = updated_content.replace(
                    f'{indent}"{old_zh_title}"',
                    f'{indent}"{new_zh_title}"'
                )
                changes_made = True
        
        # Fix zh_content if it has Chinese
        if zh_content_match:
            indent = zh_content_match.group(1)
            old_zh_content = zh_content_match.group(2)
            
            if re.search(r'[\u4e00-\u9fff]', old_zh_content):
                new_zh_content = chinese_to_pinyin(old_zh_content)
                print(f"  📝 Content: {old_zh_content[:60]}...")
                print(f"     → {new_zh_content[:60]}...")
                
                updated_content = updated_content.replace(
                    f'{indent}"{old_zh_content}"',
                    f'{indent}"{new_zh_content}"'
                )
                changes_made = True
        
        # Write back if not dry run
        if changes_made and not dry_run:
            # Create backup
            backup_path = file_path.with_suffix('.md.bak')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
        
        return changes_made
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main(dry_run: bool = False):
    """Main function."""
    print("=" * 80)
    print("Converting Chinese Characters to Pinyin in Book_of_Tweets THOUGHTS")
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
    print("=" * 80)
    
    if not PINYIN_AVAILABLE:
        return
    
    # Get all markdown files
    md_files = sorted(THOUGHTS_DIR.glob("*.md"))
    
    success_count = 0
    skipped_count = 0
    failed_count = 0
    
    for i, file_path in enumerate(md_files, 1):
        print(f"\n[{i}/{len(md_files)}] {file_path.name}")
        
        try:
            if fix_thought_file(file_path, dry_run=dry_run):
                if dry_run:
                    print(f"  🔍 Would convert to Pinyin")
                else:
                    print(f"  ✅ Converted to Pinyin")
                success_count += 1
            else:
                skipped_count += 1
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            failed_count += 1
    
    print("\n" + "=" * 80)
    print("CONVERSION COMPLETE!")
    print("=" * 80)
    print(f"Files with changes: {success_count}")
    print(f"Files skipped (no Chinese): {skipped_count}")
    print(f"Failed: {failed_count}")
    print("=" * 80)
    
    if not dry_run and success_count > 0:
        print("\n💾 Backup files created with .md.bak extension")


if __name__ == "__main__":
    import sys
    
    # Check for --dry-run flag
    dry_run = "--dry-run" in sys.argv
    
    main(dry_run=dry_run)
