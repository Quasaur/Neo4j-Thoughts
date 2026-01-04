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

    # Check if 'level' exists
    if 'level' in fm:
        level_val = fm.pop('level')
        
        # Reconstruct dict to enforce order: existing keys... then level
        # Since Python 3.7+, dict usage preserves insertion order.
        # We popped 'level', so just adding it back puts it at the end.
        fm['level'] = level_val
        
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
        print(f"Reordered 'level' to last in {os.path.basename(file_path)}")

def main():
    for target_dir in TARGET_DIRS:
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(".md"):
                    process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
