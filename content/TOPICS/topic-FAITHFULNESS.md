---
type: TOPIC
name: "topic.FAITHFULNESS"
alias: "Topic: Steadfastness"
parent: "topic.THE GODHEAD"
en_content: "Adherence to something to which one is bound by a pledge or duty."
tags: ["commitment", "fidelity", "steadfastness", "reliability", "dependability"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 3
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.FAITHFULNESS",
		alias: "Topic: Steadfastness", 
		parent: "topic.THE GODHEAD", 
		tags: ["commitment", "fidelity", "steadfastness", "reliability", "dependability"], 
		level: 3
	});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.FAITHFULNESS", 
	en_title: "Topic: Steadfastness", 
	en_content: "Adherence to something to which one is bound by a pledge or duty.", 
	es_title: "Tema: Firmeza", 
	es_content: "Adherencia a algo a lo que uno está obligado por una promesa o deber.", 
	fr_title: "Sujet : La fermeté", 
	fr_content: "Adhésion à quelque chose à laquelle on est lié par un engagement ou un devoir.", 
	hi_title: "विषय: दृढ़ता", 
	hi_content: "किसी ऐसी चीज़ का पालन करना जिसके प्रति कोई प्रतिज्ञा या कर्तव्य से बंधा हो।", 
	zh_title: "zhǔ tí ：jiān dìng", 
	zh_content: "jiānshǒu chéngnuò huò yìwù suǒ yuēshù de shìwù."
});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.FAITHFULNESS" AND d.name = "desc.FAITHFULNESS"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.FAITHFULNESS"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.FAITHFULNESS"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->FAITHFULNESS"}]->(child);

```
