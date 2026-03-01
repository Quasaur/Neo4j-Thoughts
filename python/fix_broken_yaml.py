#!/usr/bin/env python3
"""
Fix broken YAML front matter in specific files that couldn't be parsed.
"""

import os
import re

# Files with broken YAML
BROKEN_FILES = [
    "content/QUOTES/bom/quote-BEGOTTEN.md",
    "content/THOUGHTS/thought-SCIENCE-CONSPIRACY.md",
    "content/THOUGHTS/thought-ANTI-SEMITISM.md",
    "content/THOUGHTS/thought-DESPISING-THE-CROSS.md",
    "content/THOUGHTS/thought-NO-MATCH.md",
    "content/THOUGHTS/MEEK.md",
    "content/THOUGHTS/thought-INVITE-OR-COMMAND.md",
    "content/THOUGHTS/MOTION.md",
    "content/THOUGHTS/PROTECTION.md",
    "content/THOUGHTS/MIRACLES.md",
    "content/THOUGHTS/thought-GOD-IN-CHARGE.md",
    "content/THOUGHTS/EGO.md",
    "content/THOUGHTS/thought-WHEN-JESUS-RETURNS.md",
    "content/THOUGHTS/thought-THE-QUICK-AND-THE-DEAD.md",
    "content/THOUGHTS/thought-THE-REAL-YOU.md",
    "content/THOUGHTS/thought-SHUT-DOWN.md",
    "content/THOUGHTS/thought-MARK-OF-THE-BEAST.md",
    "content/THOUGHTS/thought-OBLIVION.md",
    "content/THOUGHTS/thought-ONE-REASON.md",
    "content/THOUGHTS/thought-EVIL-WAS-NECESSARY.md",
    "content/PASSAGES/Prov/03/passage-HONOR-GOD.md",
    "content/PASSAGES/Prov/03/passage-KINDNESS-AND-TRUTH.md",
    "content/PASSAGES/Prov/03/passage-PRICELESS-WISDOM.md",
    "content/PASSAGES/Prov/03/passage-INHERITED-HONOR.md",
    "content/PASSAGES/Prov/03/passage-SECURITY-2.md",
]

BASE_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts"

def extract_en_content_from_cypher(content, node_type):
    """Extract en_content from DESCRIPTION or CONTENT node in Cypher block."""
    cypher_blocks = re.findall(r'```Cypher(.*?)```', content, re.DOTALL | re.IGNORECASE)
    
    for block in cypher_blocks:
        if node_type == 'TOPIC':
            match = re.search(r'CREATE\s*\(\s*d\s*:\s*DESCRIPTION\s*\{(.*?)\}', block, re.DOTALL | re.IGNORECASE)
        else:
            match = re.search(r'CREATE\s*\(\s*c\s*:\s*CONTENT\s*\{(.*?)\}', block, re.DOTALL | re.IGNORECASE)
        
        if match:
            props_text = match.group(1)
            en_match = re.search(r'en_content\s*:\s*"((?:[^"\\]|\\.)*)"', props_text, re.DOTALL)
            if en_match:
                return en_match.group(1).replace('\\"', '"')
            en_match = re.search(r"en_content\s*:\s*'((?:[^'\\]|\\.)*)'", props_text, re.DOTALL)
            if en_match:
                return en_match.group(1).replace("\\'", "'")
    
    return None

def parse_frontmatter_raw(content):
    """Parse frontmatter as raw text when YAML parsing fails."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None, None
    
    fm_text = match.group(1)
    rest = content[match.end():]
    
    # Parse properties manually
    props = {}
    lines = fm_text.split('\n')
    current_key = None
    current_value = []
    
    for line in lines:
        # Check if this is a new property (starts at column 0, has colon)
        if line and not line.startswith(' ') and not line.startswith('\t') and ':' in line:
            # Save previous property if exists
            if current_key:
                props[current_key] = '\n'.join(current_value).strip()
            
            key, value = line.split(':', 1)
            current_key = key.strip()
            current_value = [value.strip()] if value.strip() else []
        elif current_key and line.startswith('\t'):
            # Continuation line with tab
            current_value.append(line[1:])  # Remove leading tab
    
    # Save last property
    if current_key:
        props[current_key] = '\n'.join(current_value).strip()
    
    return props, rest

def format_yaml_value(key, value):
    """Format a value for YAML."""
    if not value:
        return '""'
    
    # Check if multi-line
    if '\n' in value:
        # Use literal block scalar
        lines = value.split('\n')
        result = "|"
        for line in lines:
            result += '\n  ' + line
        return result
    else:
        # Single line - quote it and escape internal quotes
        escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'

def fix_file(filepath):
    """Fix a broken YAML file."""
    full_path = os.path.join(BASE_DIR, filepath)
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    # Parse raw frontmatter
    props, rest = parse_frontmatter_raw(content)
    if not props:
        print(f"Could not parse frontmatter in {filepath}")
        return False
    
    # Determine node type
    node_type = props.get('type', 'THOUGHT')
    
    # Extract en_content from Cypher if not present or malformed
    en_content = props.get('en_content', '')
    if not en_content or ':' in en_content[:80]:  # Likely malformed
        en_content_from_cypher = extract_en_content_from_cypher(content, node_type)
        if en_content_from_cypher:
            props['en_content'] = en_content_from_cypher
    
    # Convert ptopic format if needed
    if 'parent' in props and ('ptopic' not in props or not props['ptopic']):
        parent = props['parent'].strip('"')
        parent_link = parent.replace(".", "-")
        props['ptopic'] = f"[[{parent_link}]]"
    
    # Convert tags to single-line if needed
    if 'tags' in props:
        tags = props['tags']
        if isinstance(tags, str) and not tags.startswith('['):
            # Convert multi-line or space-separated to array
            tag_list = [t.strip() for t in tags.replace('\n', ',').split(',') if t.strip()]
            props['tags'] = '[' + ', '.join(f'"{t}"' for t in tag_list) + ']'
    
    # Build new frontmatter
    order = ['type', 'name', 'alias', 'parent', 'en_content', 'tags', 'ptopic', 'level', 'neo4j']
    new_fm_lines = []
    
    for key in order:
        if key in props:
            value = props[key]
            if key == 'tags' and isinstance(value, str) and value.startswith('['):
                new_fm_lines.append(f"{key}: {value}")
            elif key in ['type', 'level', 'neo4j']:
                new_fm_lines.append(f"{key}: {value}")
            else:
                formatted = format_yaml_value(key, value)
                new_fm_lines.append(f"{key}: {formatted}")
    
    # Add any remaining props
    for key, value in props.items():
        if key not in order:
            formatted = format_yaml_value(key, value)
            new_fm_lines.append(f"{key}: {formatted}")
    
    new_content = "---\n" + '\n'.join(new_fm_lines) + "\n---\n" + rest
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    fixed = 0
    failed = 0
    
    for filepath in BROKEN_FILES:
        if fix_file(filepath):
            print(f"✅ Fixed: {filepath}")
            fixed += 1
        else:
            print(f"❌ Failed: {filepath}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Fixed: {fixed}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    main()
