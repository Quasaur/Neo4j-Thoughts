#!/usr/bin/env python3
"""
Phase 4: Update local THOUGHT, QUOTE, PASSAGE files to match synchronized TOPIC data
"""

import re
from pathlib import Path

CONTENT_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/content")

# Mapping of old/incorrect parent formats to correct ones
PARENT_CORRECTIONS = {
    "topic.THE-BIBLE": "topic.THE BIBLE",
    "topic.POLITICAL-SCIENCE": "topic.POLITICAL SCIENCE",
    "topic.FIN-GOV": "topic.FIN GOV"
}

def update_file(file_path, content_type):
    """Update a single content file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Update YAML parent field
    for old_parent, new_parent in PARENT_CORRECTIONS.items():
        # Check YAML frontmatter
        yaml_pattern = rf'(parent:\s*){re.escape(old_parent)}'
        if re.search(yaml_pattern, content):
            content = re.sub(yaml_pattern, rf'\g<1>{new_parent}', content)
            changes.append(f"parent: {old_parent} -> {new_parent}")
        
        # Check Cypher parent property
        cypher_pattern = rf'(parent:\s*"){re.escape(old_parent)}(")'
        if re.search(cypher_pattern, content):
            content = re.sub(cypher_pattern, rf'\g<1>{new_parent}\g<2>', content)
            changes.append(f"cypher parent: {old_parent} -> {new_parent}")
    
    # Update ptopic links (hyphen to space format)
    ptopic_fixes = {
        "[[topic-THE-BIBLE]]": "[[topic-THE BIBLE]]",
        "[[topic-POLITICAL-SCIENCE]]": "[[topic-POLITICAL SCIENCE]]",
        "[[topic-FIN-GOV]]": "[[topic-FIN GOV]]"
    }
    
    for old_ptopic, new_ptopic in ptopic_fixes.items():
        if old_ptopic in content:
            content = content.replace(old_ptopic, new_ptopic)
            changes.append(f"ptopic: {old_ptopic} -> {new_ptopic}")
    
    # Write if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return None

def scan_and_update():
    """Scan all content files and update as needed"""
    print("=" * 80)
    print("PHASE 4: SYNCING LOCAL CONTENT FILES")
    print("=" * 80)
    
    total_files = 0
    updated_files = 0
    
    # Process THOUGHTS
    print("\n  Processing THOUGHT files...")
    thoughts_dir = CONTENT_DIR / "THOUGHTS"
    for file_path in thoughts_dir.glob("thought-*.md"):
        total_files += 1
        changes = update_file(file_path, "THOUGHT")
        if changes:
            updated_files += 1
            print(f"    Updated: {file_path.name}")
            for change in changes:
                print(f"      - {change}")
    
    # Process QUOTES
    print("\n  Processing QUOTE files...")
    quotes_dir = CONTENT_DIR / "QUOTES"
    for file_path in quotes_dir.rglob("quote-*.md"):
        total_files += 1
        changes = update_file(file_path, "QUOTE")
        if changes:
            updated_files += 1
            print(f"    Updated: {file_path.name}")
            for change in changes:
                print(f"      - {change}")
    
    # Process PASSAGES
    print("\n  Processing PASSAGE files...")
    passages_dir = CONTENT_DIR / "PASSAGES"
    for file_path in passages_dir.rglob("passage-*.md"):
        total_files += 1
        changes = update_file(file_path, "PASSAGE")
        if changes:
            updated_files += 1
            print(f"    Updated: {file_path.name}")
            for change in changes:
                print(f"      - {change}")
    
    print("\n" + "=" * 80)
    print("PHASE 4 COMPLETE")
    print("=" * 80)
    print(f"  Total files scanned: {total_files}")
    print(f"  Files updated: {updated_files}")

if __name__ == "__main__":
    scan_and_update()
