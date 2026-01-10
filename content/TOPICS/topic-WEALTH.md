---
name: topic.WEALTH
alias: "Topic: Abundance"
type: TOPIC
parent: topic.CREATION
tags:
- assets
- capital
- fortune
- resources
- riches
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 3
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.WEALTH",
		alias: "Topic: Abundance", 
		parent: "topic.CREATION", 
		tags: ["assets", "capital", "fortune", "resources", "riches"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.WEALTH", 
	en_title: "WEALTH", 
	en_content: "The abundance of valuable material, possessions or resources.", 
	es_title: "Riqueza", 
	es_content: "La abundancia de materiales, posesiones o recursos valiosos.", 
	fr_title: "Richesse", 
	fr_content: "L'abondance de biens matériels, de possessions ou de ressources de valeur.", 
	hi_title: "मधन", 
	hi_content: "मूल्यवान सामग्री, संपत्ति या संसाधनों की प्रचुरता।", 
	zh_title: "Cáifù", 
	zh_content: "fēngfù de bǎoguì wùzhí, cáichǎn huò zīyuán."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.WEALTH" AND d.name = "desc.WEALTH"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.WEALTH"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.CREATION" AND child.name = "topic.WEALTH"
MERGE (parent)-[:HAS_CHILD {name: "edge.CREATION->WEALTH"}]->(child)
RETURN *;

```
