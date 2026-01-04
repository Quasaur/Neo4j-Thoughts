
import os
import re
import argparse
import sys

# Fields to enforce quoting on if they contain spaces
TARGET_FIELDS = {'name', 'alias', 'en_content'}

def needs_quotes(value):
    """
    Check if a value needs quotes:
    - If it contains a space
    - And is not already surrounded by quotes
    """
    if not isinstance(value, str):
        return False
    
    value = value.strip()
    
    # If it's already quoted with " or ', assume it's fine for now (naive check)
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return False
        
    # If it contains a space, it needs quotes
    if ' ' in value:
        return True
        
    return False

def quote_value(value):
    """
    Wrap value in double quotes and escape existing double quotes.
    """
    # Remove surrounding single quotes if present and we are upgrading to double
    if value.startswith("'") and value.endswith("'"):
        value = value[1:-1]
        
    # Escape existing double quotes
    value = value.replace('"', '\\"')
    
    return f'"{value}"'

def process_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_frontmatter = False
    modified = False
    
    # Regex to match key: value pairs
    # Captures: 1=key, 2=value (rest of line)
    # This is a simple regex for YAML frontmatter key-values
    key_val_pattern = re.compile(r'^(\s*)(name|alias|en_content):\s*(.*)$')

    for i, line in enumerate(lines):
        # Detect frontmatter boundaries
        if line.strip() == '---':
            if i == 0:
                in_frontmatter = True
            elif in_frontmatter:
                in_frontmatter = False
        
        if in_frontmatter:
            match = key_val_pattern.match(line)
            if match:
                indent = match.group(1)
                key = match.group(2)
                value = match.group(3)
                
                # Check directly if the string as represented in the file needs quotes
                # This bypasses YAML parsing to preserve comments/ordering/structure exactly
                if needs_quotes(value):
                    new_value = quote_value(value)
                    new_line = f'{indent}{key}: {new_value}\n'
                    new_lines.append(new_line)
                    modified = True
                    print(f"[{'DRY RUN' if dry_run else 'FIX'}] {filepath}: Quoting '{key}'")
                    print(f"  Old: {line.strip()}")
                    print(f"  New: {new_line.strip()}")
                    continue

        new_lines.append(line)

    if modified and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

def main():
    parser = argparse.ArgumentParser(description='Quote specific YAML fields in markdown files.')
    parser.add_argument('--dir', required=True, help='Directory to scan')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without modifying files')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"Error: Directory {args.dir} does not exist.")
        sys.exit(1)

    print(f"Scanning directory: {args.dir}")
    
    count = 0
    for root, dirs, files in os.walk(args.dir):
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file), dry_run=args.dry_run)
                count += 1
                
    print(f"Processed {count} files.")

if __name__ == '__main__':
    main()
