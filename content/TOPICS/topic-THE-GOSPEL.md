---
name: "topic.THE GOSPEL"
alias: "Topic: The Good News"
type: TOPIC
parent: "topic.THE GODHEAD"
tags:
- evangel
- good_news
- jesus
- salvation
- redemption
neo4j: true
ptopic: "[[topic-THE]]"
level: 2
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.THE GOSPEL",
		alias: "Topic: The Good News", 
		parent: "topic.THE GODHEAD", 
		tags: ["evangel", "good_news", "jesus", "salvation", "redemption"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.THE GOSPEL", 
	en_title: "THE GOSPEL", 
	en_content: "The Life, Death, Burial, Resurrection, Ascension and Return of Jesus Christ.", 
	es_title: "EL EVANGELIO", 
	es_content: "Vida, Muerte, Sepultura, Resurrección, Ascensión y Regreso de Jesucristo.", 
	fr_title: "L'ÉVANGILE", 
	fr_content: "La vie, la mort, l'ensevelissement, la résurrection, l'ascension et le retour de Jésus-Christ.", 
	hi_title: "सुसमाचार", 
	hi_content: "यीशु मसीह का जीवन, मृत्यु, दफ़न, पुनरुत्थान, स्वर्गारोहण और वापसी।", 
	zh_title: "Fúyīn", 
	zh_content: "yēsū jīdū de shēngpíng, sǐwáng, máizàng, fùhuó, shēngtiān hé zàilái."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.THE GOSPEL" AND d.name = "desc.THE GOSPEL"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.The Gospel"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.THE GOSPEL"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->THE GOSPEL"}]->(child)
RETURN *;

```
