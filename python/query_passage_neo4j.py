#!/usr/bin/env python3
"""
Query Neo4j AuraDB to check PASSAGE nodes and their translation completeness.
Compare against local markdown files.
"""

from neo4j import GraphDatabase
import json

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


def query_passage_translations():
    """Query Neo4j for all PASSAGE nodes and their CONTENT translations."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Count total PASSAGE nodes
            result = session.run("MATCH (p:PASSAGE) RETURN count(p) as count")
            passage_count = result.single()['count']
            print(f"Total PASSAGE nodes in Neo4j: {passage_count}\n")
            print("=" * 80)
            
            # Get all PASSAGE nodes with their linked CONTENT
            result = session.run("""
                MATCH (p:PASSAGE)-[:HAS_CONTENT]->(c:CONTENT)
                RETURN p.name as passage_name, 
                       p.alias as passage_alias,
                       c.name as content_name,
                       c.en_title as en_title,
                       c.es_title as es_title,
                       c.fr_title as fr_title,
                       c.hi_title as hi_title,
                       c.zh_title as zh_title,
                       c.en_content as en_content,
                       c.es_content as es_content,
                       c.fr_content as fr_content,
                       c.hi_content as hi_content,
                       c.zh_content as zh_content
                ORDER BY p.name
            """)
            
            passages = []
            incomplete_count = 0
            
            for record in result:
                passage_name = record['passage_name']
                
                # Check which translations are missing
                missing_langs = []
                
                if not record['es_title'] or not record['es_content']:
                    missing_langs.append('es')
                if not record['fr_title'] or not record['fr_content']:
                    missing_langs.append('fr')
                if not record['hi_title'] or not record['hi_content']:
                    missing_langs.append('hi')
                if not record['zh_title'] or not record['zh_content']:
                    missing_langs.append('zh')
                
                is_complete = len(missing_langs) == 0
                
                passage_data = {
                    'passage_name': passage_name,
                    'passage_alias': record['passage_alias'],
                    'content_name': record['content_name'],
                    'is_complete': is_complete,
                    'missing_languages': missing_langs,
                    'translations': {
                        'en': bool(record['en_title'] and record['en_content']),
                        'es': bool(record['es_title'] and record['es_content']),
                        'fr': bool(record['fr_title'] and record['fr_content']),
                        'hi': bool(record['hi_title'] and record['hi_content']),
                        'zh': bool(record['zh_title'] and record['zh_content'])
                    }
                }
                
                passages.append(passage_data)
                
                if not is_complete:
                    incomplete_count += 1
                    print(f"\n❌ INCOMPLETE: {passage_name}")
                    print(f"   Alias: {record['passage_alias']}")
                    print(f"   Missing languages: {', '.join(missing_langs)}")
                    
                    # Show sample of what's missing
                    for lang in missing_langs:
                        title_key = f"{lang}_title"
                        content_key = f"{lang}_content"
                        title_val = record[title_key]
                        content_val = record[content_key]
                        
                        if not title_val and not content_val:
                            print(f"   {lang}: Both title and content missing")
                        elif not title_val:
                            print(f"   {lang}: Title missing")
                        elif not content_val:
                            print(f"   {lang}: Content missing")
            
            print("\n" + "=" * 80)
            print(f"\nSUMMARY:")
            print(f"  Total PASSAGE nodes: {len(passages)}")
            print(f"  Complete: {len(passages) - incomplete_count}")
            print(f"  Incomplete: {incomplete_count}")
            
            if incomplete_count > 0:
                print(f"\n⚠️  {incomplete_count} PASSAGE node(s) in Neo4j are missing translations!")
                
                # Group by missing languages
                lang_summary = {}
                for passage in passages:
                    if not passage['is_complete']:
                        for lang in passage['missing_languages']:
                            if lang not in lang_summary:
                                lang_summary[lang] = []
                            lang_summary[lang].append(passage['passage_name'])
                
                print("\nMissing translations by language in Neo4j:")
                for lang in sorted(lang_summary.keys()):
                    print(f"  {lang}: {len(lang_summary[lang])} nodes")
                    for name in lang_summary[lang]:
                        print(f"    - {name}")
            else:
                print("\n✅ All PASSAGE nodes in Neo4j have complete translations!")
            
            # Check for PASSAGE nodes without CONTENT
            print("\n" + "=" * 80)
            print("\nChecking for PASSAGE nodes without CONTENT...")
            result = session.run("""
                MATCH (p:PASSAGE)
                WHERE NOT (p)-[:HAS_CONTENT]->(:CONTENT)
                RETURN p.name as passage_name, p.alias as passage_alias
            """)
            
            orphan_passages = list(result)
            if orphan_passages:
                print(f"\n⚠️  Found {len(orphan_passages)} PASSAGE node(s) without CONTENT:")
                for record in orphan_passages:
                    print(f"  - {record['passage_name']}: {record['passage_alias']}")
            else:
                print("✅ All PASSAGE nodes have CONTENT linked.")
            
            # Save detailed report
            report_data = {
                'total_passages': len(passages),
                'complete': len(passages) - incomplete_count,
                'incomplete': incomplete_count,
                'passages': passages,
                'orphan_passages': [dict(r) for r in orphan_passages]
            }
            
            with open('ANALYSIS/neo4j_passage_report.json', 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n📄 Detailed JSON report saved to: ANALYSIS/neo4j_passage_report.json")
    
    finally:
        driver.close()


if __name__ == '__main__':
    query_passage_translations()
