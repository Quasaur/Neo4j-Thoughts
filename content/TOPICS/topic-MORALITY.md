---
name: topic.MORALITY
alias: "Topic: Matters of the Conscience"
type: TOPIC
parent: topic.SPIRITUALITY
tags:
- morals
- righteousness
- decency
- virtue
- integrity
neo4j: true
level: 3
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.MORALITY",
		alias: "Topic: Matters of the Conscience", 
		parent: "topic.SPIRITUALITY", 
		tags: ["morals", "righteousness", "decency", "virtue", "integrity"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.MORALITY", 
	en_title: "MORALITY", 
	en_content: "A doctrine or system of moral conduct.", 
	es_title: "Moralidad", 
	es_content: "Una doctrina o sistema de conducta moral.", 
	fr_title: "Moralité", 
	fr_content: "Une doctrine ou un système de conduite morale.", 
	hi_title: "नैतिकता", 
	hi_content: "नैतिक आचरण का एक सिद्धांत या प्रणाली।", 
	zh_title: "Dàodé", 
	zh_content: "dàodé xíngwéi de jiàoyì huò tǐxì."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.MORALITY' AND d.name = 'desc.MORALITY'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MORALITY"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.SPIRITUALITY' AND child.name = 'topic.MORALITY'
MERGE (parent)-[:HAS_CHILD {name: "edge.SPIRITUALITY->MORALITY"}]->(child)
RETURN *;

```
