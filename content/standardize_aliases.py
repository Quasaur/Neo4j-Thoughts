import os
import re
import yaml

TARGET_DIRS = [
    "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/TOPICS",
    "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/QUOTES"
]

# Custom representer for quoted strings to maintain style
class QuotedString(str):
    pass

def quoted_scalar_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

yaml.add_representer(QuotedString, quoted_scalar_representer)

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return # Skip invalid files

    fm_raw = parts[1]
    body = parts[2]

    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict): return
    except Exception:
        return

    changed = False
    
    if 'aliases' in fm:
        aliases_val = fm['aliases']
        
        if 'alias' in fm:
            # Delete aliases if alias exists
            del fm['aliases']
            print(f"Deleted 'aliases' (kept 'alias') in {os.path.basename(file_path)}")
            changed = True
        else:
            # Convert aliases to alias
            new_val = None
            if isinstance(aliases_val, list):
                if len(aliases_val) > 0:
                    new_val = aliases_val[0]
            elif isinstance(aliases_val, str):
                new_val = aliases_val
            
            if new_val:
                fm['alias'] = new_val
                # Remove aliases
                del fm['aliases']
                print(f"Converted 'aliases' -> 'alias': '{new_val}' in {os.path.basename(file_path)}")
                changed = True
            else:
                # Aliases was empty list or None, just remove it?
                # User said "convert... or delete". 
                # If aliases is empty and no alias, we effectively just delete aliases.
                del fm['aliases']
                print(f"Deleted empty 'aliases' in {os.path.basename(file_path)}")
                changed = True

    if changed:
        # Re-apply quoting logic
        final_fm = {}
        for k, v in fm.items():
            if isinstance(v, str) and ' ' in v:
                final_fm[k] = QuotedString(v)
            else:
                final_fm[k] = v
        
        new_fm_str = yaml.dump(final_fm, sort_keys=False, allow_unicode=True).strip()
        new_content = f"---\n{new_fm_str}\n---\n{body}"
        
        with open(file_path, 'w') as f:
            f.write(new_content)

def main():
    for target_dir in TARGET_DIRS:
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(".md"):
                    process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
