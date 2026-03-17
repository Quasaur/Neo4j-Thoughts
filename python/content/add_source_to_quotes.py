#!/usr/bin/env python3
"""
Add 'source' property from Cypher block to YAML frontmatter for QUOTE files.
Inserts 'source' between 'parent' and 'en_content'.
"""

import re
from pathlib import Path

QUOTES_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/content/QUOTES")

def extract_source_from_cypher(content):
    """Extract the source property value from the first CREATE (q:QUOTE) block"""
    # Try different formats:
    # Format 1: source: "value" (inline with quotes)
    pattern1 = r'CREATE \(q:QUOTE \{[^}]*source:\s*"([^"]+)"'
    match = re.search(pattern1, content, re.DOTALL)
    if match:
        return match.group(1)
    
    # Format 2: source: "value" (multiline with opening brace on same line)
    pattern2 = r'CREATE \(q:QUOTE\s*\{[^}]*source:\s*"([^"]+)"'
    match = re.search(pattern2, content, re.DOTALL)
    if match:
        return match.group(1)
    
    # Format 3: source: value (no quotes, just the value)
    pattern3 = r'source:\s*"?([^"\n,}]+)"?'
    match = re.search(pattern3, content, re.DOTALL)
    if match:
        return match.group(1).strip().strip('"')
    
    return None

def add_source_to_yaml(content, source_value):
    """Add source property between parent and en_content in YAML"""
    # Find the position after parent line and before en_content line
    lines = content.split('\n')
    new_lines = []
    inserted = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        
        # Check if this is the parent line (and we haven't inserted yet)
        if not inserted and re.match(r'^parent:\s', line):
            # Check if next line is en_content
            if i + 1 < len(lines) and re.match(r'^en_content:\s', lines[i + 1]):
                # Insert source before en_content
                # Determine indentation from the en_content line
                next_line = lines[i + 1]
                indent_match = re.match(r'^(\s*)', next_line)
                indent = indent_match.group(1) if indent_match else ""
                new_lines.append(f'{indent}source: "{source_value}"')
                inserted = True
    
    return '\n'.join(new_lines), inserted

def process_file(file_path):
    """Process a single QUOTE file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has source in YAML
    yaml_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        print(f"  ⚠ No YAML frontmatter: {file_path.name}")
        return False
    
    yaml_content = yaml_match.group(1)
    if 'source:' in yaml_content:
        print(f"  ℹ Already has source: {file_path.name}")
        return False
    
    # Extract source from Cypher
    source_value = extract_source_from_cypher(content)
    if not source_value:
        print(f"  ⚠ No source in Cypher: {file_path.name}")
        return False
    
    # Add source to YAML
    new_content, inserted = add_source_to_yaml(content, source_value)
    if not inserted:
        print(f"  ⚠ Could not insert source: {file_path.name}")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Added source: {file_path.name}")
    return True

def main():
    print("=" * 80)
    print("ADDING SOURCE PROPERTY TO QUOTE FILES")
    print("=" * 80)
    print()
    
    quote_files = sorted(QUOTES_DIR.glob("quote-*.md"))
    print(f"Found {len(quote_files)} QUOTE files")
    print()
    
    added = 0
    skipped = 0
    errors = 0
    
    for file_path in quote_files:
        try:
            result = process_file(file_path)
            if result:
                added += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ❌ Error processing {file_path.name}: {e}")
            errors += 1
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Added source: {added}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")

if __name__ == "__main__":
    main()
