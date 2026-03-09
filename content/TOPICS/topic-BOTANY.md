---
type: TOPIC
name: "topic.BOTANY"
alias: "Topic: Plant Life"
parent: "topic.BIOLOGY"
en_content: "The scientific study of plants—their structure, function, reproduction, evolution, classification, and interactions with the environment."
tags: ["plants", "reproduction", "physiology", "taxonomy", "ecology"]
ptopic: "[[topic-BIOLOGY]]"
level: 5
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.BOTANY",
		alias: "Topic: Plant Life", 
		parent: "topic.BIOLOGY", 
		tags: ["plants", "reproduction", "physiology", "taxonomy", "ecology"], 
		level: 5});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.BOTANY", 
	en_title: "Topic: Plant Life", 
	en_content: "The scientific study of plants—their structure, function, reproduction, evolution, classification, and interactions with the environment.", 
	es_title: "Tema: Vida vegetal",
	es_content: "El estudio científico de las plantas: su estructura, función, reproducción, evolución, clasificación e interacciones con el medio ambiente.", 
	fr_title: "Sujet : La vie végétale", 
	fr_content: "L'étude scientifique des plantes – leur structure, leur fonctionnement, leur reproduction, leur évolution, leur classification et leurs interactions avec l'environnement.", 
	hi_title: "विषय: वनस्पति जीवन", 
	hi_content: "पौधों का वैज्ञानिक अध्ययन - उनकी संरचना, कार्य, प्रजनन, विकास, वर्गीकरण और पर्यावरण के साथ उनकी परस्पर क्रिया।", 
	zh_title: "Zhǔtí: Zhíwù shēnghuó", 
	zh_content: "duì zhíwù jìnxíng kēxué yánjiū de xuékē, bāokuò zhíwù de jiégòu, gōngnéng, fánzhí, jìnhuà, fēnlèi yǐjí yǔ huánjìng de xiānghù zuòyòng."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.BOTANY" AND d.name = "desc.BOTANY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.BOTANY"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.BIOLOGY" AND child.name = "topic.BOTANY"
MERGE (parent)-[:HAS_CHILD {name: "edge.BIOLOGY->BOTANY"}]->(child);

```
