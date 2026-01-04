import os
import re

directory = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if it's a THOUGHT file
    if "type: THOUGHT" not in content:
        return False

    # Skip if en_content already in frontmatter (simple check)
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        return False
    
    frontmatter = frontmatter_match.group(1)
    if "en_content:" in frontmatter:
        return False

    # Extract en_content from Cypher block
    # Looking for: en_content: "..." or en_content: "..."
    # The value might have escaped quotes \"
    cypher_match = re.search(r'en_content:\s*"(.*?)"\s*,?\n', content)
    if not cypher_match:
        # Try again with a more flexible regex if needed, or log failure
        print(f"Warning: Could not find en_content in Cypher block for {filepath}")
        return False

    en_content_value = cypher_match.group(1)
    
    # Simple check for line numbers if present (from my previous tool output, but files themselves shouldn't have them)
    # The user instruction says "Add the en_content field to the YAML front matter WITHOUT removing it from the Cypher block"
    
    # Prepare the new frontmatter line
    new_line = f'en_content: "{en_content_value}"\n'
    
    # Insert it before 'parent:'
    updated_frontmatter = frontmatter.replace('parent:', f'{new_line}parent:')
    
    # Update the file content
    new_content = content.replace(frontmatter, updated_frontmatter)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        if update_file(os.path.join(directory, filename)):
            count += 1

print(f"Updated {count} files.")
