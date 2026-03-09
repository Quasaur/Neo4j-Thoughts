---
type: TOPIC
name: "topic.WISDOM"
alias: "Topic: The Application of Knowledge"
parent: "topic.SPIRITUALITY"
en_content: "A wise attitude, belief, or course of action."
tags: ["insight", "discernment", "perception", "understanding", "brilliance"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.WISDOM",
		alias: "Topic: The Application of Knowledge", 
		parent: "topic.SPIRITUALITY", 
		tags: ["insight", "discernment", "perception", "understanding", "brilliance"], 
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.WISDOM", 
	en_title: "Topic: The Application of Knowledge", 
	en_content: "A wise attitude, belief, or course of action.", 
	es_title: "Tema: La aplicación del conocimiento", 
	es_content: "Una actitud, creencia o curso de acción sabio.", 
	fr_title: "Sujet : L'application des connaissances", 
	fr_content: "Une attitude, une croyance ou un plan d’action sage.", 
	hi_title: "विषय: ज्ञान का अनुप्रयोग", 
	hi_content: "एक बुद्धिमान दृष्टिकोण, विश्वास, या कार्यवाही।", 
	zh_title: "zhǔ tí ： zhī shí de yìng yòng", 
	zh_content: "míngzhì de tàidù, xìnniàn huò xíngdòng fāngzhēn."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.WISDOM" AND d.name = "desc.WISDOM"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.WISDOM"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "topic.WISDOM"
MERGE (parent)-[:HAS_CHILD {name: "edge.SPIRITUALITY->WISDOM"}]->(child);

```
