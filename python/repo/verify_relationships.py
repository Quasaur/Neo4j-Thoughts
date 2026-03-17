#!/usr/bin/env python3
"""
Verify that all relationships for the 13 synced thoughts are intact in Neo4j.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# The 13 thoughts we synced with their expected parent topics
THOUGHTS = [
    {"thought": "thought.DEATH_ROW", "parent": "topic.THE-GOSPEL"},
    {"thought": "thought.DIVINE_WORTH", "parent": "topic.HOLINESS"},
    {"thought": "thought.UNFAIR", "parent": "topic.DIVINE-SOVEREIGNTY"},
    {"thought": "thought.QUIET_THE_FLESH", "parent": "topic.SANCTIFICATION"},
    {"thought": "thought.SELF_DENIAL", "parent": "topic.SANCTIFICATION"},
    {"thought": "thought.REACTION", "parent": "topic.SANCTIFICATION"},
    {"thought": "thought.FIRST_RULE", "parent": "topic.HUMOR"},
    {"thought": "thought.THE_IRC", "parent": "topic.HUMOR"},
    {"thought": "thought.ANOTHER_SINNER", "parent": "topic.EVANGELISM"},
    {"thought": "thought.FORBIDDEN", "parent": "topic.SIN"},
    {"thought": "thought.INSATIABLE", "parent": "topic.SIN"},
    {"thought": "thought.SHOCKED", "parent": "topic.SIN"},
    {"thought": "thought.THE_END_OF_EVIL", "parent": "topic.PROPHECY"},
]

def verify_relationships():
    """Verify all relationships for the synced thoughts."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    print("=" * 80)
    print("VERIFICATION: Checking Relationships for 13 Synced Thoughts")
    print("=" * 80)
    print()
    
    issues = []
    
    try:
        with driver.session() as session:
            for item in THOUGHTS:
                thought_name = item['thought']
                parent_name = item['parent']
                content_name = thought_name.replace('thought.', 'content.')
                
                print(f"🔍 {thought_name}")
                
                # Check HAS_CONTENT relationship
                query_content = """
                MATCH (t:THOUGHT {name: $thought_name})-[r:HAS_CONTENT]->(c:CONTENT {name: $content_name})
                RETURN r.name as rel_name, c.name as content_name
                """
                
                result = session.run(query_content, thought_name=thought_name, content_name=content_name)
                record = result.single()
                
                if not record:
                    print(f"  ❌ HAS_CONTENT relationship missing!")
                    issues.append({
                        'thought': thought_name,
                        'issue': 'Missing HAS_CONTENT relationship'
                    })
                else:
                    rel_name = record['rel_name']
                    print(f"  ✅ HAS_CONTENT → {content_name}")
                    if rel_name:
                        print(f"     Relationship name: {rel_name}")
                
                # Check HAS_THOUGHT relationship from parent
                query_parent = """
                MATCH (parent:TOPIC {name: $parent_name})-[r:HAS_THOUGHT]->(t:THOUGHT {name: $thought_name})
                RETURN r.name as rel_name, parent.name as parent_name
                """
                
                result = session.run(query_parent, parent_name=parent_name, thought_name=thought_name)
                record = result.single()
                
                if not record:
                    print(f"  ❌ HAS_THOUGHT relationship from {parent_name} missing!")
                    issues.append({
                        'thought': thought_name,
                        'issue': f'Missing HAS_THOUGHT relationship from {parent_name}'
                    })
                else:
                    rel_name = record['rel_name']
                    print(f"  ✅ {parent_name} -[HAS_THOUGHT]→ {thought_name}")
                    if rel_name:
                        print(f"     Relationship name: {rel_name}")
                
                print()
        
        # Summary
        print("=" * 80)
        print("RELATIONSHIP VERIFICATION SUMMARY")
        print("=" * 80)
        print(f"Thoughts verified: {len(THOUGHTS)}")
        print(f"Expected relationships: {len(THOUGHTS) * 2} (HAS_CONTENT + HAS_THOUGHT)")
        print(f"Issues found: {len(issues)}")
        
        if issues:
            print("\n❌ RELATIONSHIP ISSUES:")
            for issue in issues:
                print(f"  {issue['thought']}")
                print(f"    {issue['issue']}")
        else:
            print("\n✅ All relationships verified intact!")
            print("   - All HAS_CONTENT relationships present")
            print("   - All HAS_THOUGHT relationships from parent topics present")
        
        print("=" * 80)
        
    finally:
        driver.close()
    
    return issues

if __name__ == '__main__':
    verify_relationships()
