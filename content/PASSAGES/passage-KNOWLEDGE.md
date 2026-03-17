---
type: PASSAGE
name: "passage.KNOWLEDGE"
alias: "Passage: God's Existence as the Foundation of Education"
parent: "topic.HUMANITY"
sortedsource: "Proverbs 01:07"
en_content: "The fear of the LORD is the beginning of knowledge; fools despise wisdom and instruction."
tags: ["godly_fear", "beginning", "knowledge", "fools", "instruction"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.KNOWLEDGE",
    parent: "topic.HUMANITY",
		alias: "Passage: God's Existence as the Foundation of Education", 
		tags: ["godly_fear", "beginning", "knowledge", "fools", "instruction"], 
		source: "Proverbs 1:7",
		sortedsource: "Proverbs 01:07",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A7&version=NASB",
		level: 3
})

CREATE (c:CONTENT {
    name: "content.KNOWLEDGE", 
	ctype: "PASSAGE",
	en_title: "Passage: God's Existence as the Foundation of Education",
	en_content: "The fear of the LORD is the beginning of knowledge; fools despise wisdom and instruction.", 
	es_title: "Pasaje: La existencia de Dios como fundamento de la educación", 
	es_content: "El temor del SEÑOR es el principio del conocimiento; los necios desprecian la sabiduría y la instrucción.", 
	fr_title: "Passage : L'existence de Dieu comme fondement de l'éducation", 
	fr_content: "La crainte de l’Éternel est le commencement de la science ; les insensés méprisent la sagesse et l’instruction.", 
	hi_title: "परिच्छेद: शिक्षा की नींव के रूप में ईश्वर का अस्तित्व", 
	hi_content: "प्रभु का भय ज्ञान की शुरुआत है; मूर्ख लोग ज्ञान और शिक्षा को तुच्छ समझते हैं।", 
	zh_title: "jīng wén : shàng dì de cún zài shì jiào yù de jī chǔ", 
	zh_content: "jìngwèi yēhéhuá shì zhīshì de kāiduān; yúwàng rén miǎoshì zhìhuì hé xùnhuì."
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.KNOWLEDGE"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.HUMANITY->KNOWLEDGE"
RETURN b, parent;
```
