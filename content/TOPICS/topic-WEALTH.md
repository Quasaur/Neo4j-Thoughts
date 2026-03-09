---
type: TOPIC
name: "topic.WEALTH"
alias: "Topic: Abundance"
parent: "topic.CREATION"
en_content: "The abundance of valuable material, possessions or resources."
tags: ["assets", "capital", "fortune", "resources", "riches"]
ptopic: "[[topic-CREATION]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.WEALTH",
		alias: "Topic: Abundance", 
		parent: "topic.CREATION", 
		tags: ["assets", "capital", "fortune", "resources", "riches"], 
		level: 3
		});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.WEALTH", 
	en_title: "Topic: Abundance", 
	en_content: "The abundance of valuable material, possessions or resources.", 
	es_title: "Tema: Abundancia", 
	es_content: "La abundancia de materiales, posesiones o recursos valiosos.", 
	fr_title: "Sujet : L'abondance", 
	fr_content: "L'abondance de biens matériels, de possessions ou de ressources de valeur.", 
	hi_title: "विषय: बहुतायत", 
	hi_content: "मूल्यवान सामग्री, संपत्ति या संसाधनों की प्रचुरता।", 
	zh_title: "Zhǔtí: Fēngshèng", 
	zh_content: "fēngfù de bǎoguì wùzhí, cáichǎn huò zīyuán."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.WEALTH" AND d.name = "desc.WEALTH"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.WEALTH"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.CREATION" AND child.name = "topic.WEALTH"
MERGE (parent)-[:HAS_CHILD {name: "edge.CREATION->WEALTH"}]->(child);

```
