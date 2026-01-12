from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def query_thought():
    """Query the thought.692-189 node and its content from Neo4j"""
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            # Query THOUGHT node
            thought_result = session.run("""
                MATCH (t:THOUGHT)
                WHERE t.name = "thought.692-189" OR t.alias CONTAINS "692"
                RETURN t
            """)
            
            thought_records = list(thought_result)
            
            if not thought_records:
                print("No THOUGHT node found matching 692-189")
                return
            
            print("=== THOUGHT Node ===")
            thought = thought_records[0]["t"]
            for key in sorted(thought.keys()):
                print(f"{key}: {thought[key]}")
            
            # Query CONTENT node
            print("\n=== CONTENT Node ===")
            content_result = session.run("""
                MATCH (t:THOUGHT)-[:HAS_CONTENT]->(c:CONTENT)
                WHERE t.name = "thought.692-189" OR t.alias CONTAINS "692"
                RETURN c
            """)
            
            content_records = list(content_result)
            if content_records:
                content = content_records[0]["c"]
                for key in sorted(content.keys()):
                    print(f"{key}: {content[key]}")
            else:
                print("No CONTENT node found")
            
            # Query parent relationship
            print("\n=== Parent Relationship ===")
            parent_result = session.run("""
                MATCH (parent:TOPIC)-[:HAS_THOUGHT]->(t:THOUGHT)
                WHERE t.name = "thought.692-189" OR t.alias CONTAINS "692"
                RETURN parent.name as parent_name
            """)
            
            parent_records = list(parent_result)
            if parent_records:
                print(f"Parent: {parent_records[0]['parent_name']}")
            else:
                print("No parent relationship found")

if __name__ == "__main__":
    query_thought()
