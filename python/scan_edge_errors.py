#!/usr/bin/env python3
"""
Scan markdown files for edge name property errors in Cypher blocks.
Identifies two types of errors:
1. " >" spacing error (should be "->")
2. Missing edge prefix (edge., t.edge., q.edge., p.edge.)
"""

import re
from pathlib import Path
from collections import defaultdict

def scan_file_for_errors(file_path):
    """Scan a single file for edge name property errors."""
    errors = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Look for MERGE statements with HAS_CHILD, HAS_THOUGHT, HAS_QUOTE, HAS_PASSAGE relationships
    for i, line in enumerate(lines, 1):
        if 'MERGE' in line and (':HAS_CHILD' in line or ':HAS_THOUGHT' in line or ':HAS_QUOTE' in line or ':HAS_PASSAGE' in line):
            # Check for " >" spacing error
            if ' >' in line and ' >-' not in line:
                errors.append({
                    'line': i,
                    'type': 'spacing_error',
                    'content': line.strip(),
                    'issue': 'Contains " >" instead of "->"'
                })
            
            # Check for missing edge prefix
            # Extract the name property value
            name_match = re.search(r'name:\s*"([^"]+)"', line)
            if name_match:
                name_value = name_match.group(1)
                
                # Determine what prefix should be there based on relationship type
                if ':HAS_CHILD' in line:
                    # TOPIC->TOPIC should have "edge."
                    if not name_value.startswith('edge.'):
                        errors.append({
                            'line': i,
                            'type': 'missing_prefix',
                            'content': line.strip(),
                            'issue': f'Missing "edge." prefix. Current: "{name_value}"'
                        })
                elif ':HAS_THOUGHT' in line:
                    # TOPIC->THOUGHT should have "t.edge."
                    if not name_value.startswith('t.edge.'):
                        errors.append({
                            'line': i,
                            'type': 'missing_prefix',
                            'content': line.strip(),
                            'issue': f'Missing "t.edge." prefix. Current: "{name_value}"'
                        })
                elif ':HAS_QUOTE' in line:
                    # TOPIC->QUOTE should have "q.edge."
                    if not name_value.startswith('q.edge.'):
                        errors.append({
                            'line': i,
                            'type': 'missing_prefix',
                            'content': line.strip(),
                            'issue': f'Missing "q.edge." prefix. Current: "{name_value}"'
                        })
                elif ':HAS_PASSAGE' in line:
                    # TOPIC->PASSAGE should have "p.edge."
                    if not name_value.startswith('p.edge.'):
                        errors.append({
                            'line': i,
                            'type': 'missing_prefix',
                            'content': line.strip(),
                            'issue': f'Missing "p.edge." prefix. Current: "{name_value}"'
                        })
    
    return errors

def scan_directory(directory):
    """Scan all markdown files in a directory."""
    results = defaultdict(list)
    
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"⚠️  Directory not found: {directory}")
        return results
    
    for md_file in sorted(dir_path.rglob('*.md')):
        errors = scan_file_for_errors(md_file)
        if errors:
            results[str(md_file)] = errors
    
    return results

def main():
    base_dir = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts")
    
    print("=" * 80)
    print("SCANNING FOR EDGE NAME PROPERTY ERRORS")
    print("=" * 80)
    
    # Scan both directories
    directories = [
        base_dir / "Book_of_Tweets",
        base_dir / "content"
    ]
    
    all_results = {}
    total_spacing_errors = 0
    total_prefix_errors = 0
    
    for directory in directories:
        print(f"\n📂 Scanning: {directory.relative_to(base_dir)}")
        results = scan_directory(directory)
        all_results[str(directory)] = results
        
        spacing_count = sum(1 for file_errors in results.values() 
                          for error in file_errors if error['type'] == 'spacing_error')
        prefix_count = sum(1 for file_errors in results.values() 
                         for error in file_errors if error['type'] == 'missing_prefix')
        
        print(f"   Files with spacing errors (' >'): {len([f for f, e in results.items() if any(err['type'] == 'spacing_error' for err in e)])}")
        print(f"   Total spacing errors: {spacing_count}")
        print(f"   Files with missing prefix errors: {len([f for f, e in results.items() if any(err['type'] == 'missing_prefix' for err in e)])}")
        print(f"   Total prefix errors: {prefix_count}")
        
        total_spacing_errors += spacing_count
        total_prefix_errors += prefix_count
    
    # Detailed output
    print("\n" + "=" * 80)
    print("DETAILED ERRORS")
    print("=" * 80)
    
    for directory, results in all_results.items():
        if results:
            print(f"\n📁 {Path(directory).name}/")
            for file_path, errors in sorted(results.items()):
                rel_path = Path(file_path).relative_to(base_dir)
                print(f"\n  📄 {rel_path}")
                for error in errors:
                    print(f"     Line {error['line']}: {error['issue']}")
                    print(f"     → {error['content'][:100]}")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total files with errors: {sum(len(results) for results in all_results.values())}")
    print(f"Total spacing errors (' >'): {total_spacing_errors}")
    print(f"Total missing prefix errors: {total_prefix_errors}")
    print(f"GRAND TOTAL ERRORS: {total_spacing_errors + total_prefix_errors}")
    print("=" * 80)

if __name__ == '__main__':
    main()
