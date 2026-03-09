---
type: TOPIC
name: "topic.UNDERSTANDING"
alias: "Topic: Comprehension"
parent: "topic.SPIRITUALITY"
en_content: "A mental grasp of truth or an agreement between individuals or groups."
tags: ["comprehension", "mental", "grasp", "agreement", "ascertain"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.UNDERSTANDING",
		alias: "Topic: Comprehension", 
		parent: "topic.SPIRITUALITY", 
		tags: ["comprehension", "mental", "grasp", "agreement", "ascertain"], 
		level: 3});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.UNDERSTANDING", 
	en_title: "Topic: Comprehension", 
	en_content: "A mental grasp of truth or an agreement between individuals or groups.", 
	es_title: "Tema: Comprensión", 
	es_content: "Una comprensión mental de la verdad o un acuerdo entre individuos o grupos.", 
	fr_title: "Sujet : Compréhension", 
	fr_content: "Une compréhension mentale de la vérité ou un accord entre des individus ou des groupes.", 
	hi_title: "विषय: समझ", 
	hi_content: "सत्य की मानसिक समझ या व्यक्तियों या समूहों के बीच सहमति।", 
	zh_title: "zhǔ tí ： lǐ jiě", 
	zh_content: "duì zhēnlǐ de xīnlǐ bǎwò, huò gèrén huò qúntǐ zhī jiān de gòngshì."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.UNDERSTANDING' AND d.name = 'desc.UNDERSTANDING'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.UNDERSTANDING"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.SPIRITUALITY' AND child.name = 'topic.UNDERSTANDING'
MERGE (parent)-[:HAS_CHILD {name: "edge.SPIRITUALITY->UNDERSTANDING"}]->(child);

```
