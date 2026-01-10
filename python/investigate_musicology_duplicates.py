from neo4j import GraphDatabase
import json

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def investigate_musicology():
    """Investigate duplicate MUSICOLOGY topic nodes"""
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Query to find all MUSICOLOGY nodes
            query = """
            MATCH (t:TOPIC)
            WHERE t.name = "topic.MUSICOLOGY"
            RETURN t
            ORDER BY id(t)
            """
            
            result = session.run(query)
            records = list(result)
            
            print(f"Found {len(records)} MUSICOLOGY topic node(s)\n")
            print("=" * 80)
            
            for idx, record in enumerate(records, 1):
                node = record["t"]
                print(f"\nRecord #{idx}:")
                print(f"  Internal ID: {node.id}")
                print(f"  Properties:")
                for key, value in sorted(node.items()):
                    print(f"    {key}: {value}")
            
            # Check relationships for each node
            print("\n" + "=" * 80)
            print("\nRelationship Analysis:")
            print("=" * 80)
            
            for idx, record in enumerate(records, 1):
                node = record["t"]
                node_id = node.id
                
                print(f"\nRecord #{idx} (Internal ID: {node_id}):")
                
                # Check parent relationships
                parent_query = """
                MATCH (parent:TOPIC)-[:HAS_CHILD]->(child:TOPIC)
                WHERE id(child) = $node_id
                RETURN parent.name as parent_name
                """
                parent_result = session.run(parent_query, node_id=node_id)
                parents = [r["parent_name"] for r in parent_result]
                print(f"  Parent nodes: {parents if parents else 'None'}")
                
                # Check child relationships
                child_query = """
                MATCH (parent:TOPIC)-[:HAS_CHILD]->(child:TOPIC)
                WHERE id(parent) = $node_id
                RETURN child.name as child_name
                """
                child_result = session.run(child_query, node_id=node_id)
                children = [r["child_name"] for r in child_result]
                print(f"  Child nodes: {children if children else 'None'}")
                
                # Check description relationships
                desc_query = """
                MATCH (t:TOPIC)-[:HAS_DESCRIPTION]->(d:DESCRIPTION)
                WHERE id(t) = $node_id
                RETURN d.name as desc_name
                """
                desc_result = session.run(desc_query, node_id=node_id)
                descriptions = [r["desc_name"] for r in desc_result]
                print(f"  Description nodes: {descriptions if descriptions else 'None'}")
            
            # Summary and recommendation
            print("\n" + "=" * 80)
            print("\nROOT CAUSE ANALYSIS:")
            print("=" * 80)
            
            if len(records) > 1:
                print(f"\n⚠️  DUPLICATE NODES DETECTED: {len(records)} nodes with name 'topic.MUSICOLOGY'")
                print("\nThis likely occurred due to:")
                print("  1. Multiple executions of the CREATE statement without using MERGE")
                print("  2. Lack of uniqueness constraint on TOPIC.name property")
                print("  3. Script re-runs without checking for existing nodes")
                print("\nRecommended Actions:")
                print("  1. Identify which node has the correct relationships")
                print("  2. Delete the duplicate node(s)")
                print("  3. Add a uniqueness constraint: CREATE CONSTRAINT ON (t:TOPIC) ASSERT t.name IS UNIQUE")
            else:
                print("\n✓ No duplicate nodes found - false alarm!")
                
    finally:
        driver.close()

if __name__ == "__main__":
    investigate_musicology()
