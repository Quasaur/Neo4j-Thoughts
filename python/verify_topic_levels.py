from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def verify_topic_levels():
    """Verify the levels of the six topics from NULL TOPIC to MUSIC"""
    
    # Topics to verify with their expected levels
    topics_to_check = [
        ("topic.NULL TOPIC", 0),
        ("topic.THE GODHEAD", 1),
        ("topic.CREATION", 2),
        ("topic.HUMANITY", 3),
        ("topic.MUSICOLOGY", 4),
        ("topic.MUSIC", 5)
    ]
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            print("Verifying TOPIC levels in Neo4j AuraDB:\n")
            print(f"{'Topic Name':<25} {'Expected':<10} {'Actual':<10} {'Status'}")
            print("=" * 70)
            
            all_correct = True
            
            for topic_name, expected_level in topics_to_check:
                # Query to get the level of the topic
                query = """
                MATCH (t:TOPIC {name: $topic_name})
                RETURN t.name as name, t.level as level
                """
                
                result = session.run(query, topic_name=topic_name)
                record = result.single()
                
                if record:
                    actual_level = record["level"]
                    status = "✓ CORRECT" if actual_level == expected_level else "✗ MISMATCH"
                    
                    if actual_level != expected_level:
                        all_correct = False
                    
                    print(f"{topic_name:<25} {expected_level:<10} {actual_level if actual_level is not None else 'NULL':<10} {status}")
                else:
                    print(f"{topic_name:<25} {expected_level:<10} {'NOT FOUND':<10} ✗ MISSING")
                    all_correct = False
            
            print("=" * 70)
            if all_correct:
                print("\n✓ All topic levels are correct!")
            else:
                print("\n✗ Some topics have incorrect or missing levels!")
            
    finally:
        driver.close()

if __name__ == "__main__":
    verify_topic_levels()
