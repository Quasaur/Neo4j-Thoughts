#!/usr/bin/env python3
"""
Verify that the corrected thoughts in Neo4j don't contain multilingual markers.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# The 13 thoughts we synced
THOUGHT_NAMES = [
    "thought.DEATH_ROW",
    "thought.DIVINE_WORTH",
    "thought.UNFAIR",
    "thought.QUIET_THE_FLESH",
    "thought.SELF_DENIAL",
    "thought.REACTION",
    "thought.FIRST_RULE",
    "thought.THE_IRC",
    "thought.ANOTHER_SINNER",
    "thought.FORBIDDEN",
    "thought.INSATIABLE",
    "thought.SHOCKED",
    "thought.THE_END_OF_EVIL",
]

# Multilingual markers to check for
MARKERS = [
    "[!Thought-en]",
    "[!Pensamiento-es]",
    "[!Pensée-fr]",
    "[!सोचा-hi]",
    "[!思考-zh]",
]

def verify_thoughts():
    """Query Neo4j to verify thoughts don't contain multilingual markers."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    print("=" * 80)
    print("VERIFICATION: Checking for Multilingual Markers in Neo4j")
    print("=" * 80)
    print()
    
    issues_found = []
    
    try:
        with driver.session() as session:
            for thought_name in THOUGHT_NAMES:
                query = """
                MATCH (t:THOUGHT {name: $thought_name})-[:HAS_CONTENT]->(c:CONTENT)
                RETURN t.alias as alias, c.en_title as en_title, c.en_content as en_content
                """
                
                result = session.run(query, thought_name=thought_name)
                record = result.single()
                
                if not record:
                    print(f"❌ {thought_name}: NOT FOUND in Neo4j")
                    issues_found.append({
                        'thought': thought_name,
                        'issue': 'Not found in database'
                    })
                    continue
                
                alias = record['alias']
                en_title = record['en_title'] or ""
                en_content = record['en_content'] or ""
                
                # Check for markers
                found_markers = []
                for marker in MARKERS:
                    if marker in en_content or marker in en_title:
                        found_markers.append(marker)
                
                if found_markers:
                    print(f"❌ {alias}")
                    print(f"   Found markers: {', '.join(found_markers)}")
                    issues_found.append({
                        'thought': thought_name,
                        'alias': alias,
                        'markers': found_markers
                    })
                else:
                    print(f"✅ {alias}")
                    print(f"   en_title: {en_title}")
                    print(f"   en_content: {en_content[:80]}...")
                    print()
        
        # Summary
        print("=" * 80)
        print("VERIFICATION SUMMARY")
        print("=" * 80)
        print(f"Thoughts verified: {len(THOUGHT_NAMES)}")
        print(f"Issues found: {len(issues_found)}")
        
        if issues_found:
            print("\n❌ ISSUES DETECTED:")
            for issue in issues_found:
                print(f"  {issue['thought']}")
                if 'markers' in issue:
                    print(f"    Markers: {', '.join(issue['markers'])}")
                else:
                    print(f"    Issue: {issue['issue']}")
        else:
            print("\n✅ All thoughts verified clean - no multilingual markers found!")
        
        print("=" * 80)
        
    finally:
        driver.close()
    
    return issues_found

if __name__ == '__main__':
    verify_thoughts()
