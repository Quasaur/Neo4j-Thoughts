from neo4j import GraphDatabase
from pathlib import Path
import re

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

UNINSERTED_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS/UnInserted")
THOUGHTS_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/content/THOUGHTS")

def extract_thought_name_from_file(md_file: Path) -> str:
    """Extract thought name from markdown filename"""
    # Convert filename to thought name format
    # A-GREAT-DAY.md -> A_GREAT_DAY or A GREAT DAY
    name = md_file.stem.replace('-', '_')
    return name

def query_thought_from_db(driver, thought_name: str):
    """Query Neo4j for thought and its content"""
    with driver.session() as session:
        # Try different name variations
        variations = [
            f"thought.{thought_name}",
            f"thought.{thought_name.replace('_', '-')}",
            f"thought.{thought_name.replace('_', ' ')}",
        ]
        
        for name_variant in variations:
            result = session.run("""
                MATCH (t:THOUGHT)-[:HAS_CONTENT]->(c:CONTENT)
                WHERE t.name = $name
                RETURN t, c
            """, name=name_variant)
            
            record = result.single()
            if record:
                return record["t"], record["c"], name_variant
    
    return None, None, None

def create_obsidian_cypher_content(thought_node, content_node, thought_name):
    """Generate the Cypher block content"""
    
    # Extract properties
    tags = thought_node.get("tags", [])
    level = thought_node.get("level", 1)
    parent = thought_node.get("parent", "")
    alias = thought_node.get("alias", "")
    
    # Build THOUGHT CREATE statement
    tags_str = '", "'.join(tags)
    thought_create = f'''CREATE (t:THOUGHT {{
    name: "{thought_name}",
    alias: "{alias}",
    parent: "{parent}",
    tags: ["{tags_str}"],
    level: {level}
}});'''
    
    # Build CONTENT CREATE statement
    content_fields = []
    content_fields.append(f'    name: "{content_node["name"]}"')
    
    for lang in ['en', 'es', 'fr', 'hi', 'zh']:
        title_key = f"{lang}_title"
        content_key = f"{lang}_content"
        
        if title_key in content_node:
            title = content_node[title_key].replace('"', '\\"')
            content_fields.append(f'    {title_key}: "{title}"')
        
        if content_key in content_node:
            content = content_node[content_key].replace('"', '\\"')
            content_fields.append(f'    {content_key}: "{content}"')
    
    content_create = "CREATE (c:CONTENT {\n" + ",\n".join(content_fields) + "\n});"
    
    # Build relationship statements
    thought_base = thought_name.split('.')[-1]
    parent_name = parent.split('.')[-1] if parent else ""
    
    has_content = f'''MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "{thought_name}" AND c.name = "{content_node["name"]}"
MERGE (t)-[:HAS_CONTENT {{name: "edge.{thought_base}"}}]->(c);'''
    
    has_thought = f'''MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "{parent}" AND child.name = "{thought_name}"
MERGE (parent)-[:HAS_THOUGHT {{name: "edge.{parent_name}->{thought_base}"}}]->(child);'''
    
    return f"{thought_create}\n\n{content_create}\n\n{has_content}\n\n{has_thought}"

def update_markdown_file(md_file: Path, thought_node, content_node, thought_name):
    """Update markdown file with complete Obsidian-Cypher format"""
    
    # Read existing file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        print(f"  ⚠️  No frontmatter found in {md_file.name}")
        return False
    
    frontmatter = frontmatter_match.group(1)
    
    # Update frontmatter properties
    frontmatter_lines = []
    has_inserted = False
    
    for line in frontmatter.split('\n'):
        # Update name to match database
        if line.startswith('name:'):
            frontmatter_lines.append(f'name: "{thought_name}"')
        elif line.startswith('inserted:'):
            frontmatter_lines.append('inserted: true')
            has_inserted = True
        elif line.startswith('level:'):
            frontmatter_lines.append(f'level: {thought_node.get("level", 1)}')
        else:
            frontmatter_lines.append(line)
    
    if not has_inserted:
        frontmatter_lines.append('inserted: true')
    
    # Generate Cypher block
    cypher_content = create_obsidian_cypher_content(thought_node, content_node, thought_name)
    
    # Construct new file content
    new_content = f"---\n{chr(10).join(frontmatter_lines)}\n---\n\n```Cypher\n{cypher_content}\n```\n"
    
    # Write updated content
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("Checking UnInserted files against Neo4j AuraDB...\n")
    
    # Get all markdown files in UnInserted
    md_files = list(UNINSERTED_DIR.glob("*.md"))
    print(f"Found {len(md_files)} files in UnInserted folder\n")
    
    found_count = 0
    updated_count = 0
    moved_count = 0
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        for md_file in md_files:
            thought_name = extract_thought_name_from_file(md_file)
            
            # Query database
            thought_node, content_node, actual_name = query_thought_from_db(driver, thought_name)
            
            if thought_node and content_node:
                found_count += 1
                print(f"✅ Found in DB: {md_file.name} -> {actual_name}")
                
                # Update file
                if update_markdown_file(md_file, thought_node, content_node, actual_name):
                    updated_count += 1
                    print(f"   Updated with complete content")
                    
                    # Move to main THOUGHTS folder
                    destination = THOUGHTS_DIR / md_file.name
                    md_file.rename(destination)
                    moved_count += 1
                    print(f"   Moved to {destination.relative_to(THOUGHTS_DIR.parent)}\n")
                else:
                    print(f"   ⚠️  Failed to update\n")
            else:
                print(f"❌ Not in DB: {md_file.name}")
    
    print("\n" + "="*60)
    print(f"Summary:")
    print(f"  Files checked: {len(md_files)}")
    print(f"  Found in DB: {found_count}")
    print(f"  Updated: {updated_count}")
    print(f"  Moved to THOUGHTS: {moved_count}")
    print("="*60)

if __name__ == "__main__":
    main()
