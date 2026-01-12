#!/usr/bin/env python3
"""
Translate all markdown files in Book_of_Tweets/cypher/ that are missing proper translations.
"""

import os
import re
from pathlib import Path

# Files that already have complete translations
COMPLETE_FILES = {
    "ACCOUNTABILITY.md", "AGREEING-WITH-OPPRESSOR.md", "ALIGNING-THROUGH-PRAYER.md",
    "ALL-TRUTH-GODS.md", "ALONZO-CHURCH-FAITH.md", "AMERICA-ACCOUNTABLE-FREEDOMS.md",
    "AMERICAN-POVERTY-LINE.md", "ANGER-AND-PAIN.md", "ANGER-AS-CONTAGION.md",
    "APOCALYPSE-BETTER-WORLD.md", "APOSTLES-AS-VISION.md", "ARROGANCE-VS-DIGNITY.md",
    "ASK-GOD-PERFECTION.md", "ATROCITIES-OF-RELIGION.md", "ATTENTIONS-DESIRE.md",
    "AWESOME-GOD.md", "DEFINITION-OF-SIN.md", "DUST-AND-DIVINE.md",
    "FRIENDS-AND-ENEMIES.md", "GOD-AND-EVIL.md", "JESUS-IN-DISGUISE.md",
    "LIFE-AS-DREAM.md", "SUBMITTING-OUR-PLANS.md", "ABORTION-AND-GOLDEN-RULE.md",
    "ACCURATE-THEOLOGY.md", "ALL-OF-GOD-JESUS.md", "ALL-THINGS-FOR-HIM.md"
}

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")


def extract_content_section(file_content):
    """Extract the CONTENT node section from a Cypher file."""
    match = re.search(r'CREATE \(c:CONTENT \{([^}]+)\}\);', file_content, re.DOTALL)
    if match:
        return match.group(0), match.group(1)
    return None, None


def parse_content_fields(content_str):
    """Parse the fields from the CONTENT node."""
    fields = {}
    
    # Match name
    name_match = re.search(r'name:\s*"([^"]*)"', content_str)
    if name_match:
        fields['name'] = name_match.group(1)
    
    # Match en_title and en_content
    en_title_match = re.search(r'en_title:\s*"([^"]*)"', content_str)
    en_content_match = re.search(r'en_content:\s*"([^"]*)"', content_str)
    
    if en_title_match:
        fields['en_title'] = en_title_match.group(1)
    if en_content_match:
        fields['en_content'] = en_content_match.group(1)
    
    return fields


def generate_translations(en_title, en_content):
    """
    Generate translations for Spanish, French, Hindi, and Chinese.
    This is a placeholder - actual translations need proper context.
    """
    # Note: These are basic translations. For production, use proper translation API
    # or manual translation by native speakers for theological content.
    
    translations = {
        'es_title': en_title,  # Placeholder
        'es_content': en_content,  # Placeholder
        'fr_title': en_title,  # Placeholder
        'fr_content': en_content,  # Placeholder
        'hi_title': en_title,  # Placeholder
        'hi_content': en_content,  # Placeholder
        'zh_title': f"Pīnyīn for {en_title}",  # Placeholder
        'zh_content': f"Pīnyīn for {en_content}"  # Placeholder
    }
    
    return translations


def create_content_node(name, en_title, en_content, translations):
    """Create the properly formatted CONTENT node with all translations."""
    return f'''CREATE (c:CONTENT {{
    name: "{name}",
    en_title: "{en_title}",
    en_content: "{en_content}",
    es_title: "{translations['es_title']}",
    es_content: "{translations['es_content']}",
    fr_title: "{translations['fr_title']}",
    fr_content: "{translations['fr_content']}",
    hi_title: "{translations['hi_title']}",
    hi_content: "{translations['hi_content']}",
    zh_title: "{translations['zh_title']}",
    zh_content: "{translations['zh_content']}"
}});'''


def process_file(file_path):
    """Process a single markdown file."""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract and parse CONTENT section
    old_content_node, content_fields_str = extract_content_section(content)
    
    if not old_content_node:
        print(f"  ⚠️  Could not find CONTENT node in {file_path.name}")
        return False
    
    fields = parse_content_fields(content_fields_str)
    
    if 'en_title' not in fields or 'en_content' not in fields:
        print(f"  ⚠️  Missing en_title or en_content in {file_path.name}")
        return False
    
    # Generate translations (this will need actual translation logic)
    translations = generate_translations(fields['en_title'], fields['en_content'])
    
    # Create new CONTENT node
    new_content_node = create_content_node(
        fields['name'],
        fields['en_title'],
        fields['en_content'],
        translations
    )
    
    # Replace in file
    new_content = content.replace(old_content_node, new_content_node)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✅ Updated {file_path.name}")
    return True


def main():
    """Main processing function."""
    print("Starting translation processing...")
    print(f"Directory: {CYPHER_DIR}")
    
    # Get all .md files
    all_files = list(CYPHER_DIR.glob("*.md"))
    print(f"Total files found: {len(all_files)}")
    
    # Filter out complete files
    files_to_process = [f for f in all_files if f.name not in COMPLETE_FILES]
    print(f"Files to process: {len(files_to_process)}")
    print(f"Files skipped (already complete): {len(COMPLETE_FILES)}")
    
    # Process each file
    processed = 0
    failed = 0
    
    for file_path in files_to_process:
        try:
            if process_file(file_path):
                processed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ❌ Error processing {file_path.name}: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Processing complete!")
    print(f"Successfully processed: {processed}")
    print(f"Failed: {failed}")
    print(f"Total: {processed + failed}")
    print("="*60)


if __name__ == "__main__":
    main()
