#!/usr/bin/env python3
"""
Apply Pinyin corrections to Book_of_Tweets zh_title and zh_content fields.
"""

import os
import re
import json
from pathlib import Path

def fix_file(filepath, corrections):
    """Apply corrections to a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # Fix zh_title if provided
    if 'zh_title' in corrections:
        old_title_match = re.search(r'zh_title:\s*"([^"]*)"', content)
        if old_title_match:
            old_title = old_title_match.group(1)
            new_title = corrections['zh_title']
            content = re.sub(
                r'(zh_title:\s*)"[^"]*"',
                rf'\1"{new_title}"',
                content
            )
            changes.append(f"zh_title: {old_title} → {new_title}")
    
    # Fix zh_content if provided
    if 'zh_content' in corrections:
        old_content_match = re.search(r'zh_content:\s*"([^"]*)"', content)
        if old_content_match:
            old_content = old_content_match.group(1)
            new_content = corrections['zh_content']
            content = re.sub(
                r'(zh_content:\s*)"[^"]*"',
                rf'\1"{new_content}"',
                content
            )
            changes.append(f"zh_content updated")
    
    # Handle title-only fixes (zh_content_old means title needs shortening)
    if 'zh_content_old' in corrections and 'zh_content' not in corrections:
        # Title is already in Pinyin but needs to be shortened - just keep it as is
        # The correction file shows what it was, but we're replacing with shorter version
        pass
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return None

def main():
    os.chdir('/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts')
    
    print("=" * 80)
    print("Applying Pinyin Corrections to Book_of_Tweets")
    print("=" * 80)
    print()
    
    # Load corrections
    with open('python/chinese_corrections.json', 'r', encoding='utf-8') as f:
        corrections_map = json.load(f)
    
    thought_dir = Path("Book_of_Tweets/cypher")
    
    fixed_count = 0
    
    for filename, corrections in corrections_map.items():
        filepath = thought_dir / filename
        
        if not filepath.exists():
            print(f"⚠ File not found: {filename}")
            continue
        
        changes = fix_file(filepath, corrections)
        
        if changes:
            fixed_count += 1
            print(f"✓ Fixed {filename}")
            for change in changes:
                print(f"  {change}")
    
    print()
    print(f"Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
