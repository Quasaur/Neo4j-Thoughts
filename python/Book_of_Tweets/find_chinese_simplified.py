#!/usr/bin/env python3
"""
Find and translate Chinese Simplified characters to Pinyin in Book_of_Tweets zh_title and zh_content fields.
"""

import os
import re
from pathlib import Path

def contains_chinese_characters(text):
    """Check if text contains Chinese characters (not pinyin)."""
    # Chinese character ranges
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    return bool(chinese_pattern.search(text))

def count_words(text):
    """Count words in a string."""
    return len(text.split())

def extract_zh_fields(filepath):
    """Extract zh_title and zh_content from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for zh_title and zh_content in the Cypher block
    title_match = re.search(r'zh_title:\s*"([^"]*)"', content)
    content_match = re.search(r'zh_content:\s*"([^"]*)"', content)
    
    zh_title = title_match.group(1) if title_match else None
    zh_content = content_match.group(1) if content_match else None
    
    return zh_title, zh_content, content

def main():
    os.chdir('/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts')
    
    print("=" * 80)
    print("Chinese Simplified Character & Title Length Checker")
    print("=" * 80)
    print()
    
    thought_dir = Path("Book_of_Tweets/cypher")
    
    issues = []
    correct_files = []
    
    for thought_file in thought_dir.glob("*.md"):
        zh_title, zh_content, content = extract_zh_fields(thought_file)
        
        if zh_title is None and zh_content is None:
            continue
        
        file_issues = []
        
        # Check zh_title
        if zh_title:
            if contains_chinese_characters(zh_title):
                file_issues.append(f"Title has Chinese characters: {zh_title}")
            word_count = count_words(zh_title)
            if word_count > 4:
                file_issues.append(f"Title has {word_count} words (max 4): {zh_title}")
        
        # Check zh_content
        if zh_content and zh_content != "nèi róng":
            if contains_chinese_characters(zh_content):
                file_issues.append(f"Content has Chinese characters: {zh_content}")
        
        if file_issues:
            issues.append((thought_file.name, file_issues, zh_title, zh_content))
        else:
            correct_files.append(thought_file.name)
    
    print(f"Summary:")
    print(f"  ✓ Correct: {len(correct_files)}")
    print(f"  ✗ Issues found: {len(issues)}")
    print()
    
    if issues:
        print("=" * 80)
        print(f"FILES WITH ISSUES ({len(issues)})")
        print("=" * 80)
        print()
        
        for filename, file_issues, zh_title, zh_content in issues:
            print(f"{filename}")
            for issue in file_issues:
                print(f"  ✗ {issue}")
            print()
    else:
        print("✓ All files are correct!")

if __name__ == "__main__":
    main()
