from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def fix_musicology_duplicates():
    """Fix duplicate MUSICOLOGY nodes by keeping ID 121 and removing ID 123"""
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            print("=" * 80)
            print("STEP 1: Verify current state")
            print("=" * 80)
            
            # Get both nodes using element_id (new way)
            query_get_nodes = """
            MATCH (t:TOPIC)
            WHERE t.name = "topic.MUSICOLOGY"
            RETURN elementId(t) as element_id, id(t) as internal_id, t
            ORDER BY id(t)
            """
            
            result = session.run(query_get_nodes)
            nodes = list(result)
            
            print(f"\nFound {len(nodes)} MUSICOLOGY nodes:")
            for node in nodes:
                print(f"  Internal ID {node['internal_id']}: Element ID {node['element_id']}")
            
            if len(nodes) != 2:
                print(f"\n⚠️  Expected 2 nodes, found {len(nodes)}. Aborting.")
                return
            
            # Identify the nodes
            keep_node_id = nodes[0]['internal_id']  # Should be 121
            delete_node_id = nodes[1]['internal_id']  # Should be 123
            
            if keep_node_id != 121 or delete_node_id != 123:
                print(f"\n⚠️  Warning: Expected IDs 121 and 123, got {keep_node_id} and {delete_node_id}")
                print("Continuing anyway - keeping lower ID...")
            
            print(f"\n✓ Will keep node {keep_node_id} and delete node {delete_node_id}")
            
            # Step 2: Check for unique relationships on node to be deleted
            print("\n" + "=" * 80)
            print("STEP 2: Check relationships on node to be deleted")
            print("=" * 80)
            
            check_relationships = """
            MATCH (t:TOPIC)
            WHERE id(t) = $node_id
            OPTIONAL MATCH (t)-[r]->(other)
            RETURN type(r) as rel_type, labels(other) as other_labels, 
                   other.name as other_name
            """
            
            result = session.run(check_relationships, node_id=delete_node_id)
            delete_node_rels = list(result)
            
            print(f"\nRelationships on node {delete_node_id}:")
            for rel in delete_node_rels:
                if rel['rel_type']:
                    print(f"  -{rel['rel_type']}-> {rel['other_labels']} ({rel['other_name']})")
            
            # Step 3: Ensure node 121 has all necessary relationships
            print("\n" + "=" * 80)
            print("STEP 3: Verify node 121 has all necessary relationships")
            print("=" * 80)
            
            # Check parent relationship to HUMANITY
            verify_parent = """
            MATCH (parent:TOPIC {name: "topic.HUMANITY"})-[:HAS_CHILD]->(child:TOPIC)
            WHERE id(child) = 121
            RETURN count(*) as count
            """
            result = session.run(verify_parent)
            has_parent = result.single()['count'] > 0
            print(f"  Parent (HUMANITY) relationship: {'✓ EXISTS' if has_parent else '✗ MISSING'}")
            
            # Check child relationship to MUSIC
            verify_child = """
            MATCH (parent:TOPIC)-[:HAS_CHILD]->(child:TOPIC {name: "topic.MUSIC"})
            WHERE id(parent) = 121
            RETURN count(*) as count
            """
            result = session.run(verify_child)
            has_child = result.single()['count'] > 0
            print(f"  Child (MUSIC) relationship: {'✓ EXISTS' if has_child else '✗ MISSING'}")
            
            # Check description relationship
            verify_desc = """
            MATCH (t:TOPIC)-[:HAS_DESCRIPTION]->(d:DESCRIPTION)
            WHERE id(t) = 121
            RETURN count(*) as count
            """
            result = session.run(verify_desc)
            has_desc = result.single()['count'] > 0
            print(f"  Description relationship: {'✓ EXISTS' if has_desc else '✗ MISSING'}")
            
            # Step 4: Delete duplicate node 123
            print("\n" + "=" * 80)
            print("STEP 4: Delete duplicate node")
            print("=" * 80)
            
            delete_query = """
            MATCH (t:TOPIC)
            WHERE id(t) = $node_id
            DETACH DELETE t
            RETURN count(*) as deleted
            """
            
            result = session.run(delete_query, node_id=delete_node_id)
            deleted_count = result.single()['deleted']
            print(f"\n✓ Deleted {deleted_count} node (ID {delete_node_id}) and all its relationships")
            
            # Step 5: Add uniqueness constraint
            print("\n" + "=" * 80)
            print("STEP 5: Add uniqueness constraint on TOPIC.name")
            print("=" * 80)
            
            try:
                constraint_query = """
                CREATE CONSTRAINT topic_name_unique IF NOT EXISTS
                FOR (t:TOPIC) REQUIRE t.name IS UNIQUE
                """
                session.run(constraint_query)
                print("\n✓ Uniqueness constraint created successfully")
            except Exception as e:
                if "already exists" in str(e).lower() or "equivalent" in str(e).lower():
                    print("\n✓ Uniqueness constraint already exists")
                else:
                    print(f"\n⚠️  Warning creating constraint: {e}")
            
            # Step 6: Final verification
            print("\n" + "=" * 80)
            print("STEP 6: Final verification")
            print("=" * 80)
            
            final_check = """
            MATCH (t:TOPIC)
            WHERE t.name = "topic.MUSICOLOGY"
            RETURN count(*) as count
            """
            result = session.run(final_check)
            final_count = result.single()['count']
            
            print(f"\nFinal count of MUSICOLOGY nodes: {final_count}")
            
            if final_count == 1:
                print("\n" + "=" * 80)
                print("✓ SUCCESS! Duplicate removed and constraint added")
                print("=" * 80)
                
                # Show the remaining node
                show_node = """
                MATCH (t:TOPIC {name: "topic.MUSICOLOGY"})
                OPTIONAL MATCH (parent)-[:HAS_CHILD]->(t)
                OPTIONAL MATCH (t)-[:HAS_CHILD]->(child)
                OPTIONAL MATCH (t)-[:HAS_DESCRIPTION]->(desc)
                RETURN id(t) as id, t.name as name, t.level as level,
                       collect(DISTINCT parent.name) as parents,
                       collect(DISTINCT child.name) as children,
                       collect(DISTINCT desc.name) as descriptions
                """
                result = session.run(show_node)
                node_info = result.single()
                
                print(f"\nRemaining MUSICOLOGY node (ID {node_info['id']}):")
                print(f"  Name: {node_info['name']}")
                print(f"  Level: {node_info['level']}")
                print(f"  Parents: {node_info['parents']}")
                print(f"  Children: {node_info['children']}")
                print(f"  Descriptions: {node_info['descriptions']}")
            else:
                print("\n✗ WARNING: Expected 1 node but found {final_count}")
                
    finally:
        driver.close()

if __name__ == "__main__":
    fix_musicology_duplicates()
