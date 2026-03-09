---
type: TOPIC
name: "topic.SPIRITUALITY"
alias: "Topic: Godliness"
parent: "topic.THE GODHEAD"
en_content: "Sensitivity or attachment to the values of the Holy Spirit of God."
tags: ["attitude", "transcendence", "metaphysical", "supernatural", "breathless"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.SPIRITUALITY",
		alias: "Topic: Godliness", 
		parent: "topic.THE GODHEAD", 
		tags: ["attitude", "transcendence", "metaphysical", "supernatural", "breathless"], 
		level: 3
	});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.SPIRITUALITY", 
	en_title: "Topic: Godliness", 
	en_content: "Sensitivity or attachment to the values of the Holy Spirit of God.", 
	es_title: "Tema: La piedad", 
	es_content: "Sensibilidad o apego a los valores del Espíritu Santo de Dios.", 
	fr_title: "Sujet : La piété", 
	fr_content: "Sensibilité ou attachement aux valeurs du Saint-Esprit de Dieu.", 
	hi_title: "विषय: ईश्वरभक्ति", 
	hi_content: "ईश्वर की पवित्र आत्मा के मूल्यों के प्रति संवेदनशीलता या लगाव।", 
	zh_title: "zhǔ tí ：jìng qián", 
	zh_content: "duì shàngdì shènglíng jiàzhíguān de mǐngǎn huò yīliàn."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.SPIRITUALITY" AND d.name = "desc.SPIRITUALITY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.SPIRITUALITY"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.SPIRITUALITY"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->SPIRITUALITY"}]->(child);

```
