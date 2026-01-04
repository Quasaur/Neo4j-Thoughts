---
name: topic.WISDOM
alias: "Topic: The Application of Knowledge"
type: TOPIC
parent: topic.SPIRITUALITY
tags:
- insight
- discernment
- perception
- understanding
- brilliance
neo4j: true
level: 3
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.WISDOM",
		alias: "Topic: The Application of Knowledge", 
		parent: "topic.SPIRITUALITY", 
		tags: ["insight", "discernment", "perception", "understanding", "brilliance"], 
		notes: "",
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.WISDOM", 
	en_title: "WISDOM", 
	en_content: "A wise attitude, belief, or course of action.", 
	es_title: "Sabiduría", 
	es_content: "Una actitud, creencia o curso de acción sabio.", 
	fr_title: "Sagesse", 
	fr_content: "Une attitude, une croyance ou un plan d’action sage.", 
	hi_title: "बुद्धिमत्ता", 
	hi_content: "एक बुद्धिमान दृष्टिकोण, विश्वास, या कार्यवाही।", 
	zh_title: "Zhìhuì", 
	zh_content: "míngzhì de tàidù, xìnniàn huò xíngdòng fāngzhēn."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.WISDOM" AND d.name = "desc.WISDOM"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.WISDOM"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "topic.WISDOM"
MERGE (parent)-[:HAS_CHILD {name: "edge.CREATION->WISDOM"}]->(child)
RETURN *;

```
