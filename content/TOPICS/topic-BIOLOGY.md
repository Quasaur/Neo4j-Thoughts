---
name: "topic.BIOLOGY"
alias: "Topic: Living Matter"
type: TOPIC
parent: "topic.NATURAL SCIENCES"
en_content: "A branch of knowledge that deals with living organisms and vital processes."
tags:
- matter
- energy
- life
- spirit
- knowledge
neo4j: true
ptopic: "[[topic-NATURAL-SCIENCES]]"
level: 6
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.BIOLOGY",
		alias: "Topic: Living Matter", 
		parent: "topic.NATURAL SCIENCES", 
		tags: ["matter", "energy", "life", "spirit", "knowledge"], 
		level: 6});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.BIOLOGY", 
	en_title: "Biology", 
	en_content: "A branch of knowledge that deals with living organisms and vital processes.", 
	es_title: "Biología",
	es_content: "Una rama del conocimiento que se ocupa de los organismos vivos y los procesos vitales.", 
	fr_title: "Biologie", 
	fr_content: "Une branche du savoir qui traite des organismes vivants et des processus vitaux.", 
	hi_title: "जीव विज्ञान", 
	hi_content: "कज्ञान की एक शाखा जो जीवित जीवों और महत्वपूर्ण प्रक्रियाओं से संबंधित है।", 
	zh_title: "Shēngwù xué", 
	zh_content: "yī mén yánjiūshēng wùtǐ hé shēngmìng guòchéng de xuékē."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.BIOLOGY" AND d.name = "desc.BIOLOGY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.BIOLOGY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.NATURAL SCIENCES" AND child.name = "topic.BIOLOGY"
MERGE (parent)-[:HAS_CHILD {name: "edge.NATURAL SCIENCES->BIOLOGY"}]->(child)
RETURN *;

```
