#!/usr/bin/env python3
"""
Fix edge name property errors in Cypher blocks.
Fixes two types of errors:
1. " >" spacing error (replace with "->")
2. Missing edge prefix (add edge., t.edge., q.edge., p.edge. based on relationship type)
"""

import re
from pathlib import Path
from collections import defaultdict

def fix_file(file_path):
    """Fix edge name property errors in a single file."""
    changes = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        original_lines = content.split('\n')
    
    modified_lines = []
    made_changes = False
    
    for i, line in enumerate(original_lines, 1):
        original_line = line
        
        # Only process MERGE statements with relationship types we care about
        if 'MERGE' in line and (':HAS_CHILD' in line or ':HAS_THOUGHT' in line or ':HAS_QUOTE' in line or ':HAS_PASSAGE' in line):
            
            # Fix 1: Replace " >" with "->"
            if ' >' in line and ' >-' not in line:
                line = line.replace(' >', '->')
                changes.append({
                    'line_num': i,
                    'type': 'spacing',
                    'before': original_line.strip(),
                    'after': line.strip()
                })
                made_changes = True
            
            # Fix 2: Add missing edge prefix
            name_match = re.search(r'name:\s*"([^"]+)"', line)
            if name_match:
                current_name = name_match.group(1)
                new_name = None
                
                if ':HAS_CHILD' in line and not current_name.startswith('edge.'):
                    # TOPIC->TOPIC should have "edge."
                    new_name = f"edge.{current_name}"
                elif ':HAS_THOUGHT' in line and not current_name.startswith('t.edge.'):
                    # TOPIC->THOUGHT should have "t.edge."
                    # Remove "edge." if present and add "t.edge."
                    clean_name = current_name.replace('edge.', '')
                    new_name = f"t.edge.{clean_name}"
                elif ':HAS_QUOTE' in line and not current_name.startswith('q.edge.'):
                    # TOPIC->QUOTE should have "q.edge."
                    clean_name = current_name.replace('edge.', '')
                    new_name = f"q.edge.{clean_name}"
                elif ':HAS_PASSAGE' in line and not current_name.startswith('p.edge.'):
                    # TOPIC->PASSAGE should have "p.edge."
                    clean_name = current_name.replace('edge.', '')
                    new_name = f"p.edge.{clean_name}"
                
                if new_name:
                    old_pattern = f'name: "{current_name}"'
                    new_pattern = f'name: "{new_name}"'
                    line = line.replace(old_pattern, new_pattern)
                    changes.append({
                        'line_num': i,
                        'type': 'prefix',
                        'before': original_line.strip(),
                        'after': line.strip()
                    })
                    made_changes = True
        
        modified_lines.append(line)
    
    # Write back if changes were made
    if made_changes:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(modified_lines))
    
    return changes

def fix_directory(directory):
    """Fix all markdown files in a directory."""
    results = defaultdict(list)
    
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"⚠️  Directory not found: {directory}")
        return results
    
    for md_file in sorted(dir_path.rglob('*.md')):
        changes = fix_file(md_file)
        if changes:
            results[str(md_file)] = changes
    
    return results

def main():
    base_dir = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts")
    
    print("=" * 80)
    print("FIXING EDGE NAME PROPERTY ERRORS")
    print("=" * 80)
    
    # Fix both directories
    directories = [
        base_dir / "Book_of_Tweets",
        base_dir / "content"
    ]
    
    all_results = {}
    total_spacing_fixes = 0
    total_prefix_fixes = 0
    
    for directory in directories:
        print(f"\n📂 Processing: {directory.relative_to(base_dir)}")
        results = fix_directory(directory)
        all_results[str(directory)] = results
        
        spacing_count = sum(1 for file_changes in results.values() 
                          for change in file_changes if change['type'] == 'spacing')
        prefix_count = sum(1 for file_changes in results.values() 
                         for change in file_changes if change['type'] == 'prefix')
        
        print(f"   Files modified: {len(results)}")
        print(f"   Spacing fixes (' >' -> '->'): {spacing_count}")
        print(f"   Prefix fixes: {prefix_count}")
        
        total_spacing_fixes += spacing_count
        total_prefix_fixes += prefix_count
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total files modified: {sum(len(results) for results in all_results.values())}")
    print(f"Total spacing fixes: {total_spacing_fixes}")
    print(f"Total prefix fixes: {total_prefix_fixes}")
    print(f"GRAND TOTAL FIXES: {total_spacing_fixes + total_prefix_fixes}")
    print("=" * 80)
    
    # Save detailed change log
    log_path = base_dir / "CYPHER" / "CORRECTIONS" / "edge_corrections_log.txt"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(log_path, 'w', encoding='utf-8') as log:
        log.write("EDGE NAME PROPERTY CORRECTIONS LOG\n")
        log.write("=" * 80 + "\n\n")
        
        for directory, results in all_results.items():
            if results:
                log.write(f"\nDIRECTORY: {Path(directory).name}/\n")
                log.write("-" * 80 + "\n")
                
                for file_path, changes in sorted(results.items()):
                    rel_path = Path(file_path).relative_to(base_dir)
                    log.write(f"\nFILE: {rel_path}\n")
                    
                    for change in changes:
                        log.write(f"  Line {change['line_num']} ({change['type']} fix):\n")
                        log.write(f"    BEFORE: {change['before']}\n")
                        log.write(f"    AFTER:  {change['after']}\n")
                    log.write("\n")
        
        log.write("\n" + "=" * 80 + "\n")
        log.write(f"Total files modified: {sum(len(results) for results in all_results.values())}\n")
        log.write(f"Total spacing fixes: {total_spacing_fixes}\n")
        log.write(f"Total prefix fixes: {total_prefix_fixes}\n")
        log.write(f"GRAND TOTAL: {total_spacing_fixes + total_prefix_fixes}\n")
    
    print(f"\n📝 Detailed change log saved to: {log_path}")
    
    return all_results

if __name__ == '__main__':
    main()
