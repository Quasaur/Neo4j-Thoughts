import os
import re
import yaml

# Configuration
SOURCE_CYPHER_ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/DATA/QUOTES"
# SECONDARY_CYPHER_ROOT - Removed
DEST_MARKDOWN_ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/QUOTES"
FIELDS_TO_REMOVE = ["title", "mling", "draft"]

# Custom representer for quoted strings
class QuotedString(str):
    pass

def quoted_scalar_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

yaml.add_representer(QuotedString, quoted_scalar_representer)

def find_cypher_file(target_name):
    """
    Search key strategies:
    1. Exact match in secondary root (files end in .cypher).
    2. Recursive search in primary root for files ending with 'target_name.md' or 'quote-target_name.md'.
    """
    # Target name comes from filename like 'ADOPTION2.md' or 'quote-ADOPTION2.md'
    base_name = target_name.replace(".md", "")
    
    # Strategy 1: Check Secondary (.cypher) - Skipped as legacy path removed
    # search_names_secondary = [ ... ]
    
    # for root, _, files in os.walk(SECONDARY_CYPHER_ROOT):
    #     for file in files:
    #         if file in search_names_secondary:
    #             return os.path.join(root, file)

    # Strategy 2: Check Primary (.md)
    search_names_primary = [
        f"quote-{base_name}.md",
        f"{base_name}.md",
        f"quote-{base_name.replace('-', ' ')}.md",
        f"{base_name.replace('-', ' ')}.md",
        f"quote-THE {base_name.replace('-', ' ')}.md",
        f"THE {base_name.replace('-', ' ')}.md"
    ]
    
    # Handle "NAME2" -> "NAME (2)"
    if base_name[-1].isdigit():
        core = base_name[:-1]
        digit = base_name[-1]
        search_names_primary.extend([
            f"quote-{core} ({digit}).md",
            f"{core} ({digit}).md"
        ])
    
    for root, _, files in os.walk(SOURCE_CYPHER_ROOT):
        for file in files:
            # Check if file ends with any pattern (ignoring 000X- prefix)
            for pat in search_names_primary:
                if file.endswith(pat):
                     return os.path.join(root, file)
    
    return None

def extract_cypher_block(file_path):
    """Extracts the content between ```Cypher and ``` tags, or raw content if .cypher."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
            if file_path.endswith(".cypher"):
                return f"```Cypher\n{content}\n```"
            
            match = re.search(r'```Cypher(.*?)```', content, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(0) 
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def extract_metadata_from_cypher(cypher_block):
    """Extract name, alias, parent from Cypher block."""
    create_match = re.search(r'CREATE\s*\(q:QUOTE\s*\{(.*?)\}\);', cypher_block, re.DOTALL | re.IGNORECASE)
    content = create_match.group(1) if create_match else cypher_block
    
    extracted = {}
    
    name_match = re.search(r'name:\s*"(.*?)"', content)
    alias_match = re.search(r'alias:\s*"(.*?)"', content)
    parent_match = re.search(r'parent:\s*(".*?"|null)', content)
    
    if name_match: extracted['name'] = name_match.group(1)
    if alias_match: extracted['alias'] = alias_match.group(1)
    if parent_match:
        val = parent_match.group(1)
        extracted['parent'] = "null" if val == 'null' else val.strip('"')
            
    return extracted

def process_file(file_path):
    filename = os.path.basename(file_path)
    print(f"Processing {filename}...")
    
    with open(file_path, 'r') as f:
        content = f.read()

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    
    if len(parts) >= 3:
        frontmatter_raw = parts[1]
    else:
        print(f"Skipping {filename}: Invalid frontmatter.")
        return

    # Find Source
    cypher_path = find_cypher_file(filename)
    if not cypher_path:
        print(f"Warning: No source found for {filename}")
        return

    cypher_block = extract_cypher_block(cypher_path)
    if not cypher_block:
         print(f"Warning: No Cypher block found in {cypher_path}")
         return

    # Extract new metadata
    cypher_meta = extract_metadata_from_cypher(cypher_block)

    # Process YAML
    try:
        fm = yaml.safe_load(frontmatter_raw)
        if not isinstance(fm, dict): return

        # Remove fields
        for field in FIELDS_TO_REMOVE:
            if field in fm: del fm[field]
        
        # Build new FM with strict ordering
        new_fm = {}
        
        # 1. Name
        if 'name' in cypher_meta: new_fm['name'] = cypher_meta['name']
        elif 'name' in fm: new_fm['name'] = fm['name']
        
        # 2. Alias
        if 'alias' in cypher_meta: new_fm['alias'] = cypher_meta['alias']
        elif 'alias' in fm: new_fm['alias'] = fm['alias']
        
        # 3. Type
        new_fm['type'] = 'QUOTE'
        
        # 4. Parent
        if 'parent' in cypher_meta: new_fm['parent'] = cypher_meta['parent']
        elif 'parent' in fm: new_fm['parent'] = fm['parent']
        
        # 5. Others
        skip = {'name', 'alias', 'type', 'parent'}
        for k, v in fm.items():
            if k not in skip: new_fm[k] = v
            
        # Apply strict quoting
        final_fm = {}
        for k, v in new_fm.items():
            if isinstance(v, str) and ' ' in v:
                final_fm[k] = QuotedString(v)
            else:
                final_fm[k] = v

        new_frontmatter = yaml.dump(final_fm, sort_keys=False, allow_unicode=True).strip()
    except yaml.YAMLError as e:
        print(f"Skipping {filename}: YAML error {e}")
        return

    new_content = f"---\n{new_frontmatter}\n---\n{cypher_block}\n"
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    print(f"Updated {filename}")

def main():
    # Recursive walk for destination
    for root, _, files in os.walk(DEST_MARKDOWN_ROOT):
        for file in files:
            if file.endswith(".md") and not file.startswith("."):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
