import os
import re
import yaml

# Configuration
SOURCE_CYPHER_ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/DATA/TOPICS"
# SECONDARY_CYPHER_ROOT - Removed as it referred to deleted repo
DEST_MARKDOWN_ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/TOPICS"
FIELDS_TO_REMOVE = ["title", "mling", "draft"]

def find_cypher_file(topic_name):
    """Recursively search for a cypher file matching the topic name."""
    # Matches: 0001-topic-NAME.md or just topic-NAME.md
    # Also tries to match ignoring the '00XX-' prefix effectively
    
    # Standardize target name: remove extension, remove potential 'topic-' prefix if we want to be loose, 
    # but here inputs are 'topic-NAME.md'.
    target_base = topic_name.replace(".md", "")
    
    # Try primary root
    for root, _, files in os.walk(SOURCE_CYPHER_ROOT):
        for file in files:
            if file.endswith(topic_name):
                return os.path.join(root, file)

    # Try secondary root
    # Secondary files end in .cypher not .md
    # target_cypher = topic_name.replace(".md", ".cypher")
    # for root, _, files in os.walk(SECONDARY_CYPHER_ROOT):
    #     for file in files:
    #         if file == target_cypher:
    #              return os.path.join(root, file)
            
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

def extract_parent_from_cypher(cypher_block):
    """Extracts parent field from CREATE statement."""
    # Look for parent: "value" or parent: null
    match = re.search(r'parent:\s*(".*?"|null)', cypher_block)
    if match:
        val = match.group(1)
        if val == 'null':
            return "null" # Return string "null" to be unquoted in YAML? or None?
                          # User wrote parent: "null" in their manual edit, so let's stick to string "null" or unquoted null.
                          # YAML `parent: null` is None. `parent: "null"` is string "null".
                          # The Cypher has `parent: null` (unquoted null keyword) usually for root.
                          # Or `parent: "topic.THE GODHEAD"`.
        return val.strip('"') 
    return None

def process_file(filename):
    dest_path = os.path.join(DEST_MARKDOWN_ROOT, filename)
    if not os.path.exists(dest_path):
        return

    print(f"Processing {filename}...")
    
    with open(dest_path, 'r') as f:
        content = f.read()

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    
    if len(parts) >= 3:
        frontmatter_raw = parts[1]
    else:
        print(f"Skipping {filename}: Invalid frontmatter.")
        return

    # Find Cypher source
    cypher_path = find_cypher_file(filename)
    cypher_block = ""
    parent_val = None

    if cypher_path:
        cypher_block = extract_cypher_block(cypher_path)
        if cypher_block:
            parent_val = extract_parent_from_cypher(cypher_block)
    else:
        print(f"Warning: No source found for {filename}")
        # We proceed to just clean frontmatter if user wants, BUT 
        # the user's prompt implies merging. If we can't merge, maybe we shouldn't touch it?
        # "Can you do this with all the markdown... that correspond to the same nodes"
        # If no correspondence, maybe skip?
        # Only preserve if we have source?
        # Let's clean frontmatter regardless, as requested "remove title...".
        pass

    try:
        fm = yaml.safe_load(frontmatter_raw)
        if not isinstance(fm, dict):
            return

        # Remove fields
        for field in FIELDS_TO_REMOVE:
            if field in fm:
                del fm[field]
        
        # Add parent IF found
        if parent_val:
            fm['parent'] = parent_val
        elif 'parent' not in fm and filename == "topic-NULL.md":
             # Special case for NULL TOPIC if we didn't confirm extraction
             pass 

        new_frontmatter = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()
    except yaml.YAMLError as e:
        print(f"Skipping {filename}: YAML error {e}")
        return

    # If we found a cypher block, append it. If not, preserve existing body?
    # The previous script completely replaced body with cypher block.
    # If we don't have a cypher block, we probably shouldn't destroy the existing body 
    # if it contained valid content.
    # BUT, the goal is to "store the cypher queries".
    # If we didn't find one, we can't store it.
    
    if cypher_block:
        new_content = f"---\n{new_frontmatter}\n---\n{cypher_block}\n"
        with open(dest_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Just update frontmatter?
        # Parsing body again to preserve it is tricky if we don't use the original one.
        # body = parts[2]
        # new_content = f"---\n{new_frontmatter}\n---\n{body}"
        # with open(dest_path, 'w') as f:
            # f.write(new_content)
        # print(f"Updated {filename} (Frontmatter only)")
        print(f"Skipped content update for {filename} (No Cypher found)")

def main():
    for filename in os.listdir(DEST_MARKDOWN_ROOT):
        if filename.startswith("topic-") and filename.endswith(".md"):
            process_file(filename)

if __name__ == "__main__":
    main()
