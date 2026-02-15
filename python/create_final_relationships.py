#!/usr/bin/env python3
"""
Create the final 2 missing HAS_THOUGHT relationships with corrected parent topic names.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# The two relationships that need the corrected parent names
RELATIONSHIPS = [
    {
        'parent': 'topic.THE GOSPEL',  # Not THE-GOSPEL
        'child': 'thought.DEATH_ROW',
        'edge_name': 't.edge.THE GOSPEL->DEATH_ROW'
    },
    {
        'parent': 'topic.DIVINE SOVEREIGNTY',  # Not DIVINE-SOVEREIGNTY
        'child': 'thought.UNFAIR',
        'edge_name': 't.edge.DIVINE SOVEREIGNTY->UNFAIR'
    }
]

def create_relationship(session, parent_name, child_name, edge_name):
    """Create HAS_THOUGHT relationship."""
    query = """
    MATCH (parent:TOPIC {name: $parent_name})
    MATCH (child:THOUGHT {name: $child_name})
    MERGE (parent)-[r:HAS_THOUGHT {name: $edge_name}]->(child)
    RETURN r
    """
    
    result = session.run(query, parent_name=parent_name, child_name=child_name, edge_name=edge_name)
    return result.single()

def main():
    """Create the final 2 missing relationships."""
    print("=" * 80)
    print("CREATING FINAL 2 HAS_THOUGHT RELATIONSHIPS")
    print("=" * 80)
    print()
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            for rel in RELATIONSHIPS:
                parent = rel['parent']
                child = rel['child']
                edge_name = rel['edge_name']
                
                print(f"Creating: {parent} -[HAS_THOUGHT]-> {child}")
                print(f"Edge name: {edge_name}")
                
                try:
                    result = create_relationship(session, parent, child, edge_name)
                    if result:
                        print(f"✅ Relationship created successfully")
                    else:
                        print(f"❌ Failed - no result returned")
                except Exception as e:
                    print(f"❌ Error: {str(e)}")
                
                print()
        
        print("=" * 80)
        print("✅ Final relationships created!")
        print("=" * 80)
        
    finally:
        driver.close()

if __name__ == '__main__':
    main()
