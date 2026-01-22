---
name: "topic.BOTANY"
alias: "Topic: Plant Life"
type: TOPIC
parent: "topic.BIOLOGY"
en_content: "The scientific study of plants—their structure, function, reproduction, evolution, classification, and interactions with the environment."
tags:
- plants
- reproduction
- physiology
- taxonomy
- ecology
neo4j: true
ptopic: "[[topic-BIOLOGY]]"
level: 7
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.BOTANY",
		alias: "Topic: Plant Life", 
		parent: "topic.BIOLOGY", 
		tags: ["plants", "reproduction", "physiology", "taxonomy", "cology"], 
		level: 7});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.BOTANY", 
	en_title: "Botany", 
	en_content: "The scientific study of plants—their structure, function, reproduction, evolution, classification, and interactions with the environment.", 
	es_title: "Botánica",
	es_content: "El estudio científico de las plantas: su estructura, función, reproducción, evolución, clasificación e interacciones con el medio ambiente.", 
	fr_title: "Botanique", 
	fr_content: "L'étude scientifique des plantes – leur structure, leur fonctionnement, leur reproduction, leur évolution, leur classification et leurs interactions avec l'environnement.", 
	hi_title: "वनस्पति विज्ञान", 
	hi_content: "पौधों का वैज्ञानिक अध्ययन - उनकी संरचना, कार्य, प्रजनन, विकास, वर्गीकरण और पर्यावरण के साथ उनकी परस्पर क्रिया।", 
	zh_title: "Zhíwù xué", 
	zh_content: "duì zhíwù jìnxíng kēxué yánjiū de xuékē, bāokuò zhíwù de jiégòu, gōngnéng, fánzhí, jìnhuà, fēnlèi yǐjí yǔ huánjìng de xiānghù zuòyòng."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.BOTANY" AND d.name = "desc.BOTANY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.BOTANY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.BIOLOGY" AND child.name = "topic.BOTANY"
MERGE (parent)-[:HAS_CHILD {name: "edge.BIOLOGY->BOTANY"}]->(child)
RETURN *;

```
