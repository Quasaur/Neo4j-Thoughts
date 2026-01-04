---
name: topic.TRUTH
alias: "Topic: The Divine Being"
type: TOPIC
parent: "topic.THE GODHEAD"
tags:
- actuality
- reality
- fact
- verity
- authentic
neo4j: true
level: 2
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.TRUTH",
		alias: "Topic: The Divine Being", 
		parent: "topic.THE GODHEAD", 
		tags: ["actuality", "reality", "fact", "authentic", "verity"], 
		notes: "",
		level: 2});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.TRUTH", 
	en_title: "TRUTH", 
	en_content: "A transcendent fundamental or spiritual reality.", 
	es_title: "VERDAD", 
	es_content: "Una realidad fundamental o espiritual trascendente.", 
	fr_title: "VÉRITÉ", 
	fr_content: "Une réalité fondamentale ou spirituelle transcendante.", 
	hi_title: "सत्य", 
	hi_content: "एक पारलौकिक मौलिक या आध्यात्मिक वास्तविकता।", 
	zh_title: "Zhēnlǐ", 
	zh_content: "chāoyuè de gēnběn huò jīngshén xiànshí."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.TRUTH" AND d.name = "desc.TRUTH"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.Truth"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.TRUTH"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->TRUTH"}]->(child)
RETURN *;

```
