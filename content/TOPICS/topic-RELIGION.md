---
name: topic.RELIGION
alias: "Topic: Humanity's Attempt to Grasp and Manipulate The Transcendent One"
type: TOPIC
parent: topic.MORALITY
tags:
- cult
- paganism
- sect
- ritual
- superstition
neo4j: true
level: 4
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.RELIGION",
		alias: "Topic: Humanity's Attempt to Grasp and Manipulate The Transcendent One", 
		parent: "topic.MORALITY", 
		tags: ["cult", "paganism", "sect", "ritual", "superstition"], 
		notes: "",
		level: 4});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.RELIGION", 
	en_title: "RELIGION", 
	en_content: "A personal or institutionalized system of religious attitudes, beliefs, and practices.", 
	es_title: "Religión", 
	es_content: "Un système personnel ou institutionnalisé d’attitudes, de croyances et de pratiques religieuses.", 
	fr_title: "Religion", 
	fr_content: "Une compréhension mentale de la vérité ou un accord entre des individus ou des groupes.", 
	hi_title: "धर्म",
	hi_content: "धार्मिक दृष्टिकोणों, विश्वासों और प्रथाओं की एक व्यक्तिगत या संस्थागत प्रणाली।",
	zh_title: "Zōngjiào",
	zh_content: "gèrén huò zhìdù huà de zōngjiào tàidù, xìnyǎng hé shíjiàn tǐxì."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.RELIGION' AND d.name = 'desc.RELIGION'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.RELIGION"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.MORALITY' AND child.name = 'topic.RELIGION'
MERGE (parent)-[:HAS_CHILD {name: "edge.MORALITY->RELIGION"}]->(child)
RETURN *;

```
