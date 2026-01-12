#!/usr/bin/env python3
"""
Convert UnInserted THOUGHTS to Obsidian-Cypher format.
This script:
1. Maps cypher files to their corresponding markdown files in UnInserted folder
2. Creates new Obsidian-Cypher format files (frontmatter + embedded Cypher)
3. Deletes original cypher files after successful conversion
"""

import os
import re
from pathlib import Path
from typing import Dict, Optional, Tuple, List

UNINSERTED_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS/UnInserted")
CYPHER_DIR = UNINSERTED_DIR / "cypher" / "done"


def find_markdown_file(cypher_name: str) -> Optional[Path]:
    """Find the markdown file corresponding to a cypher file."""
    # Extract the thought name from cypher filename: thought-NAME.cypher -> NAME
    thought_name = cypher_name.replace("thought-", "").replace(".cypher", "")
    
    # Convert underscores to hyphens to match markdown naming convention
    # Example: 'A_GREAT_DAY' -> 'A-GREAT-DAY'
    thought_name = thought_name.replace('_', '-')
    
    # Look in UnInserted directory
    md_file = UNINSERTED_DIR / f"{thought_name}.md"
    if md_file.exists():
        return md_file
    
    return None


def extract_frontmatter_and_content(md_path: Path) -> Tuple[Dict[str, str], str, List[str]]:
    """Extract frontmatter, content, and tags from markdown file."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter and content
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter_text = parts[1].strip()
        body = parts[2].strip()
    else:
        frontmatter_text = ""
        body = content.strip()
    
    # Parse frontmatter into dict and extract tags
    frontmatter = {}
    tags = []
    current_key = None
    
    for line in frontmatter_text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        if line_stripped.startswith('-') and current_key == 'tags':
            # This is a tag
            tags.append(line_stripped.lstrip('- ').strip())
        elif ':' in line_stripped:
            key, value = line_stripped.split(':', 1)
            key = key.strip()
            value = value.strip()
            frontmatter[key] = value
            current_key = key
        else:
            current_key = None
    
    return frontmatter, body, tags


def read_cypher_file(cypher_path: Path) -> str:
    """Read cypher file content."""
    with open(cypher_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the first comment line if it exists
    lines = content.strip().split('\n')
    if lines and lines[0].startswith('// Generated from'):
        lines = lines[1:]
    
    return '\n'.join(lines).strip()


def create_obsidian_cypher_format(frontmatter: Dict[str, str], tags: List[str], cypher_content: str) -> str:
    """Create new Obsidian-Cypher format content."""
    # Build frontmatter section
    fm_lines = ["---"]
    
    # Extract key fields for the new format based on TOPICS example
    title = frontmatter.get('title', 'Thought: UNKNOWN')
    # Extract name from cypher content if possible
    name_match = re.search(r'name:\s*"(thought\.[^"]+)"', cypher_content)
    if name_match:
        name = name_match.group(1)
    else:
        name = title.replace('Thought: ', 'thought.').replace(' ', '_').replace('-', '_')
    
    # Extract alias from cypher content if possible
    alias_match = re.search(r'alias:\s*"([^"]+)"', cypher_content)
    alias = alias_match.group(1) if alias_match else title
    
    # Extract parent from cypher content
    parent_match = re.search(r'parent:\s*"([^"]+)"', cypher_content)
    if parent_match:
        parent = parent_match.group(1)
    else:
        parent_raw = frontmatter.get('ptopic', '').replace('[[', '').replace(']]', '').strip('"')
        parent = parent_raw if parent_raw else "topic.NULL"
    
    # Get ptopic from frontmatter
    ptopic = frontmatter.get('ptopic', '').strip('"')
    
    # Construct new frontmatter
    fm_lines.append(f"name: {name}")
    fm_lines.append(f'alias: "{alias}"')
    fm_lines.append(f"type: {frontmatter.get('type', 'THOUGHT')}")
    fm_lines.append(f"parent: {parent}")
    
    if tags:
        fm_lines.append("tags:")
        for tag in tags:
            fm_lines.append(f"- {tag}")
    
    fm_lines.append(f"neo4j: {frontmatter.get('neo4j', 'true')}")
    fm_lines.append(f'ptopic: "{ptopic}"')
    fm_lines.append(f"level: {frontmatter.get('level', '3')}")
    fm_lines.append("---")
    fm_lines.append("")
    
    # Add embedded Cypher block
    fm_lines.append("```Cypher")
    fm_lines.append(cypher_content)
    fm_lines.append("```")
    
    return '\n'.join(fm_lines)


def main():
    """Main conversion process."""
    converted = []
    failed = []
    
    # Iterate through all cypher files
    cypher_files = sorted(CYPHER_DIR.glob("thought-*.cypher"))
    
    print(f"Found {len(cypher_files)} cypher files to process\n")
    
    for cypher_file in cypher_files:
        cypher_name = cypher_file.name
        
        # Find corresponding markdown file
        md_file = find_markdown_file(cypher_name)
        
        if not md_file:
            print(f"⚠️  No markdown file found for {cypher_name}")
            failed.append(cypher_name)
            continue
        
        try:
            # Read both files
            frontmatter, body, tags = extract_frontmatter_and_content(md_file)
            cypher_content = read_cypher_file(cypher_file)
            
            # Create new Obsidian-Cypher format
            new_content = create_obsidian_cypher_format(frontmatter, tags, cypher_content)
            
            # Write new file (overwrite the old markdown file)
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Converted: {md_file.name}")
            converted.append((md_file, cypher_file))
            
        except Exception as e:
            print(f"❌ Error converting {cypher_name}: {e}")
            failed.append(cypher_name)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Converted: {len(converted)}")
    print(f"  Failed: {len(failed)}")
    print(f"{'='*60}")
    
    if failed:
        print(f"\n⚠️  Failed files:")
        for f in failed:
            print(f"  - {f}")
    
    # Ask for confirmation before deletion
    if converted:
        print("\nFiles ready for cleanup. Run with --delete flag to remove originals.")
        print("(This will delete the original .cypher files)")
    
    return converted, failed


if __name__ == "__main__":
    import sys
    
    converted, failed = main()
    
    # If --delete flag is provided, delete the cypher files
    if "--delete" in sys.argv and converted:
        print("\n🗑️  Deleting original .cypher files...")
        deleted_count = 0
        for md_file, cypher_file in converted:
            try:
                cypher_file.unlink()
                print(f"  Deleted: {cypher_file.name}")
                deleted_count += 1
            except Exception as e:
                print(f"  ❌ Failed to delete {cypher_file.name}: {e}")
        
        print(f"\n✅ Deleted {deleted_count} cypher files")
