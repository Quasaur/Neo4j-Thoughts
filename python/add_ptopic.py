#!/usr/bin/env python3
"""
Add missing ptopic YAML property to markdown files.
The ptopic property creates an Obsidian link to the parent topic file.
"""

import os
import re
from pathlib import Path

def extract_parent_from_yaml(content):
    """Extract the parent value from YAML frontmatter."""
    match = re.search(r'^parent:\s*["\']?(topic\.[A-Z0-9_-]+|null)["\']?', content, re.MULTILINE)
    if match:
        parent_value = match.group(1)
        return parent_value
    return None

def has_ptopic(content):
    """Check if the file already has a ptopic property."""
    return bool(re.search(r'^ptopic:', content, re.MULTILINE))

def convert_parent_to_ptopic_link(parent_value):
    """Convert parent value to ptopic Obsidian link format."""
    if parent_value == "null":
        return "null"
    
    # Convert topic.PARENT-NAME to topic-PARENT-NAME
    topic_name = parent_value.replace(".", "-")
    return f'"[[{topic_name}]]"'

def add_ptopic_to_file(filepath):
    """Add ptopic property to a markdown file if missing."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if ptopic already exists
    if has_ptopic(content):
        return False, "Already has ptopic"
    
    # Extract parent value
    parent_value = extract_parent_from_yaml(content)
    if not parent_value:
        return False, "No parent property found"
    
    # Convert to ptopic link
    ptopic_value = convert_parent_to_ptopic_link(parent_value)
    
    # Find the location to insert ptopic (after neo4j property)
    # Look for the pattern and insert ptopic after neo4j: true
    pattern = r'(neo4j:\s*true\n)'
    replacement = f'\\1ptopic: {ptopic_value}\n'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content == content:
        # Try alternate insertion point (after parent property)
        pattern = r'(parent:\s*["\']?[^"\'\n]+["\']?\n)'
        replacement = f'\\1ptopic: {ptopic_value}\n'
        new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content == content:
        return False, "Could not find insertion point"
    
    # Write the updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Added ptopic: {ptopic_value}"

def main():
    content_dir = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content")
    
    stats = {
        "processed": 0,
        "updated": 0,
        "skipped": 0,
        "errors": 0
    }
    
    # Process all markdown files
    for md_file in content_dir.rglob("*.md"):
        stats["processed"] += 1
        success, message = add_ptopic_to_file(md_file)
        
        if success:
            stats["updated"] += 1
            print(f"✓ {md_file.relative_to(content_dir)}: {message}")
        else:
            if "Already has ptopic" in message:
                stats["skipped"] += 1
            else:
                stats["errors"] += 1
                print(f"✗ {md_file.relative_to(content_dir)}: {message}")
    
    print("\n" + "="*60)
    print(f"Processed: {stats['processed']} files")
    print(f"Updated: {stats['updated']} files")
    print(f"Skipped: {stats['skipped']} files (already had ptopic)")
    print(f"Errors: {stats['errors']} files")

if __name__ == "__main__":
    main()
