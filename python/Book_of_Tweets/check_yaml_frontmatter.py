#!/usr/bin/env python3
"""
Check and correct YAML front matter in content and Book_of_Tweets folders
according to docs/Naming/naming_02_yaml.md.md
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
REPORT_PATH = os.path.join(BASE_DIR, "docs", "reports", "yaml_corrections_28-Feb-2026@2105.md")

# Deprecated properties to remove
DEPRECATED_PROPS = ["mling", "draft", "inserted", "title"]

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            fm = yaml.safe_load(match.group(1))
            return fm if isinstance(fm, dict) else {}, match.start(1), match.end(1)
        except yaml.YAMLError:
            pass
    return None, 0, 0

def extract_en_content_from_cypher(content, node_type):
    """Extract en_content from DESCRIPTION or CONTENT node in Cypher block."""
    # Find Cypher blocks
    cypher_blocks = re.findall(r'```Cypher(.*?)```', content, re.DOTALL | re.IGNORECASE)
    
    for block in cypher_blocks:
        if node_type == 'TOPIC':
            # Look for DESCRIPTION node
            match = re.search(r'CREATE\s*\(\s*d\s*:\s*DESCRIPTION\s*\{(.*?)\}', block, re.DOTALL | re.IGNORECASE)
        else:
            # Look for CONTENT node
            match = re.search(r'CREATE\s*\(\s*c\s*:\s*CONTENT\s*\{(.*?)\}', block, re.DOTALL | re.IGNORECASE)
        
        if match:
            props_text = match.group(1)
            # Extract en_content value
            en_match = re.search(r'en_content\s*:\s*"((?:[^"\\]|\\.)*)"', props_text, re.DOTALL)
            if en_match:
                return en_match.group(1).replace('\\"', '"')
            # Try single-quoted version
            en_match = re.search(r"en_content\s*:\s*'((?:[^'\\]|\\.)*)'", props_text, re.DOTALL)
            if en_match:
                return en_match.group(1).replace("\\'", "'")
    
    return None

def format_en_content(value):
    """Format en_content for YAML front matter using literal block scalar."""
    if not value:
        return '""'
    
    # Clean up line endings
    value = value.replace('\r\n', '\n').replace('\r', '\n')
    
    # Check if multi-line (contains newline)
    if '\n' in value:
        # Multi-line: use literal block scalar (|) which preserves newlines
        lines = value.split('\n')
        # Remove empty lines at start/end
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        
        if not lines:
            return '""'
        
        # Use literal block scalar with 2-space indentation for subsequent lines
        # This avoids issues with tabs and special characters like colons
        formatted = "|"
        for line in lines:
            formatted += '\n  ' + line
        return formatted
    else:
        # Single-line: wrap in quotes, escape internal quotes and backslashes
        escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'

def convert_parent_to_ptopic(parent_value):
    """Convert parent value to ptopic format."""
    if not parent_value:
        return None
    parent_clean = parent_value.strip('"')
    parent_link = parent_clean.replace(".", "-")
    return f"[[{parent_link}]]"

def fix_alias(alias_value, node_type):
    """Fix alias format to be 'NodeType: Title'."""
    if not alias_value:
        return None
    
    alias_clean = alias_value.strip('"')
    
    type_prefixes = ["Topic: ", "Thought: ", "Quote: ", "Passage: "]
    for prefix in type_prefixes:
        if alias_clean.startswith(prefix):
            parts = alias_clean.split(": ", 1)
            if len(parts) == 2:
                return f"{parts[0]}: {parts[1]}"
    
    type_map = {
        "TOPIC": "Topic",
        "THOUGHT": "Thought", 
        "QUOTE": "Quote",
        "PASSAGE": "Passage"
    }
    
    prefix = type_map.get(node_type, node_type.capitalize())
    
    if alias_clean.lower().startswith(prefix.lower() + ":"):
        alias_clean = alias_clean.split(":", 1)[1].strip()
    
    return f"{prefix}: {alias_clean}"

def format_tags(tags_value):
    """Convert tags to single-line array format."""
    if not tags_value:
        return None
    
    if isinstance(tags_value, list):
        tags_str = ', '.join(f'"{tag}"' for tag in tags_value)
        return f"[{tags_str}]"
    elif isinstance(tags_value, str):
        if tags_value.startswith('[') and tags_value.endswith(']'):
            return tags_value
        return f'["{tags_value}"]'
    
    return None

def check_and_fix_file(filepath, corrections):
    """Check and fix YAML frontmatter in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"Error reading: {e}", False
    
    fm, start, end = extract_frontmatter(content)
    if not fm:
        return "No valid frontmatter found", False
    
    changes = []
    
    # Get node type
    node_type = fm.get("type", "").upper()
    if not node_type:
        return "No type specified", False
    
    # Derive name from filename if missing
    if "name" not in fm:
        filename = os.path.basename(filepath)
        # Remove extension and type prefix
        name_part = filename.replace('.md', '')
        if '-' in name_part:
            # Remove type prefix (e.g., "thought-")
            name_part = name_part.split('-', 1)[1]
        # Create full name with type prefix
        fm["name"] = f"{node_type.lower()}.{name_part}"
        changes.append(f"Added name from filename")
    
    # Check for deprecated properties
    for prop in DEPRECATED_PROPS:
        if prop in fm:
            if prop == "title" and "alias" not in fm:
                fm["alias"] = fm.pop(prop)
                changes.append(f"Converted 'title' to 'alias'")
            else:
                del fm[prop]
                changes.append(f"Removed deprecated property '{prop}'")
    
    # Fix alias format
    if "alias" in fm:
        new_alias = fix_alias(fm["alias"], node_type)
        if new_alias != fm["alias"]:
            fm["alias"] = new_alias
            changes.append(f"Fixed alias format")
    
    # Fix tags format
    if "tags" in fm:
        new_tags = format_tags(fm["tags"])
        if new_tags != fm["tags"]:
            fm["tags"] = new_tags
            changes.append(f"Converted tags to single-line format")
    
    # Add ptopic if parent exists
    if "parent" in fm and "ptopic" not in fm:
        ptopic = convert_parent_to_ptopic(fm["parent"])
        if ptopic:
            fm["ptopic"] = ptopic
            changes.append(f"Added ptopic")
    
    # Extract and add en_content from Cypher block if missing
    if "en_content" not in fm:
        en_content_from_cypher = extract_en_content_from_cypher(content, node_type)
        if en_content_from_cypher:
            fm["en_content"] = en_content_from_cypher
            changes.append(f"Added en_content from Cypher block")
    
    # Define correct property order
    correct_order = ["type", "name", "alias", "parent", "en_content", "tags", "ptopic", "level", "neo4j"]
    
    # Reorder properties
    ordered_fm = {}
    for prop in correct_order:
        if prop in fm:
            ordered_fm[prop] = fm[prop]
    
    # Add any remaining properties not in standard order
    for prop, value in fm.items():
        if prop not in ordered_fm:
            ordered_fm[prop] = value
    
    if changes and corrections:
        # Reconstruct frontmatter
        new_fm_yaml = "\n".join(format_yaml_line(k, v) for k, v in ordered_fm.items())
        new_content = content[:start-4] + "---\n" + new_fm_yaml + "\n---\n" + content[end+4:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return changes, len(changes) > 0

def format_yaml_line(key, value):
    """Format a YAML key-value pair."""
    if key == "tags" and isinstance(value, str) and value.startswith('['):
        return f"{key}: {value}"
    elif key == "en_content" and value:
        formatted = format_en_content(value)
        return f"{key}: {formatted}"
    elif key in ["type", "level", "neo4j"]:
        if isinstance(value, bool):
            return f"{key}: {str(value).lower()}"
        return f"{key}: {value}"
    elif value is None:
        return f"{key}:"
    elif isinstance(value, list):
        items = ', '.join(f'"{item}"' for item in value)
        return f"{key}: [{items}]"
    else:
        val_str = str(value).replace('"', '\\"')
        return f'{key}: "{val_str}"'

def scan_files(directory, corrections):
    """Scan directory for markdown files and check YAML."""
    results = []
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', '.venv', '.venv_new']]
        
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, BASE_DIR)
            
            changes, was_modified = check_and_fix_file(filepath, corrections)
            
            if isinstance(changes, str):
                results.append({
                    'file': rel_path,
                    'error': changes,
                    'changes': []
                })
            elif changes:
                results.append({
                    'file': rel_path,
                    'error': None,
                    'changes': changes,
                    'modified': was_modified
                })
    
    return results

def generate_report(results):
    """Generate the markdown report."""
    report_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    total_files = len(results)
    files_with_errors = len([r for r in results if r.get('error')])
    files_with_changes = len([r for r in results if r.get('changes')])
    files_modified = len([r for r in results if r.get('modified')])
    
    report = f"""# YAML Front Matter Corrections Report

**Generated:** {report_date}

## Summary

| Category | Count |
|----------|-------|
| Total Files Checked | {total_files} |
| Files with Errors | {files_with_errors} |
| Files Needing Changes | {files_with_changes} |
| Files Modified | {files_modified} |

---

## YAML Naming Convention Rules Applied

Based on `docs/Naming/naming_02_yaml.md.md`:

### Deprecated Properties Removed
- `mling` - Multilingual indicator
- `draft` - Draft status
- `inserted` - Upload status
- `title` - Converted to `alias` if `alias` doesn't exist

### Required Properties (in order)
1. **type** - Node type (TOPIC, THOUGHT, QUOTE, PASSAGE)
2. **name** - Node name (e.g., "topic.THE GODHEAD")
3. **alias** - Display alias (e.g., "Topic: The Godhead")
4. **parent** - Parent topic name
5. **en_content** - English content from DESCRIPTION/CONTENT node
6. **tags** - Tags array (single-line format)
7. **ptopic** - Obsidian parent link (e.g., "[[topic-THE-GODHEAD]]")
8. **level** - Hierarchy level (integer)
9. **neo4j** - Upload status (boolean)

### Corrections Made
- Converted `title` property to `alias`
- Fixed `alias` format to "NodeType: Title"
- Converted `tags` to single-line array format
- Added `ptopic` property derived from `parent`
- Extracted `en_content` from Cypher block DESCRIPTION/CONTENT nodes
- Formatted `en_content` for single-line or multi-line YAML
- Reordered properties to standard order
- Removed deprecated properties

---

## Files Modified

| File | Changes |
|------|---------|
"""
    
    for result in results:
        if result.get('changes'):
            changes_str = "; ".join(result['changes'])
            report += f"| {result['file']} | {changes_str} |\n"
    
    if not any(r.get('changes') for r in results):
        report += "\n**No files required YAML corrections.**\n"
    
    report += """
---

## Files with Errors

| File | Error |
|------|-------|
"""
    
    for result in results:
        if result.get('error'):
            report += f"| {result['file']} | {result['error']} |\n"
    
    if not any(r.get('error') for r in results):
        report += "\n**No files had errors.**\n"
    
    report += """
---

## Detailed Change Log

"""
    
    for result in results:
        if result.get('changes'):
            report += f"\n### {result['file']}\n"
            for change in result['changes']:
                report += f"- {change}\n"
    
    report += "\n---\n\n*Report generated by check_yaml_frontmatter.py*\n"
    
    return report

def main():
    """Main function to check and optionally correct YAML frontmatter."""
    print("=" * 80)
    print("YAML Front Matter Convention Checker")
    print("=" * 80)
    print()
    
    all_results = []
    
    print("Scanning content folder...")
    content_results = scan_files(CONTENT_DIR, corrections=True)
    all_results.extend(content_results)
    print(f"  Checked {len(content_results)} files")
    
    print("\nScanning Book_of_Tweets/THOUGHTS folder...")
    bot_thoughts_dir = os.path.join(BOOK_OF_TWEETS_DIR, "THOUGHTS")
    if os.path.exists(bot_thoughts_dir):
        bot_results = scan_files(bot_thoughts_dir, corrections=True)
        all_results.extend(bot_results)
        print(f"  Checked {len(bot_results)} files")
    
    print("\nGenerating report...")
    report = generate_report(all_results)
    
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Report saved to: {REPORT_PATH}")
    
    files_with_changes = len([r for r in all_results if r.get('changes')])
    files_with_errors = len([r for r in all_results if r.get('error')])
    files_modified = len([r for r in all_results if r.get('modified')])
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files checked:      {len(all_results)}")
    print(f"Files with changes: {files_with_changes}")
    print(f"Files modified:     {files_modified}")
    print(f"Files with errors:  {files_with_errors}")
    print("=" * 80)

if __name__ == "__main__":
    main()
