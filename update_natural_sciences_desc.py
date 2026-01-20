"""
Update desc.NATURAL SCIENCES en_content field in Neo4j AuraDB
Adds a period at the end of the en_content field.
"""

from neo4j import GraphDatabase

# Neo4j AuraDB connection details
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

def update_description():
    """Update the en_content field for desc.NATURAL SCIENCES"""
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            # First, let's verify the current content
            print("Checking current en_content...")
            result = session.run("""
                MATCH (d:DESCRIPTION {name: "desc.NATURAL SCIENCES"})
                RETURN d.en_content as current_content
            """)
            
            record = result.single()
            if record:
                print(f"Current content: {record['current_content']}")
            else:
                print("Description node not found!")
                return
            
            # Update the en_content field
            new_content = "Any of the sciences (such as physics, chemistry, or biology) that deal with matter, energy, and their interrelations and transformations or with objectively measurable phenomena."
            
            print(f"\nUpdating to: {new_content}")
            
            result = session.run("""
                MATCH (d:DESCRIPTION {name: "desc.NATURAL SCIENCES"})
                SET d.en_content = $new_content
                RETURN d.en_content as updated_content
            """, new_content=new_content)
            
            record = result.single()
            if record:
                print(f"\n✓ Successfully updated!")
                print(f"New content: {record['updated_content']}")
            else:
                print("Update failed!")

if __name__ == "__main__":
    print("=" * 80)
    print("Updating desc.NATURAL SCIENCES en_content field")
    print("=" * 80)
    update_description()
    print("=" * 80)
