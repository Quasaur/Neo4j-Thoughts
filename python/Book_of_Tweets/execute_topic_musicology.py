import sys
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Individual statements
q1_topic = """
CREATE (t:TOPIC {
    name: "topic.MUSICOLOGY",
    alias: "Topic: Musicology",
    parent: "topic.HUMANITY",
    tags: ["musicology", "music", "study", "research", "history", "theory"],
    notes: "",
    level: 4
});
"""

q1_desc = """
CREATE (d:DESCRIPTION {
    name: "description.MUSICOLOGY",
    en_title: "Musicology",
    en_content: "The scholarly study of music, encompassing the historical, cultural, theoretical, and scientific aspects of music and its role in human society.",
    es_title: "Musicología",
    es_content: "El estudio académico de la música, que abarca los aspectos históricos, culturales, teóricos y científicos de la música y su papel en la sociedad humana.",
    fr_title: "Musicologie",
    fr_content: "L'étude savante de la musique, englobant les aspects historiques, culturels, théoriques et scientifiques de la musique et son rôle dans la société humaine.",
    hi_title: "संगीत विज्ञान",
    hi_content: "संगीत का विद्वतापूर्ण अध्ययन, जिसमें संगीत के ऐतिहासिक, सांस्कृतिक, सैद्धांतिक और वैज्ञानिक पहलुओं और मानव समाज में इसकी भूमिका को शामिल किया गया है।",
    zh_title: "yīn yuè xué",
    zh_content: "yīn yuè de xué shù yán jiū ， bāo kuò yīn yuè de lì shǐ 、 wén huà 、 lǐ lùn hé kē xué fāng miàn jí qí zài rén lèi shè huì zhōng de zuò yòng 。"
});
"""

q2_link_desc = """
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.MUSICOLOGY" AND d.name = "description.MUSICOLOGY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MUSICOLOGY"}]->(d);
"""

q3_link_parent = """
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.HUMANITY" AND child.name = "topic.MUSICOLOGY"
MERGE (parent)-[:HAS_CHILD {name: "edge.HUMANITY->MUSICOLOGY"}]->(child);
"""

def execute_queries():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    try:
        with driver.session(database="neo4j") as session:
            print("Executing Cypher statements...")
            
            # 1. Create Topic
            print("1/4: Creating TOPIC node...")
            session.run(q1_topic)
            
            # 2. Create Description
            print("2/4: Creating DESCRIPTION node...")
            session.run(q1_desc)
            
            # 3. Link Description
            print("3/4: Linking DESCRIPTION to TOPIC...")
            session.run(q2_link_desc)
            
            # 4. Link to Parent
            print("4/4: Linking to Parent TOPIC (topic.HUMANITY)...")
            session.run(q3_link_parent)
            
            print("\nAll statements executed successfully.")
            print("topic.MUSICOLOGY has been inserted into Neo4j AuraDB!")

    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)
    finally:
        driver.close()

if __name__ == "__main__":
    execute_queries()
