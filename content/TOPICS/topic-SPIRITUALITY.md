---
name: topic.SPIRITUALITY
alias: "Topic: Godliness"
type: TOPIC
parent: "topic.THE GODHEAD"
tags:
- attitude
- transcendence
- metaphysical
- supernatural
- breathless
neo4j: true
level: 2
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.SPIRITUALITY",
		alias: "Topic: Godliness", 
		parent: "topic.THE GODHEAD", 
		tags: ["breath", "atitude", "transcendence", "metaphysical", "supernatural"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.SPIRITUALITY", 
	en_title: "SPIRITUALITY", 
	en_content: "Sensitivity or attachment to the values of the Holy Spirit of God.", 
	es_title: "ESPIRITUALIDAD", 
	es_content: "Sensibilidad o apego a los valores del Espíritu Santo de Dios.", 
	fr_title: "SPIRITUALITÉ", 
	fr_content: "Sensibilité ou attachement aux valeurs du Saint-Esprit de Dieu.", 
	hi_title: "आध्यात्मिकता", 
	hi_content: "ईश्वर की पवित्र आत्मा के मूल्यों के प्रति संवेदनशीलता या लगाव।", 
	zh_title: "Língxìng", 
	zh_content: "duì shàngdì shènglíng jiàzhíguān de mǐngǎn huò yīliàn."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.SPIRITUALITY" AND d.name = "desc.SPIRITUALITY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.Spirituality"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.SPIRITUALITY"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->SPIRITUALITY"}]->(child)
RETURN *;

```
