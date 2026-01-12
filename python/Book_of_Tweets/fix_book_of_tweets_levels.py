#!/usr/bin/env python3
"""
Fix level mismatches in Book_of_Tweets thoughts.

Rule: THOUGHT, QUOTE, PASSAGE children should have the SAME level as their parent TOPIC.
This script checks frontmatter level vs Cypher code level and reports/fixes mismatches.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_topic_levels():
    """Extract all topic levels from content/TOPICS."""
    topic_levels = {}
    topic_dir = Path("content/TOPICS")
    
    for topic_file in topic_dir.glob("topic-*.md"):
        with open(topic_file, 'r', encoding='utf-8') as f:
            content = f.read()
            name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
            level_match = re.search(r'^level:\s*(\d+)$', content, re.MULTILINE)
            
            if name_match and level_match:
                topic_name = name_match.group(1).strip().strip('"')  # Remove quotes if present
                topic_levels[topic_name] = int(level_match.group(1))
    
    return topic_levels

def analyze_thought_file(filepath, topic_levels):
    """Analyze a thought file for level mismatches."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter values
    parent_match = re.search(r'^parent:\s*(.+)$', content, re.MULTILINE)
    fm_level_match = re.search(r'^level:\s*(\d+)$', content, re.MULTILINE)
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    
    if not (parent_match and fm_level_match and name_match):
        return None
    
    parent_topic = parent_match.group(1).strip().strip('"')  # Remove quotes if present
    # Normalize: replace hyphens with spaces to match actual topic names
    parent_topic_normalized = parent_topic.replace('-', ' ')
    fm_level = int(fm_level_match.group(1))
    thought_name = name_match.group(1).strip().strip('"')  # Remove quotes if present
    
    # Extract Cypher level
    cypher_match = re.search(r'CREATE \(t:THOUGHT\s*\{[^}]*level:\s*(\d+)', content, re.DOTALL)
    
    if not cypher_match:
        return None
    
    cypher_level = int(cypher_match.group(1))
    
    # Get expected level from parent topic (try both original and normalized)
    expected_level = topic_levels.get(parent_topic) or topic_levels.get(parent_topic_normalized)
    
    return {
        'filepath': filepath,
        'name': thought_name,
        'parent': parent_topic,
        'fm_level': fm_level,
        'cypher_level': cypher_level,
        'expected_level': expected_level,
        'content': content
    }

def fix_thought_file(info):
    """Fix level mismatches in a thought file."""
    content = info['content']
    expected = info['expected_level']
    
    changes = []
    
    # Fix frontmatter level if needed
    if info['fm_level'] != expected:
        old_line = f"level: {info['fm_level']}"
        new_line = f"level: {expected}"
        content = re.sub(r'^level:\s*\d+$', new_line, content, count=1, flags=re.MULTILINE)
        changes.append(f"frontmatter: {info['fm_level']} → {expected}")
    
    # Fix Cypher level if needed
    if info['cypher_level'] != expected:
        # Find and replace the level in the CREATE statement
        pattern = r'(CREATE \(t:THOUGHT\s*\{[^}]*level:\s*)(\d+)'
        replacement = rf'\g<1>{expected}'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        changes.append(f"cypher: {info['cypher_level']} → {expected}")
    
    if changes:
        with open(info['filepath'], 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return None

def main():
    os.chdir('/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts')
    
    print("=" * 80)
    print("Book of Tweets Level Checker & Fixer")
    print("=" * 80)
    print()
    
    # Get topic levels
    print("Loading topic levels...")
    topic_levels = extract_topic_levels()
    print(f"Found {len(topic_levels)} topics\n")
    
    # Analyze all thought files
    print("Analyzing thoughts in Book_of_Tweets/cypher...")
    thought_dir = Path("Book_of_Tweets/cypher")
    
    mismatches = []
    correct = []
    missing_parent = []
    
    for thought_file in thought_dir.glob("*.md"):
        info = analyze_thought_file(thought_file, topic_levels)
        
        if info is None:
            continue
        
        if info['expected_level'] is None:
            missing_parent.append(info)
        elif info['fm_level'] != info['expected_level'] or info['cypher_level'] != info['expected_level']:
            mismatches.append(info)
        else:
            correct.append(info)
    
    print(f"\nResults:")
    print(f"  ✓ Correct: {len(correct)}")
    print(f"  ✗ Mismatches: {len(mismatches)}")
    print(f"  ? Missing parent topic: {len(missing_parent)}")
    print()
    
    if missing_parent:
        print("=" * 80)
        print("THOUGHTS WITH MISSING PARENT TOPICS")
        print("=" * 80)
        for info in missing_parent[:10]:
            print(f"  {info['name']}")
            print(f"    Parent: {info['parent']} (NOT FOUND)")
            print(f"    File: {info['filepath'].name}")
            print()
    
    if mismatches:
        print("=" * 80)
        print("LEVEL MISMATCHES FOUND")
        print("=" * 80)
        
        # Group by parent topic
        by_topic = defaultdict(list)
        for info in mismatches:
            by_topic[info['parent']].append(info)
        
        for topic in sorted(by_topic.keys()):
            items = by_topic[topic]
            expected = items[0]['expected_level']
            print(f"\n{topic} (expected level: {expected})")
            print(f"  {len(items)} thoughts with mismatches:")
            
            for info in items:
                fm_status = "✓" if info['fm_level'] == expected else f"✗ {info['fm_level']}"
                cy_status = "✓" if info['cypher_level'] == expected else f"✗ {info['cypher_level']}"
                print(f"    {info['name']}")
                print(f"      Frontmatter: {fm_status}")
                print(f"      Cypher: {cy_status}")
        
        print("\n" + "=" * 80)
        print("FIXING MISMATCHES")
        print("=" * 80)
        
        fixed_count = 0
        for info in mismatches:
            changes = fix_thought_file(info)
            if changes:
                fixed_count += 1
                print(f"✓ Fixed {info['filepath'].name}: {', '.join(changes)}")
        
        print(f"\nFixed {fixed_count} files")
    
    else:
        print("✓ All thoughts have correct levels!")

if __name__ == "__main__":
    main()
