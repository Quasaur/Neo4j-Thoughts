#!/usr/bin/env python3
"""
Verify that topic.SOCIOLOGY is still connected to its DESCRIPTION node.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def check_description_relationship(tx):
    """Check if SOCIOLOGY has a DESCRIPTION relationship."""
    query = """
    MATCH (sociology:TOPIC {name: 'topic.SOCIOLOGY'})
    OPTIONAL MATCH (sociology)-[r:HAS_DESCRIPTION]->(desc:DESCRIPTION)
    RETURN 
        sociology.name as topic_name,
        sociology.alias as topic_alias,
        COUNT(r) as description_count,
        desc.name as desc_name,
        desc.en_content as desc_content
    """
    result = tx.run(query)
    return [dict(record) for record in result]

def main():
    print("=" * 80)
    print("VERIFYING SOCIOLOGY DESCRIPTION RELATIONSHIP")
    print("=" * 80)
    print()
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            results = session.execute_read(check_description_relationship)
        
        if not results:
            print("❌ Error: topic.SOCIOLOGY not found!")
            return
        
        result = results[0]
        
        print(f"Topic: {result['topic_name']}")
        print(f"Alias: {result['topic_alias']}")
        print()
        
        if result['description_count'] > 0:
            print(f"✅ HAS_DESCRIPTION relationship exists!")
            print(f"   Description name: {result['desc_name']}")
            print(f"   Content preview: {result['desc_content'][:150] if result['desc_content'] else 'None'}...")
        else:
            print("❌ No HAS_DESCRIPTION relationship found!")

if __name__ == "__main__":
    main()
