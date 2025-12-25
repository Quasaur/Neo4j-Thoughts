from neo4j import GraphDatabase
import os

# Cleaned URI
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def update_topic():
    print(f"Connecting to {URI}...")
    try:
        driver = GraphDatabase.driver(URI, auth=AUTH)
        driver.verify_connectivity()
        print("Connectivity verified.")
        
        query = """
        MATCH (n:TOPIC {name: "NULL TOPIC"})
        SET n.name = "topic.NULL TOPIC"
        RETURN n
        """
        with driver.session() as session:
            result = session.run(query)
            record = result.single()
            if record:
                print(f"Updated node: {record['n']}")
            else:
                # If name is already changed or node not found
                print("No node found with name 'NULL TOPIC'. Checking if it was already updated...")
                check_query = "MATCH (n:TOPIC {name: 'topic.NULL TOPIC'}) RETURN n"
                result = session.run(check_query)
                record = result.single()
                if record:
                    print("Found node with new name 'topic.NULL TOPIC'. Update likely already happened.")
                else:
                    print("Node not found at all.")
                    
        driver.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_topic()
