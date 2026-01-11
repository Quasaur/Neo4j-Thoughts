#!/usr/bin/env python3
"""
Update Neo4j AuraDB with Correct Translations
This script connects to the AuraDB instance and updates CONTENT nodes
with the correct translations from our batch_1_translations.json file.
"""

import json
from neo4j import GraphDatabase

# Neo4j AuraDB connection details
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


class Neo4jUpdater:
    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)
    
    def close(self):
        self.driver.close()
    
    def update_content_translations(self, thought_name, translations):
        """Update a CONTENT node with new translations."""
        query = """
        MATCH (c:CONTENT)
        WHERE c.name = $content_name
        SET c.es_title = $es_title,
            c.es_content = $es_content,
            c.fr_title = $fr_title,
            c.fr_content = $fr_content,
            c.hi_title = $hi_title,
            c.hi_content = $hi_content,
            c.zh_title = $zh_title,
            c.zh_content = $zh_content
        RETURN c.name as updated
        """
        
        with self.driver.session() as session:
            result = session.run(
                query,
                content_name=thought_name.replace("thought.", "content."),
                es_title=translations['es_title'],
                es_content=translations['es_content'],
                fr_title=translations['fr_title'],
                fr_content=translations['fr_content'],
                hi_title=translations['hi_title'],
                hi_content=translations['hi_content'],
                zh_title=translations['zh_title'],
                zh_content=translations['zh_content']
            )
            record = result.single()
            return record is not None
    
    def check_content_exists(self, thought_name):
        """Check if a CONTENT node exists for the given thought."""
        query = """
        MATCH (c:CONTENT)
        WHERE c.name = $content_name
        RETURN c.name as name, 
               c.en_title as en_title,
               c.es_title as es_title
        """
        
        with self.driver.session() as session:
            result = session.run(
                query,
                content_name=thought_name.replace("thought.", "content.")
            )
            record = result.single()
            return record


def extract_thought_name_from_file(file_path):
    """Extract the thought name from the file path."""
    # Parse from file path: ABORTION-AND-GOLDEN-RULE.md -> thought.ABORTION AND GOLDEN RULE
    filename = file_path.split('/')[-1].replace('.md', '')
    thought_name = "thought." + filename.replace('-', ' ')
    return thought_name


def main():
    """Main update process."""
    # Load translations
    translations_file = "/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/python/batch_1_translations.json"
    with open(translations_file, 'r', encoding='utf-8') as f:
        batch = json.load(f)
    
    print("Connecting to Neo4j AuraDB...")
    updater = Neo4jUpdater(URI, AUTH)
    
    try:
        print(f"Processing {len(batch)} translations...\n")
        
        success = 0
        not_found = 0
        failed = 0
        
        for idx, item in enumerate(batch, 1):
            thought_name = extract_thought_name_from_file(item['file'])
            
            # Check if content exists
            existing = updater.check_content_exists(thought_name)
            
            if not existing:
                print(f"[{idx}/{len(batch)}] ⚠️  NOT FOUND: {thought_name}")
                not_found += 1
                continue
            
            # Show current state
            current_es = existing['es_title'] if existing else 'N/A'
            print(f"[{idx}/{len(batch)}] {item['name']}")
            print(f"  Current ES: {current_es}")
            print(f"  New ES:     {item['translations']['es_title']}")
            
            # Update translations
            if updater.update_content_translations(thought_name, item['translations']):
                print(f"  ✅ Updated successfully")
                success += 1
            else:
                print(f"  ❌ Update failed")
                failed += 1
            
            print()
        
        print("=" * 60)
        print(f"Summary:")
        print(f"  Successfully updated: {success}")
        print(f"  Not found in DB:      {not_found}")
        print(f"  Failed to update:     {failed}")
        print("=" * 60)
        
    finally:
        updater.close()
        print("\nConnection closed.")


if __name__ == "__main__":
    main()
