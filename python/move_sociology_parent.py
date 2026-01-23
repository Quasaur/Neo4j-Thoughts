#!/usr/bin/env python3
"""
Move topic.SOCIOLOGY from parent topic.HUMANITY to parent topic.SOCIAL SCIENCES.
This will:
1. Delete the existing HAS_CHILD relationship from HUMANITY to SOCIOLOGY
2. Create a new HAS_CHILD relationship from SOCIAL SCIENCES to SOCIOLOGY
3. All child relationships of SOCIOLOGY remain intact (no changes needed)
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def verify_nodes_exist(tx):
    """Verify that all required nodes exist."""
    query = """
    MATCH (sociology:TOPIC {name: 'topic.SOCIOLOGY'})
    OPTIONAL MATCH (humanity:TOPIC {name: 'topic.HUMANITY'})
    OPTIONAL MATCH (social_sciences:TOPIC {name: 'topic.SOCIAL SCIENCES'})
    OPTIONAL MATCH (humanity)-[old_rel:HAS_CHILD]->(sociology)
    RETURN 
        sociology.name as sociology_name,
        sociology.alias as sociology_alias,
        humanity.name as humanity_name,
        social_sciences.name as social_sciences_name,
        COUNT(old_rel) as existing_rel_count
    """
    result = tx.run(query)
    record = result.single()
    return dict(record) if record else None

def move_parent_relationship(tx):
    """Delete old parent relationship and create new one."""
    # Delete the old relationship from HUMANITY to SOCIOLOGY
    delete_query = """
    MATCH (humanity:TOPIC {name: 'topic.HUMANITY'})-[r:HAS_CHILD]->(sociology:TOPIC {name: 'topic.SOCIOLOGY'})
    DELETE r
    RETURN COUNT(r) as deleted_count
    """
    delete_result = tx.run(delete_query)
    deleted_count = delete_result.single()['deleted_count']
    
    # Create the new relationship from SOCIAL SCIENCES to SOCIOLOGY
    create_query = """
    MATCH (social_sciences:TOPIC {name: 'topic.SOCIAL SCIENCES'})
    MATCH (sociology:TOPIC {name: 'topic.SOCIOLOGY'})
    CREATE (social_sciences)-[r:HAS_CHILD]->(sociology)
    RETURN COUNT(r) as created_count
    """
    create_result = tx.run(create_query)
    created_count = create_result.single()['created_count']
    
    return deleted_count, created_count

def verify_child_relationships(tx):
    """Verify that SOCIOLOGY's child relationships remain intact."""
    query = """
    MATCH (sociology:TOPIC {name: 'topic.SOCIOLOGY'})-[:HAS_CHILD]->(child)
    RETURN COUNT(child) as child_count, COLLECT(child.name) as children
    """
    result = tx.run(query)
    record = result.single()
    return dict(record) if record else {'child_count': 0, 'children': []}

def main():
    print("=" * 80)
    print("MOVING SOCIOLOGY TOPIC PARENT")
    print("=" * 80)
    print()
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        # Step 1: Verify all nodes exist
        print("Step 1: Verifying nodes exist...")
        with driver.session(database="neo4j") as session:
            verification = session.execute_read(verify_nodes_exist)
        
        if not verification:
            print("❌ Error: Could not query database")
            return
        
        if not verification['sociology_name']:
            print("❌ Error: topic.SOCIOLOGY not found!")
            return
        
        if not verification['humanity_name']:
            print("❌ Error: topic.HUMANITY not found!")
            return
        
        if not verification['social_sciences_name']:
            print("❌ Error: topic.SOCIAL SCIENCES not found!")
            return
        
        print(f"✓ Found SOCIOLOGY (alias: {verification['sociology_alias']})")
        print(f"✓ Found HUMANITY")
        print(f"✓ Found SOCIAL SCIENCES")
        print(f"✓ Existing HUMANITY→SOCIOLOGY relationships: {verification['existing_rel_count']}")
        print()
        
        # Step 2: Check SOCIOLOGY's children before change
        print("Step 2: Checking SOCIOLOGY's children before change...")
        with driver.session(database="neo4j") as session:
            children_before = session.execute_read(verify_child_relationships)
        
        print(f"✓ SOCIOLOGY has {children_before['child_count']} children")
        if children_before['child_count'] > 0:
            print("  Children:")
            for child in children_before['children']:
                print(f"    - {child}")
        print()
        
        # Step 3: Confirm the operation
        print("=" * 80)
        print("PLANNED CHANGES:")
        print("=" * 80)
        print("1. DELETE: topic.HUMANITY → topic.SOCIOLOGY")
        print("2. CREATE: topic.SOCIAL SCIENCES → topic.SOCIOLOGY")
        print(f"3. PRESERVE: All {children_before['child_count']} child relationships of SOCIOLOGY")
        print()
        
        confirm = input("⚠️  Proceed with this change? Type 'MOVE' to confirm: ")
        
        if confirm != 'MOVE':
            print("\n❌ Operation cancelled.")
            return
        
        # Step 4: Execute the move
        print("\n🔄 Moving parent relationship...\n")
        
        with driver.session(database="neo4j") as session:
            deleted, created = session.execute_write(move_parent_relationship)
        
        print(f"✓ Deleted {deleted} old relationship(s)")
        print(f"✓ Created {created} new relationship(s)")
        print()
        
        # Step 5: Verify the changes
        print("Step 5: Verifying changes...")
        
        with driver.session(database="neo4j") as session:
            children_after = session.execute_read(verify_child_relationships)
        
        if children_after['child_count'] == children_before['child_count']:
            print(f"✓ Confirmed: SOCIOLOGY still has {children_after['child_count']} children")
        else:
            print(f"⚠️  Warning: Child count changed from {children_before['child_count']} to {children_after['child_count']}")
        
        # Final verification
        with driver.session(database="neo4j") as session:
            final_check = session.execute_read(verify_nodes_exist)
        
        if final_check['existing_rel_count'] == 0:
            print("✓ Confirmed: Old HUMANITY→SOCIOLOGY relationship removed")
        else:
            print(f"⚠️  Warning: {final_check['existing_rel_count']} HUMANITY→SOCIOLOGY relationships still exist")
        
        print("\n✅ Successfully moved topic.SOCIOLOGY!")
        print(f"   New parent: topic.SOCIAL SCIENCES")
        print(f"   Children preserved: {children_after['child_count']}")


if __name__ == "__main__":
    main()
