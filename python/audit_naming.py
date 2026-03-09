import os
import re
import yaml
from datetime import datetime

CONTENT_DIR = 'content'
REPORTS_DIR = 'docs/reports'

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")

def check_filename(root, filename):
    errors = []
    node_type = None
    if filename.startswith('topic-'): node_type = 'TOPIC'
    elif filename.startswith('thought-'): node_type = 'THOUGHT'
    elif filename.startswith('quote-'): node_type = 'QUOTE'
    elif filename.startswith('passage-'): node_type = 'PASSAGE'
    
    if not node_type:
        errors.append(f"Invalid prefix: {filename}")
        return errors, None

    # Check folder vs prefix
    folder = os.path.basename(os.path.dirname(os.path.join(root, filename)))
    # Note: folder might be a subfolder like 'bom' or 'Prov/01'
    full_path = os.path.join(root, filename)
    if 'TOPICS' in full_path and node_type != 'TOPIC': errors.append(f"File {filename} in TOPICS folder but has prefix {node_type}")
    if 'THOUGHTS' in full_path and node_type != 'THOUGHT': errors.append(f"File {filename} in THOUGHTS folder but has prefix {node_type}")
    if 'QUOTES' in full_path and node_type != 'QUOTE': errors.append(f"File {filename} in QUOTES folder but has prefix {node_type}")
    if 'PASSAGES' in full_path and node_type != 'PASSAGE': errors.append(f"File {filename} in PASSAGES folder but has prefix {node_type}")

    name_part = filename[len(node_type)+1:-3] # remove prefix and .md
    
    # Rule 1a/1c: CAPITAL LETTERS and dashes
    if not re.match(r'^[A-Z0-9-]+(\([0-9]+\))?$', name_part):
        errors.append(f"Invalid name format: {name_part} (should be ALL-CAPS-WITH-DASHES)")

    # Rule 1e: sequential integer in parentheses
    if re.search(r'[0-9]$', name_part) and not re.search(r'\([0-9]+\)$', name_part):
        # Check if it ends in a number without parentheses (like VOLITION5)
        # Exception: numbers that are part of the name (like 692-189)
        # But if it's like SECURITY-2, it's a violation.
        if '-' in name_part and name_part.split('-')[-1].isdigit():
             errors.append(f"Violation of Rule 1e: {name_part} uses dash-number instead of (number)")
        elif name_part[-1].isdigit() and not name_part[-2].isdigit() and name_part[-2] != '-':
             # Case like VOLITION5 (if VOLITION exists)
             errors.append(f"Violation of Rule 1e: {name_part} uses trailing number instead of (number)")

    # Rule 1d: Max 4 words
    words = name_part.split('-')
    if len(words) > 4:
        errors.append(f"Violation of Rule 1d: {name_part} has {len(words)} words (max 4 recommended)")

    return errors, node_type

def check_yaml(file_path, node_type_from_file):
    errors = []
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            errors.append("Missing YAML front matter")
            return errors

        yaml_str = match.group(1)
        # Check order and approved properties
        lines = yaml_str.strip().split('\n')
        keys = []
        for line in lines:
            if ':' in line:
                keys.append(line.split(':')[0].strip())

        approved_keys = ['type', 'name', 'alias', 'parent', 'en_content', 'tags', 'ptopic', 'level', 'neo4j']
        deprecated_keys = ['mling', 'draft', 'inserted']
        
        # Rule 7e: ONLY approved properties in order
        found_approved = [k for k in keys if k in approved_keys]
        # Check if they are in the correct relative order
        expected_order = [k for k in approved_keys if k in found_approved]
        if found_approved != expected_order:
            errors.append(f"Incorrect YAML property order. Found: {found_approved}, Expected: {expected_order}")

        for k in keys:
            if k in deprecated_keys:
                errors.append(f"Deprecated YAML property found: {k}")
            if k not in approved_keys and k not in deprecated_keys:
                errors.append(f"Unapproved YAML property found: {k}")

        # Rule 3: type
        try:
            data = yaml.safe_load(yaml_str)
        except:
            errors.append("YAML parsing error")
            return errors

        if 'type' not in data:
            errors.append("Missing 'type' in YAML")
        elif data['type'] != node_type_from_file:
            errors.append(f"YAML type '{data['type']}' does not match file prefix '{node_type_from_file}'")

        # Rule 4b: name format "type.NAME WITH SPACES"
        if 'name' in data:
            name_val = data['name']
            prefix = node_type_from_file.lower() + '.'
            if not name_val.startswith(prefix):
                errors.append(f"YAML name '{name_val}' should start with '{prefix}'")
            name_part = name_val[len(prefix):]
            if name_part != name_part.upper():
                 errors.append(f"YAML name '{name_val}' should be in ALL CAPS")
            if '-' in name_part or '_' in name_part:
                 errors.append(f"YAML name '{name_val}' contains dashes or underscores (should use spaces)")

        # Rule 5b: alias format "Type: Initial Caps"
        if 'alias' in data:
            alias_val = data['alias']
            prefix = node_type_from_file.capitalize() + ': '
            if not alias_val.startswith(prefix):
                 errors.append(f"YAML alias '{alias_val}' should start with '{prefix}'")
            # Check for Initial Caps (Rule 5b: words in full capitals are forbidden)
            alias_part = alias_val[len(prefix):]
            if any(word.isupper() and len(word) > 1 for word in re.findall(r'\w+', alias_part)):
                 errors.append(f"YAML alias '{alias_val}' contains full capital words (forbidden)")

        # Rule 9: tags format ["a", "b"]
        # We need to check the raw string for this as yaml.safe_load might hide the format
        if 'tags:' in yaml_str:
            tag_line = [l for l in lines if l.startswith('tags:')][0]
            if '[' not in tag_line or ']' not in tag_line:
                 errors.append(f"YAML tags format violation: should be [\"a\", \"b\"]")
            # Rule 9b: underscores for multi-word tags
            # (Hard to check without knowing what is a multi-word tag, but we can look for spaces)
            if ' ' in tag_line.split('[')[1].split(']')[0] and ',' not in tag_line: # very basic check
                 pass # handled by yaml parsing usually

        # Rule 10b: ptopic format "[[topic-NAME]]"
        if 'ptopic' in data:
            ptopic_val = data['ptopic']
            if not (ptopic_val.startswith('[[topic-') and ptopic_val.endswith(']]')):
                errors.append(f"YAML ptopic '{ptopic_val}' should be in format '[[topic-NAME]]'")

    except Exception as e:
        errors.append(f"Error checking YAML: {str(e)}")
    
    return errors

def main():
    report = []
    all_errors = {}
    
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and file != 'README.md':
                file_path = os.path.join(root, file)
                file_errors, node_type = check_filename(root, file)
                if node_type:
                    yaml_errors = check_yaml(file_path, node_type)
                    file_errors.extend(yaml_errors)
                
                if file_errors:
                    all_errors[file_path] = file_errors

    # Generate Report
    ts = get_timestamp()
    report_filename = f"naming_discrepancy_report_{ts}.md"
    report_path = os.path.join(REPORTS_DIR, report_filename)
    
    with open(report_path, 'w') as f:
        f.write(f"# Naming Discrepancy Report\n")
        f.write(f"Generated: {ts}\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Total files checked: {sum(len(files) for _, _, files in os.walk(CONTENT_DIR))}\n")
        f.write(f"- Files with discrepancies: {len(all_errors)}\n\n")
        
        f.write(f"## Detailed Violations\n\n")
        for path, errors in all_errors.items():
            f.write(f"### `{path}`\n")
            for err in errors:
                f.write(f"- {err}\n")
            f.write(f"\n")

    print(f"Report generated at {report_path}")

if __name__ == "__main__":
    main()
