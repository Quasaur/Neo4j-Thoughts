#!/usr/bin/env python3
"""
Check if the parent topics exist for the two failed relationships.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def check_topics():
    """Check if specific topics exist."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    topics_to_check = [
        "topic.THE-GOSPEL",
        "topic.DIVINE-SOVEREIGNTY",
    ]
    
    print("=" * 80)
    print("CHECKING FOR MISSING PARENT TOPICS")
    print("=" * 80)
    print()
    
    try:
        with driver.session() as session:
            for topic_name in topics_to_check:
                query = "MATCH (t:TOPIC {name: $topic_name}) RETURN t.name as name, t.alias as alias"
                result = session.run(query, topic_name=topic_name)
                record = result.single()
                
                if record:
                    print(f"✅ {topic_name}")
                    print(f"   Alias: {record['alias']}")
                else:
                    print(f"❌ {topic_name} - NOT FOUND")
                    
                    # Search for similar topics
                    search_query = """
                    MATCH (t:TOPIC)
                    WHERE t.name CONTAINS $search_term OR t.alias CONTAINS $search_term
                    RETURN t.name as name, t.alias as alias
                    LIMIT 5
                    """
                    
                    # Extract search term from topic name
                    search_term = topic_name.replace('topic.', '').replace('-', ' ')
                    search_result = session.run(search_query, search_term=search_term)
                    
                    similar = list(search_result)
                    if similar:
                        print(f"   Similar topics found:")
                        for rec in similar:
                            print(f"     - {rec['name']}: {rec['alias']}")
                    else:
                        print(f"   No similar topics found")
                
                print()
    
    finally:
        driver.close()

if __name__ == '__main__':
    check_topics()
