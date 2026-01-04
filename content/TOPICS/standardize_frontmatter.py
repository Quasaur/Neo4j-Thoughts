import os
import re
import yaml

ROOT_DIR = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/TOPICS"

def extract_cypher_fields(cypher_block):
    """
    Extracts name, alias, and parent from valid Cypher syntax.
    """
    # Regex designed to catch properties inside key: "value" or key: value
    # We look specifically for the CREATE (t:TOPIC ...) block content
    
    # 1. Isolate the CREATE (t:TOPIC { ... }) block
    # This matches the first CREATE (t:TOPIC ... }) occurrence
    create_match = re.search(r'CREATE\s*\(t:TOPIC\s*\{(.*?)\}\);', cypher_block, re.DOTALL | re.IGNORECASE)
    if not create_match:
        # Fallback: maybe just search the whole block, 
        # but matching specific T:TOPIC block is safer to avoid confusion with DESCRIPTION node
        content_to_search = cypher_block
    else:
        content_to_search = create_match.group(1)

    name_match = re.search(r'name:\s*"(.*?)"', content_to_search)
    alias_match = re.search(r'alias:\s*"(.*?)"', content_to_search)
    # Parent can be "string" or null
    parent_match = re.search(r'parent:\s*(".*?"|null)', content_to_search)
    
    extracted = {}
    if name_match:
        extracted['name'] = name_match.group(1)
    if alias_match:
        extracted['alias'] = alias_match.group(1)
    if parent_match:
        val = parent_match.group(1)
        if val == 'null':
            extracted['parent'] = "null" # Keep as string "null" as per user preference
        else:
            extracted['parent'] = val.strip('"')
            
    return extracted

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Split FM
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        print(f"Skipping {os.path.basename(file_path)}: Invalid frontmatter")
        return

    fm_raw = parts[1]
    body = parts[2]

    # Parse YAML
    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict):
             print(f"Skipping {os.path.basename(file_path)}: FM not dict")
             return
    except Exception as e:
        print(f"Skipping {os.path.basename(file_path)}: YAML error {e}")
        return

    # Extract Cypher
    cypher_match = re.search(r'```Cypher(.*?)```', body, re.DOTALL | re.IGNORECASE)
    if not cypher_match:
        print(f"Skipping {os.path.basename(file_path)}: No Cypher block")
        return
    
    cypher_data = extract_cypher_fields(cypher_match.group(1))
    
    if 'name' not in cypher_data or 'alias' not in cypher_data:
        print(f"Warning: Missing name/alias in Cypher for {os.path.basename(file_path)}")
        # We might continue with what we have, but let's be careful
        # User said "copy ... from the TOPIC CREATE query". 
        # If extraction fails, we can't copy.
    
    # Construct New Order
    # 1. Name
    # 2. Alias
    # 3. Others (excluding name, alias, type, parent)
    # 4. Type
    # 5. Parent
    
    new_fm = {}
    
    # 1. Name
    if 'name' in cypher_data:
        new_fm['name'] = cypher_data['name']
    elif 'name' in fm:
        new_fm['name'] = fm['name']
        
    # 2. Alias
    if 'alias' in cypher_data:
        new_fm['alias'] = cypher_data['alias']
    elif 'alias' in fm:
        new_fm['alias'] = fm['alias']

    # 3. Type (User just said parent after type, didn't strictly say Type must be 3rd, 
    # but "first two... name and alias". So Type can be 3rd or later. 
    # Let's put Type next to be clean, or put it after "others"?
    # "place [parent] ... AFTER "type"". 
    # Let's check topic-NULL.md again: name, alias, type, parent, tags...
    # I'll stick to that order.
    
    type_val = fm.get('type', 'TOPIC')
    new_fm['type'] = type_val
    
    # 4. Parent
    # "place it ... AFTER "type", if missing."
    # Use Cypher parent if avail, else existing FM parent ?? 
    # User: "copy the "parent" ... from the same block"
    if 'parent' in cypher_data and cypher_data['parent']:
        new_fm['parent'] = cypher_data['parent']
    elif 'parent' in fm:
        new_fm['parent'] = fm['parent']
    
    # 5. Others
    # Filter out keys we've already handled
    skip_keys = {'name', 'alias', 'type', 'parent'}
    
    # We want to preserve existing keys (tags, neo4j, level, etc.)
    for k, v in fm.items():
        if k not in skip_keys:
            new_fm[k] = v
    # Custom representer for quoted strings
    class QuotedString(str):
        pass

    def quoted_scalar_representer(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

    yaml.add_representer(QuotedString, quoted_scalar_representer)

    new_fm_ready = {}
    for k, v in new_fm.items():
        if isinstance(v, str) and ' ' in v:
            new_fm_ready[k] = QuotedString(v)
        else:
            new_fm_ready[k] = v
            
    # Dump
    new_fm_str = yaml.dump(new_fm_ready, sort_keys=False, allow_unicode=True).strip()
    
    new_content = f"---\n{new_fm_str}\n---\n{body}"
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    print(f"Updated {os.path.basename(file_path)}")

def main():
    for filename in os.listdir(ROOT_DIR):
        if filename.startswith("topic-") and filename.endswith(".md"):
            process_file(os.path.join(ROOT_DIR, filename))

if __name__ == "__main__":
    main()
