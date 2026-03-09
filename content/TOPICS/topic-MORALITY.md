---
type: TOPIC
name: "topic.MORALITY"
alias: "Topic: Matters of the Conscience"
parent: "topic.SPIRITUALITY"
en_content: "A doctrine or system of moral conduct."
tags: ["morals", "righteousness", "decency", "virtue", "integrity"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.MORALITY",
		alias: "Topic: Matters of the Conscience", 
		parent: "topic.SPIRITUALITY", 
		tags: ["morals", "righteousness", "decency", "virtue", "integrity"], 
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.MORALITY", 
	en_title: "Topic: Matters of the Conscience", 
	en_content: "A doctrine or system of moral conduct.", 
	es_title: "Tema: Asuntos de conciencia", 
	es_content: "Una doctrina o sistema de conducta moral.", 
	fr_title: "Sujet : Questions de conscience", 
	fr_content: "Une doctrine ou un système de conduite morale.", 
	hi_title: "विषय: अंतरात्मा के मामले", 
	hi_content: "नैतिक आचरण का एक सिद्धांत या प्रणाली।", 
	zh_title: "Zhǔtí: Liángxīn wèntí", 
	zh_content: "dàodé xíngwéi de jiàoyì huò tǐxì."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.MORALITY' AND d.name = 'desc.MORALITY'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MORALITY"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.SPIRITUALITY' AND child.name = 'topic.MORALITY'
MERGE (parent)-[:HAS_CHILD {name: "edge.SPIRITUALITY->MORALITY"}]->(child);

```
