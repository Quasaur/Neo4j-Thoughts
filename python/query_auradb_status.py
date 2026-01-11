#!/usr/bin/env python3
"""
Query Neo4j AuraDB to see existing THOUGHT and CONTENT nodes
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


def query_database():
    """Query the database for existing nodes."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Count THOUGHT nodes
            result = session.run("MATCH (t:THOUGHT) RETURN count(t) as count")
            thought_count = result.single()['count']
            print(f"Total THOUGHT nodes: {thought_count}")
            
            # Count CONTENT nodes
            result = session.run("MATCH (c:CONTENT) RETURN count(c) as count")
            content_count = result.single()['count']
            print(f"Total CONTENT nodes: {content_count}")
            
            # Check for nodes with placeholder translations
            result = session.run("""
                MATCH (c:CONTENT)
                WHERE c.es_title = 'TITULO DEL PENSAMIENTO'
                RETURN count(c) as count
            """)
            placeholder_count = result.single()['count']
            print(f"Nodes with placeholder translations: {placeholder_count}")
            
            # Sample some THOUGHT names
            print("\nSample THOUGHT nodes (first 10):")
            result = session.run("""
                MATCH (t:THOUGHT)
                RETURN t.name as name
                LIMIT 10
            """)
            for record in result:
                print(f"  - {record['name']}")
            
            # Sample some CONTENT nodes with placeholders
            print("\nSample CONTENT nodes with placeholders (first 10):")
            result = session.run("""
                MATCH (c:CONTENT)
                WHERE c.es_title = 'TITULO DEL PENSAMIENTO'
                RETURN c.name as name, c.en_title as en_title
                LIMIT 10
            """)
            for record in result:
                print(f"  - {record['name']}: {record['en_title']}")
    
    finally:
        driver.close()


if __name__ == "__main__":
    query_database()
