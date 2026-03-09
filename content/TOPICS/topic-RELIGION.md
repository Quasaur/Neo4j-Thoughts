---
type: TOPIC
name: "topic.RELIGION"
alias: "Topic: Humanity's Attempt to Manipulate God"
parent: "topic.MORALITY"
en_content: "A personal or institutionalized system of religious attitudes, beliefs, and practices."
tags: ["cult", "paganism", "sect", "ritual", "superstition"]
ptopic: "[[topic-MORALITY]]"
level: 4
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.RELIGION",
		alias: "Topic: Humanity's Attempt to Manipulate God", 
		parent: "topic.MORALITY", 
		tags: ["cult", "paganism", "sect", "ritual", "superstition"], 
		level: 4
	});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.RELIGION", 
	en_title: "Topic: Humanity's Attempt to Manipulate God", 
	en_content: "A personal or institutionalized system of religious attitudes, beliefs, and practices.", 
	es_title: "Tema: El intento de la humanidad de manipular a Dios", 
	es_content: "Un sistema personal o institucionalizado de actitudes, creencias y prácticas religiosas.", 
	fr_title: "Sujet : La tentative de l'humanité de manipuler Dieu", 
	fr_content: "Un système personnel ou institutionnalisé d’attitudes, de croyances et de pratiques religieuses.", 
	hi_title: "विषय: इंसानियत की भगवान को मैनिपुलेट करने की कोशिश",
	hi_content: "धार्मिक दृष्टिकोणों, विश्वासों और प्रथाओं की एक व्यक्तिगत या संस्थागत प्रणाली।",
	zh_title: "Zhǔtí: Rénlèi shìtú cāozòng shàngdì",
	zh_content: "gèrén huò zhìdù huà de zōngjiào tàidù, xìnyǎng hé shíjiàn tǐxì."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.RELIGION' AND d.name = 'desc.RELIGION'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.RELIGION"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.MORALITY' AND child.name = 'topic.RELIGION'
MERGE (parent)-[:HAS_CHILD {name: "edge.MORALITY->RELIGION"}]->(child);

```
