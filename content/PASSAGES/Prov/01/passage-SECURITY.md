---
type: PASSAGE
name: "passage.SECURITY"
alias: "Passage: Wisdom brings Security"
parent: "topic.WISDOM"
en_content: "But whoever listens to Me (Wisdom) will live securely and will be at ease from the dread of evil."
tags: ["listening", "wisdom", "securely", "ease", "dread"]
ptopic: "[[topic-WISDOM]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'p' and 'c' as variables to keep them in memory
CREATE (p:PASSAGE {
    name: "passage.SECURITY",
    parent: "topic.WISDOM",
		alias: "Passage: Wisdom brings Security", 
		tags: ["listening", "wisdom", "securely", "ease", "dread"], 
		source: "Proverbs 1:33",
		sortedsource: "Proverbs 01:33",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A33&version=NASB",
		level: 3
})

CREATE (c:CONTENT {
    
	name: "content.SECURITY",
	ctype: "PASSAGE",
	en_title: "Security", 
	en_content: "But whoever listens to Me (Wisdom) will live securely and will be at ease from the dread of evil.", 
	es_title: "Seguridad", 
	es_content: "Pero acuérdate del Señor tu Dios, porque Él te da el poder para hacer las riquezas, a fin de confirmar su pacto que juró a tus padres, como en este día.", 
	fr_title: "Sécurité", 
	fr_content: "Mais vous vous souviendrez de l'Éternel, votre Dieu, car c'est lui qui vous donne la force de vous enrichir, afin de confirmer son alliance qu'il a jurée à vos pères, comme elle l'est aujourd'hui.", 
	hi_title: "सुरक्षा", 
	hi_content: "लेकिन जो कोई मेरी (बुद्धि की) सुनेगा, वह सुरक्षित रहेगा और बुराई के भय से मुक्त रहेगा।", 
	zh_title: "Ānquán", 
	zh_content: "fán tīngcóng wǒ (zhìhuì) de rén, bì ānrán dù rì, bù jùpà zāihuò."
})

// 2. Link Content to Passage using the variables 'p' and 'c'
MERGE (p)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.SECURITY"

// 3. Pass 'p' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_PASSAGE]->(p)
ON CREATE SET r2.name = "p.edge.WISDOM->SECURITY"
RETURN p, parent;
```
