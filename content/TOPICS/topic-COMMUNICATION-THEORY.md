---
name: "topic.COMMUNICATION THEORY"
alias: "Topic: Mankind"
type: TOPIC
en_content: "A systematic, interdisciplinary study of how information is created, encoded, transmitted, received, and interpreted across human, technological, and symbolic systems."
parent: topic.HUMANITY
tags:
  - information
  - context
  - encoding
  - transmission
  - interpretation
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.COMMUNICATION THEORY",
		alias: "Topic: Information Sharing", 
		parent: "topic.HUMANITY", 
		tags: ["iknformation", "context", "encoding", "transmission", "interpretation"], 
		level: 4});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.COMMUNICATION THEORY", 
	en_title: "Communication Theory", 
	en_content: "A systematic, interdisciplinary study of how information is created, encoded, transmitted, received, and interpreted across human, technological, and symbolic systems.", 
	es_title: "Teoría de la comunicación", 
	es_content: "Un estudio sistemático e interdisciplinario de cómo se crea, codifica, transmite, recibe e interpreta la información a través de sistemas humanos, tecnológicos y simbólicos.", 
	fr_title: "Théorie de la communication", 
	fr_content: "Une étude systématique et interdisciplinaire de la manière dont l'information est créée, codée, transmise, reçue et interprétée à travers les systèmes humains, technologiques et symboliques.", 
	hi_title: "कम्युनिकेशन थ्योरी", 
	hi_content: "यह एक सिस्टमैटिक, इंटरडिसिप्लिनरी स्टडी है कि इंसानी, टेक्नोलॉजिकल और सिंबॉलिक सिस्टम में जानकारी कैसे बनाई जाती है, एन्कोड की जाती है, भेजी जाती है, रिसीव की जाती है और समझी जाती है।", 
	zh_title: "Chuánbò lǐlùn", 
	zh_content: "zhè shì yī mén xìtǒng xìng de kuà xuékē yánjiū, tàntǎo xìnxī rúhé zài rénlèi xìtǒng, jìshù xìtǒng hé fúhào xìtǒng zhōng bèi chuàngzào, biānmǎ, chuánshū, jiēshōu hé jiědú."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.COMMUNICATION THEORY" AND d.name = "desc.COMMUNICATION THEORY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.COMMUNICATION THEORY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.HUMANITY" AND child.name = "topic.COMMUNICATION THEORY"
MERGE (parent)-[:HAS_CHILD {name: "edge.HUMANITY->COMMUNICATION THEORY"}]->(child)
RETURN *;

```
