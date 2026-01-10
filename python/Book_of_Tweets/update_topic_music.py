import sys
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Update queries
q1_update_topic = """
MATCH (t:TOPIC {name: "topic.MUSIC"})
SET t.parent = "topic.MUSICOLOGY",
    t.level = 5
"""

q2_delete_old_parent_link = """
MATCH (parent:TOPIC {name: "topic.BEAUTY"})-[r:HAS_CHILD {name: "edge.BEAUTY->MUSIC"}]->(child:TOPIC {name: "topic.MUSIC"})
DELETE r
"""

q3_create_new_parent_link = """
MATCH (parent:TOPIC {name: "topic.MUSICOLOGY"})
MATCH (child:TOPIC {name: "topic.MUSIC"})
MERGE (parent)-[:HAS_CHILD {name: "edge.MUSICOLOGY->MUSIC"}]->(child)
"""

def execute_queries():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    try:
        with driver.session(database="neo4j") as session:
            print("Updating topic.MUSIC in Neo4j AuraDB...")
            
            # 1. Update TOPIC properties
            print("1/3: Updating TOPIC properties (parent, level)...")
            session.run(q1_update_topic)
            
            # 2. Delete old parent relationship
            print("2/3: Deleting old parent relationship (topic.BEAUTY -> topic.MUSIC)...")
            session.run(q2_delete_old_parent_link)
            
            # 3. Create new parent relationship
            print("3/3: Creating new parent relationship (topic.MUSICOLOGY -> topic.MUSIC)...")
            session.run(q3_create_new_parent_link)
            
            print("\nAll updates executed successfully.")
            print("topic.MUSIC now has topic.MUSICOLOGY as its parent!")

    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)
    finally:
        driver.close()

if __name__ == "__main__":
    execute_queries()
