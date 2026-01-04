import os
import re

SOURCE_ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/DATA/THOUGHTS"
TARGET_ROOT = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS"

def build_target_index(root_dir):
    """Builds a set of all filenames in the target directory."""
    index = set()
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                index.add(file)
    return index

def normalize_source_name(filename):
    """
    Normalizes a source filename to match target format.
    Example: '0004-thought-IMPERSONAL-GOD.md' -> 'IMPERSONAL-GOD.md'
    """
    # Remove leading 4 digits and dash
    name = re.sub(r'^\d{4}-', '', filename)
    # Remove 'thought-' prefix
    name = re.sub(r'^thought-', '', name)
    return name

def check_variations(normalized_name, target_index):
    """Checks for the name or variations in the target index."""
    if normalized_name in target_index:
        return True
    
    # Check for (2) vs 2
    base = normalized_name.replace(".md", "")
    
    # Case: Source 'NAME (2).md' -> Target 'NAME2.md'
    if base.endswith(" (2)"):
        var1 = base.replace(" (2)", "2") + ".md"
        if var1 in target_index: return True
        
    # Case: Source 'NAME2.md' -> Target 'NAME (2).md' or 'NAME2.md' (already checked)
    
    return False

def main():
    target_index = build_target_index(TARGET_ROOT)
    print(f"Index built with {len(target_index)} target files.")
    
    deleted_count = 0
    kept_count = 0
    
    for root, _, files in os.walk(SOURCE_ROOT):
        for file in files:
            if not file.endswith(".md"):
                continue
                
            path = os.path.join(root, file)
            normalized = normalize_source_name(file)
            
            if check_variations(normalized, target_index):
                try:
                    os.remove(path)
                    print(f"[DELETED] Verified duplicate: {file} -> {normalized}")
                    deleted_count += 1
                except OSError as e:
                    print(f"Error deleting {path}: {e}")
            else:
                print(f"[KEPT] No match found: {file} (Normalized: {normalized})")
                kept_count += 1

    print("-" * 30)
    print(f"Cleanup Complete.")
    print(f"Deleted: {deleted_count}")
    print(f"Kept: {kept_count}")
    
    # Remove empty directories
    print("Removing empty directories...")
    for root, dirs, files in os.walk(SOURCE_ROOT, topdown=False):
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError:
                pass # Directory not empty

if __name__ == "__main__":
    main()
