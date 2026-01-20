#!/usr/bin/env python3
"""
Find and delete duplicate COSMOLOGY topic entries in Neo4j AuraDB.
The script identifies the younger (more recently created) duplicate and removes it
along with its DESCRIPTION and relationship to parent topic.HUMANITY.
"""

from neo4j import GraphDatabase
from datetime import datetime

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def find_unique_topics_and_descriptions(tx):
    """Find unique TOPIC and DESCRIPTION nodes for COSMOLOGY."""
    # Get unique topics
    topics_query = """
    MATCH (t:TOPIC {name: 'topic.COSMOLOGY'})
    RETURN DISTINCT
        elementId(t) as topic_id,
        t.name as name,
        t.alias as alias
    """
    topics = [dict(record) for record in tx.run(topics_query)]
    
    # Get unique descriptions
    desc_query = """
    MATCH (t:TOPIC {name: 'topic.COSMOLOGY'})-[:HAS_DESCRIPTION]->(d:DESCRIPTION)
    RETURN DISTINCT
        elementId(d) as desc_id,
        d.en_content as content
    """
    descriptions = [dict(record) for record in tx.run(desc_query)]
    
    # Get relationships
    rel_query = """
    MATCH (parent:TOPIC {name: 'topic.HUMANITY'})-[r:HAS_CHILD]->(t:TOPIC {name: 'topic.COSMOLOGY'})
    RETURN DISTINCT
        elementId(r) as rel_id,
        elementId(t) as topic_id,
        parent.name as parent_name
    """
    relationships = [dict(record) for record in tx.run(rel_query)]
    
    return topics, descriptions, relationships

def extract_id_number(element_id):
    """Extract the numeric portion from a Neo4j element ID for comparison."""
    # Element IDs look like: 4:11d10329-e159-4d47-8092-68c08b7aab28:112
    # The last number (112) is what we care about
    parts = element_id.split(':')
    return int(parts[-1])

def delete_nodes_by_ids(tx, topic_ids, desc_ids, rel_ids):
    """Delete specified nodes and relationships by their element IDs."""
    # Delete relationships
    for rel_id in rel_ids:
        delete_rel_query = """
        MATCH ()-[r]->()
        WHERE elementId(r) = $rel_id
        DELETE r
        """
        tx.run(delete_rel_query, rel_id=rel_id)
        print(f"  ✓ Deleted relationship: {rel_id}")
    
    # Delete descriptions
    for desc_id in desc_ids:
        delete_desc_query = """
        MATCH (d:DESCRIPTION)
        WHERE elementId(d) = $desc_id
        DETACH DELETE d
        """
        tx.run(delete_desc_query, desc_id=desc_id)
        print(f"  ✓ Deleted DESCRIPTION: {desc_id}")
    
    # Delete topics
    for topic_id in topic_ids:
        delete_topic_query = """
        MATCH (t:TOPIC)
        WHERE elementId(t) = $topic_id
        DETACH DELETE t
        """
        tx.run(delete_topic_query, topic_id=topic_id)
        print(f"  ✓ Deleted TOPIC: {topic_id}")

def main():
    print("=" * 80)
    print("DUPLICATE COSMOLOGY TOPIC CLEANUP")
    print("=" * 80)
    print()
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        # Find all unique nodes
        with driver.session(database="neo4j") as session:
            topics, descriptions, relationships = session.execute_read(find_unique_topics_and_descriptions)
        
        print(f"Found {len(topics)} unique TOPIC nodes:")
        for topic in topics:
            print(f"  - ID: {topic['topic_id']}")
            print(f"    Alias: {topic['alias']}")
            print()
        
        print(f"Found {len(descriptions)} unique DESCRIPTION nodes:")
        for desc in descriptions:
            print(f"  - ID: {desc['desc_id']}")
            print(f"    Content: {desc['content'][:100]}..." if desc['content'] else "None")
            print()
        
        print(f"Found {len(relationships)} relationships from HUMANITY:")
        for rel in relationships:
            print(f"  - Rel ID: {rel['rel_id']}")
            print(f"    Points to TOPIC: {rel['topic_id']}")
            print()
        
        if len(topics) != 2:
            print(f"❌ Expected 2 duplicate TOPIC nodes, found {len(topics)}")
            return
        
        if len(descriptions) != 2:
            print(f"❌ Expected 2 duplicate DESCRIPTION nodes, found {len(descriptions)}")
            return
        
        # Determine which set is newer (higher ID number = newer)
        topics_sorted = sorted(topics, key=lambda x: extract_id_number(x['topic_id']), reverse=True)
        descs_sorted = sorted(descriptions, key=lambda x: extract_id_number(x['desc_id']), reverse=True)
        
        # The newer (younger) set
        newer_topic_id = topics_sorted[0]['topic_id']
        newer_desc_id = descs_sorted[0]['desc_id']
        
        # Find relationships pointing to the newer topic
        newer_rels = [r['rel_id'] for r in relationships if r['topic_id'] == newer_topic_id]
        
        print("=" * 80)
        print("DELETION TARGET (Newer/Younger duplicate):")
        print("=" * 80)
        print(f"  TOPIC ID: {newer_topic_id} (ID#: {extract_id_number(newer_topic_id)})")
        print(f"  DESCRIPTION ID: {newer_desc_id} (ID#: {extract_id_number(newer_desc_id)})")
        print(f"  Relationships: {len(newer_rels)}")
        for rel_id in newer_rels:
            print(f"    - {rel_id}")
        print()
        
        print("KEEPING (Older set):")
        print("=" * 80)
        print(f"  TOPIC ID: {topics_sorted[1]['topic_id']} (ID#: {extract_id_number(topics_sorted[1]['topic_id'])})")
        print(f"  DESCRIPTION ID: {descs_sorted[1]['desc_id']} (ID#: {extract_id_number(descs_sorted[1]['desc_id'])})")
        print()
        
        # Confirm deletion
        confirm = input("⚠️  Proceed with deletion? Type 'DELETE' to confirm: ")
        
        if confirm != 'DELETE':
            print("\n❌ Deletion cancelled.")
            return
        
        print("\n🗑️  Deleting newer duplicate...\n")
        
        # Perform deletion
        with driver.session(database="neo4j") as session:
            session.execute_write(
                delete_nodes_by_ids,
                [newer_topic_id],
                [newer_desc_id],
                newer_rels
            )
        
        print("\n✅ Successfully deleted duplicate COSMOLOGY topic!")
        print("\nVerifying remaining nodes...")
        
        # Verify only one of each remains
        with driver.session(database="neo4j") as session:
            topics, descriptions, relationships = session.execute_read(find_unique_topics_and_descriptions)
        
        if len(topics) == 1 and len(descriptions) == 1:
            print(f"✓ Confirmed: Only 1 TOPIC and 1 DESCRIPTION remain")
            print(f"  TOPIC ID: {topics[0]['topic_id']}")
            print(f"  DESCRIPTION ID: {descriptions[0]['desc_id']}")
        else:
            print(f"⚠️  Warning: {len(topics)} TOPIC nodes and {len(descriptions)} DESCRIPTION nodes still exist!")


if __name__ == "__main__":
    main()
