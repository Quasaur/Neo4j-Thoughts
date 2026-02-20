---
name: topic.GUILT
alias: "Topic: Guilt - The Instrument of Law & Religion"
type: TOPIC
parent: topic.RELIGION
tags:
- responsibility
- transgression
- condemnation
- repentance
- atonement
neo4j: false
ptopic: "[[topic-RELIGION]]"
level: 5
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {
	    name: "topic.GUILT",
		alias: "Topic: Guilt - The Instrument of Law & Religion", 
		parent: "topic.RELIGION", 
		tags: ["responsibility", "transgression", "condemnation", "repentance", "atonement"],
		level: 5
		});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.GUILT", 
	en_title: "Guilt", 
	en_content: "A feeling of responsibility for wrongdoing; a courtroom conviction.", 
	es_title: "Culpa", 
	es_content: "Sentimiento de responsabilidad por haber cometido una falta; una condena judicial.", 
	fr_title: "Culpabilité", 
	fr_content: "Un sentiment de responsabilité pour une faute commise ; une condamnation par un tribunal.", 
	hi_title: "दोष",
	hi_content: "गलत काम के लिए ज़िम्मेदारी का एहसास; कोर्ट में सज़ा मिलना।",
	zh_title: "Zuì'è gǎn",
	zh_content: "duì zìjǐ de cuòwù xíngwéi gǎndào nèijiù; fǎtíng shàng de dìngzuì."
	});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = 'topic.GUILT' AND d.name = 'desc.GUILT'
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.GUILT"}]->(d)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = 'topic.RELIGION' AND child.name = 'topic.GUILT'
MERGE (parent)-[:HAS_CHILD {name: "edge.RELIGION->GUILT"}]->(child)
RETURN *;

```
