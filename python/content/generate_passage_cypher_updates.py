#!/usr/bin/env python3
"""
Generate Cypher UPDATE queries for PASSAGE translations.
Reads the translations JSON and generates UPDATE statements for Neo4j.
"""

import json
from pathlib import Path

def generate_cypher_updates():
    """Generate Cypher UPDATE queries from translations JSON."""
    
    # Read translations
    translations_file = Path("ANALYSIS/passage_translations.json")
    
    if not translations_file.exists():
        print(f"❌ Translations file not found: {translations_file}")
        return
    
    with open(translations_file, 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    # Generate Cypher file
    cypher_file = Path("CYPHER/UPDATES/passage_translations_update.cypher")
    cypher_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(cypher_file, 'w', encoding='utf-8') as f:
        f.write("// Cypher UPDATE queries to add missing translations to PASSAGE CONTENT nodes\n")
        f.write("// Generated automatically from passage_translations.json\n")
        f.write(f"// Total updates: {len(results)}\n\n")
        
        for i, result in enumerate(results, 1):
            passage_name = result['passage_name']
            translations = result['translations']
            
            # Extract content name from passage name
            content_name = passage_name.replace('passage.', 'content.')
            
            f.write(f"// Update {i}/{len(results)}: {passage_name}\n")
            f.write(f"MATCH (c:CONTENT {{name: \"{content_name}\"}})\n")
            f.write("SET\n")
            
            # Build SET clauses
            set_clauses = []
            for key in ['es_title', 'es_content', 'fr_title', 'fr_content',
                       'hi_title', 'hi_content', 'zh_title', 'zh_content']:
                if key in translations:
                    # Escape quotes and backslashes for Cypher
                    value = translations[key].replace('\\', '\\\\').replace('"', '\\"')
                    set_clauses.append(f'    c.{key} = "{value}"')
            
            f.write(',\n'.join(set_clauses))
            f.write('\n')
            f.write(f"RETURN c.name as updated;\n\n")
        
        # Add verification query at the end
        f.write("// Verification: Check all PASSAGE CONTENT nodes have complete translations\n")
        f.write("MATCH (p:PASSAGE)-[:HAS_CONTENT]->(c:CONTENT)\n")
        f.write("WHERE c.es_title IS NULL OR c.es_content IS NULL OR\n")
        f.write("      c.fr_title IS NULL OR c.fr_content IS NULL OR\n")
        f.write("      c.hi_title IS NULL OR c.hi_content IS NULL OR\n")
        f.write("      c.zh_title IS NULL OR c.zh_content IS NULL\n")
        f.write("RETURN p.name as passage_name, c.name as content_name,\n")
        f.write("       c.es_title IS NULL as missing_es,\n")
        f.write("       c.fr_title IS NULL as missing_fr,\n")
        f.write("       c.hi_title IS NULL as missing_hi,\n")
        f.write("       c.zh_title IS NULL as missing_zh;\n")
        f.write("// Should return 0 rows if all translations are complete\n")
    
    print(f"✅ Generated Cypher UPDATE queries: {cypher_file}")
    print(f"   Total updates: {len(results)}")
    
    return cypher_file


if __name__ == "__main__":
    generate_cypher_updates()
