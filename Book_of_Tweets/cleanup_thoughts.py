import os
import re

CYPHER_DIR = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher"

def cleanup_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by the frontmatter markers ---
    parts = re.split(r'^---\s*$', content, flags=re.MULTILINE)
    
    if len(parts) < 3:
        return False # Not a standard frontmatter file

    frontmatter = parts[1].strip()
    rest = parts[2].strip()

    # Find the start of the Cypher block
    cypher_match = re.search(r'```Cypher', rest, flags=re.IGNORECASE)
    if not cypher_match:
        return False

    cypher_block = rest[cypher_match.start():].strip()

    # Construct new content
    new_content = f"---\n{frontmatter}\n---\n\n{cypher_block}\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    files = [f for f in os.listdir(CYPHER_DIR) if f.endswith(".md")]
    count = 0
    for filename in files:
        filepath = os.path.join(CYPHER_DIR, filename)
        if cleanup_file(filepath):
            count += 1
    print(f"Cleaned up {count} files.")

if __name__ == "__main__":
    main()
