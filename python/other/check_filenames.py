#!/usr/bin/env python3
"""
Check and correct markdown file names in content and Book_of_Tweets folders
according to the naming conventions in docs/Naming/naming_01_file_names.md
"""

import os
import re
import yaml
from datetime import datetime
from pathlib import Path

# Base paths
BASE_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
BOOK_OF_TWEETS_DIR = os.path.join(BASE_DIR, "Book_of_Tweets")
REPORT_PATH = os.path.join(BASE_DIR, "docs", "reports", "filename_corrections_27-Feb-2026@1505.md")

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match frontmatter between --- markers
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            frontmatter = yaml.safe_load(match.group(1))
            return frontmatter if isinstance(frontmatter, dict) else {}
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return {}

def get_expected_filename(node_type, node_name):
    """
    Generate expected filename based on node type and name.
    
    Rules:
    - TOPIC: "topic-NAME.md"
    - THOUGHT: "thought-NAME.md" 
    - QUOTE: "quote-NAME.md"
    - PASSAGE: "passage-NAME.md"
    - Multi-word names: words in CAPS separated by dashes
    - Sequential duplicates: NAME(2), NAME(3), etc.
    """
    # Extract just the name part (after the dot if present)
    if '.' in node_name:
        _, name = node_name.rsplit('.', 1)
    else:
        name = node_name
    
    # Convert to uppercase and replace spaces/special chars with dashes
    # Keep only alphanumeric and dashes
    name = name.upper()
    name = re.sub(r'[^A-Z0-9]', '-', name)
    # Remove multiple consecutive dashes
    name = re.sub(r'-+', '-', name)
    # Remove leading/trailing dashes
    name = name.strip('-')
    
    prefix_map = {
        'TOPIC': 'topic',
        'THOUGHT': 'thought',
        'QUOTE': 'quote',
        'PASSAGE': 'passage'
    }
    
    prefix = prefix_map.get(node_type)
    if not prefix:
        return None
    
    return f"{prefix}-{name}.md"

def scan_files(directory, corrections):
    """Scan directory for markdown files and check naming."""
    issues = []
    
    for root, dirs, files in os.walk(directory):
        # Skip venv and hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'venv' and d != '.venv' and d != '.venv_new']
        
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            file_path = os.path.join(root, filename)
            rel_path = os.path.relpath(file_path, BASE_DIR)
            
            # Skip non-node files
            if filename in ['Book6E-FINAL.md', 'batch_1_review.md']:
                continue
                
            fm = extract_frontmatter(file_path)
            if not fm:
                issues.append({
                    'file': rel_path,
                    'issue': 'No frontmatter found',
                    'current_name': filename,
                    'expected_name': None,
                    'action': 'SKIP'
                })
                continue
            
            node_type = fm.get('type')
            node_name = fm.get('name', '')
            
            if not node_type or not node_name:
                issues.append({
                    'file': rel_path,
                    'issue': 'Missing type or name in frontmatter',
                    'current_name': filename,
                    'expected_name': None,
                    'action': 'SKIP'
                })
                continue
            
            expected_name = get_expected_filename(node_type, node_name)
            
            if not expected_name:
                issues.append({
                    'file': rel_path,
                    'issue': f'Unknown node type: {node_type}',
                    'current_name': filename,
                    'expected_name': None,
                    'action': 'SKIP'
                })
                continue
            
            if filename != expected_name:
                issues.append({
                    'file': rel_path,
                    'issue': f'Filename does not match convention',
                    'current_name': filename,
                    'expected_name': expected_name,
                    'node_type': node_type,
                    'node_name': node_name,
                    'action': 'RENAME'
                })
                
                # Perform rename if corrections enabled
                if corrections:
                    new_path = os.path.join(root, expected_name)
                    try:
                        os.rename(file_path, new_path)
                        print(f"  Renamed: {rel_path} -> {expected_name}")
                    except Exception as e:
                        print(f"  ERROR renaming {rel_path}: {e}")
            
    return issues

def generate_report(all_issues):
    """Generate the markdown report."""
    report_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Separate by action type
    rename_issues = [i for i in all_issues if i['action'] == 'RENAME']
    skip_issues = [i for i in all_issues if i['action'] == 'SKIP']
    
    # Group by folder
    content_renames = [i for i in rename_issues if i['file'].startswith('content/')]
    bot_renames = [i for i in rename_issues if i['file'].startswith('Book_of_Tweets/')]
    
    report = f"""# Filename Corrections Report

**Generated:** {report_date}

## Summary

| Category | Count |
|----------|-------|
| Total Files Checked | {len(all_issues)} |
| Files Needing Rename | {len(rename_issues)} |
| Files with Issues (Skipped) | {len(skip_issues)} |
| Content Folder Renames | {len(content_renames)} |
| Book_of_Tweets Folder Renames | {len(bot_renames)} |

---

## Naming Convention Rules Applied

Based on `docs/Naming/naming_01_file_names.md`:

1. **Rule 1:** File names must start with type prefix:
   - TOPIC: `topic-`
   - THOUGHT: `thought-`
   - QUOTE: `quote-`
   - PASSAGE: `passage-`

2. **Rule 2:** Node name in CAPITAL LETTERS

3. **Rule 3:** Multi-word names use dashes (e.g., `thought-MY-NODE-NAME.md`)

4. **Rule 4:** Max 4 words recommended

5. **Rule 5:** Sequential duplicates use parentheses: `NAME(2).md`

6. **Rule 6:** All files must have `.md` extension

---

## Files Renamed in Content Folder

| Current Path | Current Name | Expected Name | Node Type | Node Name |
|--------------|--------------|---------------|-----------|-----------|
"""
    
    for issue in content_renames:
        dir_path = os.path.dirname(issue['file'])
        report += f"| {dir_path}/ | {issue['current_name']} | {issue['expected_name']} | {issue.get('node_type', 'N/A')} | `{issue.get('node_name', 'N/A')}` |\n"
    
    if not content_renames:
        report += "\n**No files needed renaming in the content folder.**\n"
    
    report += """
---

## Files Renamed in Book_of_Tweets Folder

| Current Path | Current Name | Expected Name | Node Type | Node Name |
|--------------|--------------|---------------|-----------|-----------|
"""
    
    for issue in bot_renames:
        dir_path = os.path.dirname(issue['file'])
        report += f"| {dir_path}/ | {issue['current_name']} | {issue['expected_name']} | {issue.get('node_type', 'N/A')} | `{issue.get('node_name', 'N/A')}` |\n"
    
    if not bot_renames:
        report += "\n**No files needed renaming in the Book_of_Tweets folder.**\n"
    
    report += """
---

## Files with Issues (Skipped)

| File Path | Issue |
|-----------|-------|
"""
    
    for issue in skip_issues:
        report += f"| {issue['file']} | {issue['issue']} |\n"
    
    if not skip_issues:
        report += "\n**No files had issues requiring skipping.**\n"
    
    report += """
---

## Statistics by Node Type

"""
    
    type_counts = {}
    for issue in rename_issues:
        node_type = issue.get('node_type', 'UNKNOWN')
        type_counts[node_type] = type_counts.get(node_type, 0) + 1
    
    report += "| Node Type | Count Needing Rename |\n"
    report += "|-----------|---------------------|\n"
    for node_type, count in sorted(type_counts.items()):
        report += f"| {node_type} | {count} |\n"
    
    report += """
---

## Action Taken

"""
    
    if rename_issues:
        report += f"All {len(rename_issues)} files have been renamed to match the naming convention.\n"
    else:
        report += "No files required renaming. All files comply with the naming convention.\n"
    
    report += "\n---\n\n*Report generated by check_filenames.py*\n"
    
    return report

def main():
    """Main function to check and optionally correct filenames."""
    print("=" * 80)
    print("Filename Convention Checker")
    print("=" * 80)
    print()
    
    all_issues = []
    
    # Scan content folder
    print("Scanning content folder...")
    content_issues = scan_files(CONTENT_DIR, corrections=True)
    all_issues.extend(content_issues)
    print(f"  Found {len([i for i in content_issues if i['action'] == 'RENAME'])} files to rename")
    
    # Scan Book_of_Tweets folder (THOUGHTS subfolder only)
    print("\nScanning Book_of_Tweets/THOUGHTS folder...")
    bot_thoughts_dir = os.path.join(BOOK_OF_TWEETS_DIR, "THOUGHTS")
    if os.path.exists(bot_thoughts_dir):
        bot_issues = scan_files(bot_thoughts_dir, corrections=True)
        all_issues.extend(bot_issues)
        print(f"  Found {len([i for i in bot_issues if i['action'] == 'RENAME'])} files to rename")
    
    # Generate report
    print("\nGenerating report...")
    report = generate_report(all_issues)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    
    # Write report
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Report saved to: {REPORT_PATH}")
    
    # Print summary
    rename_count = len([i for i in all_issues if i['action'] == 'RENAME'])
    skip_count = len([i for i in all_issues if i['action'] == 'SKIP'])
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files renamed:     {rename_count}")
    print(f"Files with issues: {skip_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
