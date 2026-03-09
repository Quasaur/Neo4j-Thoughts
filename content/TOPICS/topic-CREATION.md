---
type: TOPIC
name: "topic.CREATION"
alias: "Topic: The Universe"
parent: "topic.THE GODHEAD"
en_content: "All beings, places and things that exist apart from The GODHEAD as a result of Divine Creation."
tags: ["creation", "cosmos", "universe", "dominion", "kingdom"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
verified: true
---

```Cypher
//create the TOPIC with the same fields as a normal topic
CREATE (t:TOPIC
    {	    name: "topic.CREATION",
		alias: "Topic: The Universe", 
		parent: "topic.THE GODHEAD", 
		tags: ["creation", "cosmos", "universe", "dominion", "kingdom"], 
		level: 1});
// create multi-lingual description		
CREATE (d:DESCRIPTION {
	name: "desc.CREATION", 
	en_title: "Topic: The Universe", 
	en_content: "All beings, places and things that exist apart from The GODHEAD as a result of Divine Creation.", 
	es_title: "Tema: El universo", 
	es_content: "Todos los seres, lugares y cosas que existen aparte de La DEIDAD como resultado de la Creación Divina.", 
	fr_title: "Sujet : L'Univers", 
	fr_content: "Tous les êtres, lieux et choses qui existent en dehors de la DIVINITÉ, résultat de la Création Divine.", 
	hi_title: "विषय: ब्रह्मांड", 
	hi_content: "ईश्वर के बाहर मौजूद सभी प्राणी, स्थान और चीज़ें ईश्वरीय सृष्टि का परिणाम हैं।", 
	zh_title: "zhǔ tí ： yǔ zhòu", 
	zh_content: "zuò wéi shén shèng chuàng zào de jié guǒ , chú le shén tóu zhī wài ér cún zài de suǒ yǒu cún zài 、 dì diǎn hé shì wù ."});
// link description to node
MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.CREATION" AND d.name = "desc.CREATION"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.CREATION"}]->(d);
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "topic.CREATION"
MERGE (parent)-[:HAS_CHILD {name: "edge.THE GODHEAD->CREATION"}]->(child);

```
