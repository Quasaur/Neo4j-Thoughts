#!/usr/bin/env python3
"""
Add missing ptopic YAML property to markdown files in Book_of_Tweets folder.
Adds the property without the wiki-link value so it can be filled in manually.
"""

import os
import re
from pathlib import Path

def has_ptopic(content):
    """Check if the file already has a ptopic property."""
    return bool(re.search(r'^ptopic:', content, re.MULTILINE))

def is_topic_or_thought(content):
    """Check if the file is a TOPIC or THOUGHT type."""
    return bool(re.search(r'^type:\s*(TOPIC|THOUGHT)', content, re.MULTILINE))

def add_ptopic_to_file(filepath):
    """Add ptopic property to a markdown file if missing."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it's a TOPIC or THOUGHT file
    if not is_topic_or_thought(content):
        return False, "Not a TOPIC or THOUGHT file"
    
    # Check if ptopic already exists
    if has_ptopic(content):
        return False, "Already has ptopic"
    
    # Find the location to insert ptopic (after neo4j property)
    # Look for the pattern and insert ptopic after neo4j: true
    pattern = r'(neo4j:\s*true\n)'
    replacement = r'\1ptopic: \n'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content == content:
        # Try alternate insertion point (after level property)
        pattern = r'(level:\s*\d+\n)'
        replacement = r'\1ptopic: \n'
        new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content == content:
        return False, "Could not find insertion point"
    
    # Write the updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "Added ptopic: (empty - ready for manual link)"

def main():
    book_of_tweets_dir = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets")
    
    stats = {
        "processed": 0,
        "updated": 0,
        "skipped": 0,
        "not_topic_thought": 0,
        "errors": 0
    }
    
    # Process all markdown files
    for md_file in book_of_tweets_dir.rglob("*.md"):
        stats["processed"] += 1
        success, message = add_ptopic_to_file(md_file)
        
        if success:
            stats["updated"] += 1
            print(f"✓ {md_file.relative_to(book_of_tweets_dir)}: {message}")
        else:
            if "Already has ptopic" in message:
                stats["skipped"] += 1
            elif "Not a TOPIC or THOUGHT" in message:
                stats["not_topic_thought"] += 1
            else:
                stats["errors"] += 1
                print(f"✗ {md_file.relative_to(book_of_tweets_dir)}: {message}")
    
    print("\n" + "="*60)
    print(f"Processed: {stats['processed']} files")
    print(f"Updated: {stats['updated']} files")
    print(f"Skipped: {stats['skipped']} files (already had ptopic)")
    print(f"Not TOPIC/THOUGHT: {stats['not_topic_thought']} files")
    print(f"Errors: {stats['errors']} files")

if __name__ == "__main__":
    main()
