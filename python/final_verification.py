#!/usr/bin/env python3
"""
Final comprehensive verification of all 13 synced thoughts and their relationships.
Uses the ACTUAL parent topic names from the database.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# The 13 thoughts with ACTUAL parent names (as they exist in Neo4j)
THOUGHTS = [
    {"thought": "thought.DEATH_ROW", "expected_parent": "topic.THE GOSPEL"},
    {"thought": "thought.DIVINE_WORTH", "expected_parent": "topic.HOLINESS"},
    {"thought": "thought.UNFAIR", "expected_parent": "topic.DIVINE SOVEREIGNTY"},
    {"thought": "thought.QUIET_THE_FLESH", "expected_parent": "topic.GRACE"},
    {"thought": "thought.SELF_DENIAL", "expected_parent": "topic.ATTITUDE"},
    {"thought": "thought.REACTION", "expected_parent": "topic.PSYCHOLOGY"},
    {"thought": "thought.FIRST_RULE", "expected_parent": "topic.HUMOR"},
    {"thought": "thought.THE_IRC", "expected_parent": "topic.FIN-GOV"},
    {"thought": "thought.ANOTHER_SINNER", "expected_parent": "topic.EVIL"},
    {"thought": "thought.FORBIDDEN", "expected_parent": "topic.EVIL"},
    {"thought": "thought.INSATIABLE", "expected_parent": "topic.EVIL"},
    {"thought": "thought.SHOCKED", "expected_parent": "topic.EVIL"},
    {"thought": "thought.THE_END_OF_EVIL", "expected_parent": "topic.EVIL"},
]

def verify_all_relationships():
    """Verify all relationships for the 13 synced thoughts."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    print("=" * 80)
    print("FINAL VERIFICATION: All 13 Synced Thoughts")
    print("=" * 80)
    print()
    
    issues = []
    
    try:
        with driver.session() as session:
            for item in THOUGHTS:
                thought_name = item['thought']
                expected_parent = item['expected_parent']
                content_name = thought_name.replace('thought.', 'content.')
                
                # Get full details for this thought
                query = """
                MATCH (t:THOUGHT {name: $thought_name})
                OPTIONAL MATCH (t)-[has_content:HAS_CONTENT]->(c:CONTENT)
                OPTIONAL MATCH (parent:TOPIC)-[has_thought:HAS_THOUGHT]->(t)
                RETURN 
                    t.alias as thought_alias,
                    c.name as content_name,
                    c.en_content as en_content,
                    parent.name as actual_parent,
                    parent.alias as parent_alias
                """
                
                result = session.run(query, thought_name=thought_name)
                record = result.single()
                
                if not record:
                    print(f"❌ {thought_name}: NOT FOUND")
                    issues.append({'thought': thought_name, 'issue': 'Not found'})
                    continue
                
                thought_alias = record['thought_alias']
                content_name_actual = record['content_name']
                actual_parent = record['actual_parent']
                parent_alias = record['parent_alias']
                en_content = record['en_content'] or ""
                
                print(f"📄 {thought_alias}")
                
                # Check for multilingual markers
                has_markers = any(marker in en_content for marker in ['[!Thought-en]', '[!Pensamiento-es]', '[!Pensée-fr]'])
                
                if has_markers:
                    print(f"  ❌ Content contains multilingual markers!")
                    issues.append({'thought': thought_name, 'issue': 'Multilingual markers found'})
                else:
                    print(f"  ✅ Content clean (no markers)")
                
                # Check HAS_CONTENT relationship
                if content_name_actual:
                    print(f"  ✅ HAS_CONTENT → {content_name_actual}")
                else:
                    print(f"  ❌ Missing HAS_CONTENT relationship")
                    issues.append({'thought': thought_name, 'issue': 'Missing HAS_CONTENT'})
                
                # Check HAS_THOUGHT relationship
                if actual_parent:
                    if actual_parent == expected_parent:
                        print(f"  ✅ {actual_parent} -[HAS_THOUGHT]→ {thought_name}")
                        print(f"     Parent: {parent_alias}")
                    else:
                        print(f"  ⚠️  Parent mismatch!")
                        print(f"     Expected: {expected_parent}")
                        print(f"     Actual: {actual_parent}")
                        issues.append({'thought': thought_name, 'issue': f'Parent mismatch: expected {expected_parent}, got {actual_parent}'})
                else:
                    print(f"  ❌ Missing HAS_THOUGHT relationship from {expected_parent}")
                    issues.append({'thought': thought_name, 'issue': f'Missing HAS_THOUGHT from {expected_parent}'})
                
                print()
        
        # Summary
        print("=" * 80)
        print("FINAL VERIFICATION SUMMARY")
        print("=" * 80)
        print(f"Thoughts verified: {len(THOUGHTS)}")
        print(f"Issues found: {len(issues)}")
        
        if issues:
            print("\n❌ ISSUES:")
            for issue in issues:
                print(f"  {issue['thought']}: {issue['issue']}")
        else:
            print("\n✅ PERFECT! All 13 thoughts are fully synced:")
            print("   ✓ All THOUGHT nodes present")
            print("   ✓ All CONTENT nodes present")
            print("   ✓ All HAS_CONTENT relationships intact")
            print("   ✓ All HAS_THOUGHT relationships intact")
            print("   ✓ All content clean (no multilingual markers)")
        
        print("=" * 80)
        
    finally:
        driver.close()
    
    return issues

if __name__ == '__main__':
    verify_all_relationships()
