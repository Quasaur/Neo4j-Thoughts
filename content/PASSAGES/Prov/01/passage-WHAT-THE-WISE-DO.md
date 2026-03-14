---
type: PASSAGE
name: "passage.WHAT THE WISE DO"
alias: "Passage: Wisdom Brings Growth"
parent: "topic.UNDERSTANDING"
en_content: "A wise person will hear and increase in learning, and a person of understanding will acquire wise counsel."
tags: ["wise", "listening", "learning", "collecting", "counsel"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'p' and 'c' as variables to keep them in memory
CREATE (p:PASSAGE {
    name: "passage.WHAT THE WISE DO",
    parent: "topic.UNDERSTANDING",
		alias: "Passage: Wisdom Brings Growth", 
		tags: ["wise", "listening", "learning", "collecting", "counsel"], 
		source: "Proverbs 1:5",
		sortedsource: "Proverbs 01:05",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A5&version=NASB",
		level: 3
})

CREATE (c:CONTENT {
    
	name: "content.WHAT THE WISE DO",
	ctype: "PASSAGE",
	en_title: "What the Wise Do", 
	en_content: "A wise person will hear and increase in learning, and a person of understanding will acquire wise counsel.", 
	es_title: "Lo que hacen los sabios", 
	es_content: "El sabio oirá y aumentará su conocimiento, y el entendido adquirirá consejo sabio.", 
	fr_title: "Ce que font les sages", 
	fr_content: "L’homme sage entendra et grandira en connaissance, et l’homme intelligent acquerra de sages conseils.", 
	hi_title: "बुद्धिमान क्या करते हैं", 
	hi_content: "बुद्धिमान व्यक्ति सुनेगा और अपनी शिक्षा बढ़ाएगा, और समझदार व्यक्ति बुद्धिमानी भरी सलाह ग्रहण करेगा।", 
	zh_title: "Zhìzhě zhī dào", 
	zh_content: "zhìzhě shànyú qīngtīng, zēngzhǎng xuéshì; tōngdá rén néng huòdé míngzhì de jiànyì."
})

// 2. Link Content to Passage using the variables 'p' and 'c'
MERGE (p)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.WHAT THE WISE DO"

// 3. Pass 'p' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MERGE (parent)-[r2:HAS_PASSAGE]->(p)
ON CREATE SET r2.name = "p.edge.UNDERSTANDING->WHAT THE WISE DO"
RETURN p, parent;
```
