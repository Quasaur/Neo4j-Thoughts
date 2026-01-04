import sys
from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Individual statements
q1_topic = """
CREATE (t:TOPIC {
    name: "topic.MUSIC",
    alias: "Topic: Music",
    parent: "topic.BEAUTY",
    tags: ["music", "art", "sound", "harmony", "melody"],
    level: 3
});
"""

q1_desc = """
CREATE (d:DESCRIPTION {
    name: "description.MUSIC",
    en_title: "Music",
    en_content: "The art and science of combining vocal or instrumental sounds to produce beauty of form, harmony, and expression of emotion.",
    es_title: "Música",
    es_content: "El arte y la ciencia de combinar sonidos vocales o instrumentales para producir belleza de forma, armonía y expresión de emociones.",
    fr_title: "Musique",
    fr_content: "L'art et la science de combiner des sons vocaux ou instrumentaux pour produire une beauté de forme, d'harmonie et une expression d'émotion.",
    hi_title: "संगीत",
    hi_content: "संगीत रूप की सुंदरता, सद्भाव और भावना की अभिव्यक्ति का उत्पादन करने के लिए मुखर या वाद्य ध्वनियों के संयोजन की कला और विज्ञान।",
    zh_title: "yīn yuè",
    zh_content: "yīn yuè shì yī mén jié hé rén shēng huò lè qì shēng yīn yǐ chǎn shēng xíng tà sù fǎ 、 hé xié hé qíng gǎn biǎo dá de yì shù hé kē xué 。"
});
"""

q2_link_desc = """
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.MUSIC" AND d.name = "description.MUSIC"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MUSIC"}]->(d);
"""

q3_link_parent = """
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.BEAUTY" AND child.name = "topic.MUSIC"
MERGE (parent)-[:HAS_CHILD {name: "edge.BEAUTY->MUSIC"}]->(child);
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
            print("4/4: Linking to Parent TOPIC (topic.BEAUTY)...")
            session.run(q3_link_parent)
            
            print("All statements executed successfully.")

    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)
    finally:
        driver.close()

if __name__ == "__main__":
    execute_queries()
