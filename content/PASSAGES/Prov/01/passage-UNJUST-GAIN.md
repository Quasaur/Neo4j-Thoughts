---
type: PASSAGE
name: "passage.UNJUST GAIN"
alias: "Passage: Cheating is Deadly"
parent: "topic.WEALTH"
en_content: "Such are the ways of everyone who makes unjust gain; it takes away the life of its possessors."
tags: ["gain", "greed", "unjust", "death", "just"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'p' and 'c' as variables to keep them in memory
CREATE (p:PASSAGE {
    name: "passage.UNJUST GAIN",
    parent: "topic.WEALTH",
		alias: "Passage: Cheating is Deadly", 
		tags: ["gain", "greed", "unjust", "death", "just"], 
		source: "Proverbs 1:19",
		sortedsource: "Proverbs 01:19",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A19&version=NASBNASB",
		level: 3
})

CREATE (c:CONTENT {
    
	name: "content.UNJUST GAIN",
	ctype: "PASSAGE",
	en_title: "Unjust Gain", 
	en_content: "Such are the ways of everyone who makes unjust gain; it takes away the life of its possessors.", 
	es_title: "Ganancia injusta", 
	es_content: "Así procede todo el que obtiene ganancia injusta: quita la vida a sus poseedores.", 
	fr_title: "Gain injuste", 
	fr_content: "Telles sont les voies de quiconque se livre à un gain injuste : il enlève la vie à ceux qui le possèdent.", 
	hi_title: "अन्यायपूर्ण लाभ", 
	hi_content: "जो लोग अन्यायपूर्ण लाभ कमाते हैं, उनके तरीके ऐसे ही होते हैं; यह अपने मालिकों के जीवन को छीन लेता है।", 
	zh_title: "Bù yì zhī cái", 
	zh_content: "fán móuqǔ bù yì zhī cái de rén, dōu shì rúcǐ xíngjìng; bù yì zhī cái duó qùle yǒngyǒu zhě de shēngmìng."
})

// 2. Link Content to Passage using the variables 'p' and 'c'
MERGE (p)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.UNJUST GAIN"

// 3. Pass 'p' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MERGE (parent)-[r2:HAS_PASSAGE]->(p)
ON CREATE SET r2.name = "p.edge.WEALTH->UNJUST GAIN"
RETURN p, parent;
```
