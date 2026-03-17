#!/usr/bin/env python3
"""
Check if both 'topic.SOCIAL SCIENCES' and 'topic.SOCIAL SCIENCE' exist in Neo4j AuraDB.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def check_topics(tx, topic_names):
    """Check if topics exist and get their details."""
    results = {}
    
    for topic_name in topic_names:
        query = """
        MATCH (t:TOPIC {name: $topic_name})
        OPTIONAL MATCH (t)-[:HAS_DESCRIPTION]->(d:DESCRIPTION)
        OPTIONAL MATCH (parent:TOPIC)-[:HAS_CHILD]->(t)
        RETURN 
            count(t) as count,
            collect(DISTINCT {
                id: elementId(t),
                alias: t.alias,
                description: d.en_content,
                parent_name: parent.name,
                parent_alias: parent.alias
            }) as details
        """
        result = tx.run(query, topic_name=topic_name).single()
        results[topic_name] = {
            'count': result['count'],
            'details': result['details']
        }
    
    return results

def main():
    print("=" * 80)
    print("CHECKING FOR POLITICAL SCIENCE TOPICS IN NEO4J AURADB")
    print("=" * 80)
    print()
    
    topic_names = ["topic.POLITICAL SCIENCE", "topic.POLITICAL SCIENCES"]
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            results = session.execute_read(check_topics, topic_names)
        
        for topic_name in topic_names:
            print(f"Topic: {topic_name}")
            print("-" * 80)
            
            count = results[topic_name]['count']
            details = results[topic_name]['details']
            
            if count == 0:
                print("  ❌ NOT FOUND")
            else:
                print(f"  ✓ FOUND ({count} instance(s))")
                
                for idx, detail in enumerate(details, 1):
                    if detail['id']:  # Only show if there's actual data
                        print(f"\n  Instance {idx}:")
                        print(f"    Element ID: {detail['id']}")
                        print(f"    Alias: {detail['alias']}")
                        if detail['parent_name']:
                            print(f"    Parent: {detail['parent_name']} ({detail['parent_alias']})")
                        if detail['description']:
                            desc_preview = detail['description'][:100] + "..." if len(detail['description']) > 100 else detail['description']
                            print(f"    Description: {desc_preview}")
            
            print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for topic_name in topic_names:
        count = results[topic_name]['count']
        status = "EXISTS ✓" if count > 0 else "DOES NOT EXIST ❌"
        print(f"  {topic_name}: {status}")

if __name__ == "__main__":
    main()
