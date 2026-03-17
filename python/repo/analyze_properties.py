#!/usr/bin/env python3
"""
Analyze DESCRIPTION and CONTENT node properties across all content files
"""

import os
import re
from collections import defaultdict

CONTENT_ROOT = "/Users/quasaur/Developer/Neo4j-Thoughts/content"

def extract_cypher_blocks(content):
    """Extract Cypher blocks from markdown content."""
    pattern = r'```Cypher(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
    return matches

def parse_node_properties(cypher_text, node_type):
    """Parse properties from CREATE (node_type { ... } statement."""
    properties = {}
    
    # Look for CREATE (d:DESCRIPTION or CREATE (c:CONTENT
    pattern = rf'CREATE \([dc]:{node_type}\s*\{{(.*?)\}}'
    match = re.search(pattern, cypher_text, re.DOTALL | re.IGNORECASE)
    
    if match:
        props_text = match.group(1)
        # Extract key: value pairs, handling multi-line
        # Pattern matches: key: "value" or key: number or key: [array] or key: "value" (with quotes)
        prop_pattern = r'(\w+)\s*:\s*("(?:[^"\\]|\\.)*"|\[[^\]]*\]|[^,\n]+)'
        
        for prop_match in re.finditer(prop_pattern, props_text):
            key = prop_match.group(1)
            # Clean up the key
            key = key.strip()
            if key:
                properties[key] = True
    
    return properties

def main():
    description_props = defaultdict(int)
    content_props = defaultdict(int)
    desc_files = []
    content_files = []
    
    files_checked = 0
    
    for root, dirs, files in os.walk(CONTENT_ROOT):
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(root, filename)
            files_checked += 1
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                cypher_blocks = extract_cypher_blocks(content)
                
                for block in cypher_blocks:
                    # Check for DESCRIPTION node
                    if re.search(r'CREATE\s*\(\s*d\s*:\s*DESCRIPTION', block, re.IGNORECASE):
                        props = parse_node_properties(block, 'DESCRIPTION')
                        if props:
                            desc_files.append(filepath)
                            for prop in props:
                                description_props[prop] += 1
                    
                    # Check for CONTENT node
                    if re.search(r'CREATE\s*\(\s*c\s*:\s*CONTENT', block, re.IGNORECASE):
                        props = parse_node_properties(block, 'CONTENT')
                        if props:
                            content_files.append(filepath)
                            for prop in props:
                                content_props[prop] += 1
                            
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
    
    print(f"Files checked: {files_checked}")
    print(f"Files with DESCRIPTION nodes: {len(desc_files)}")
    print(f"Files with CONTENT nodes: {len(content_files)}")
    
    print("\n" + "="*80)
    print("DESCRIPTION NODE PROPERTIES")
    print("="*80)
    print(f"{'Property':<30} {'Count':<10} {'Usage %'}")
    print("-"*80)
    
    for prop, count in sorted(description_props.items(), key=lambda x: -x[1]):
        pct = (count / len(desc_files)) * 100 if desc_files else 0
        print(f"{prop:<30} {count:<10} {pct:.1f}%")
    
    print("\n" + "="*80)
    print("CONTENT NODE PROPERTIES")
    print("="*80)
    print(f"{'Property':<30} {'Count':<10} {'Usage %'}")
    print("-"*80)
    
    for prop, count in sorted(content_props.items(), key=lambda x: -x[1]):
        pct = (count / len(content_files)) * 100 if content_files else 0
        print(f"{prop:<30} {count:<10} {pct:.1f}%")
    
    print("\n" + "="*80)
    print("RARE/UNIQUE PROPERTIES (< 10% usage in their node type)")
    print("="*80)
    
    print("\nDESCRIPTION node rare properties:")
    for prop, count in sorted(description_props.items(), key=lambda x: x[1]):
        pct = (count / len(desc_files)) * 100 if desc_files else 0
        if pct < 10:
            print(f"  {prop}: {count} files ({pct:.2f}%)")
    
    print("\nCONTENT node rare properties:")
    for prop, count in sorted(content_props.items(), key=lambda x: x[1]):
        pct = (count / len(content_files)) * 100 if content_files else 0
        if pct < 10:
            print(f"  {prop}: {count} files ({pct:.2f}%)")
    
    # List files with rare properties
    print("\n" + "="*80)
    print("FILES WITH RARE PROPERTIES")
    print("="*80)
    
    # Re-scan to find files with specific rare properties
    rare_desc_props = {p for p, c in description_props.items() 
                       if (c / len(desc_files)) * 100 < 10 if desc_files}
    rare_content_props = {p for p, c in content_props.items() 
                          if (c / len(content_files)) * 100 < 10 if content_files}
    
    if rare_desc_props:
        print("\nDESCRIPTION files with rare properties:")
        for filepath in desc_files[:10]:  # Limit output
            print(f"  {filepath}")
    
    if rare_content_props:
        print("\nCONTENT files with rare properties:")
        for filepath in content_files[:10]:  # Limit output
            print(f"  {filepath}")

if __name__ == "__main__":
    main()
