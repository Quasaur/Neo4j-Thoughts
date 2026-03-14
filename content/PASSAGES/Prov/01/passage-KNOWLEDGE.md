---
type: PASSAGE
name: "passage.KNOWLEDGE"
alias: "Passage: God's Existence as the Foundation of Education"
parent: "topic.HUMANITY"
en_content: "The fear of the LORD is the beginning of knowledge; fools despise wisdom and instruction."
tags: ["fear_of_the_lord", "beginning", "knowledge", "fools", "instruction"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.KNOWLEDGE",
    parent: "topic.HUMANITY",
		alias: "Passage: God's Existence as the Foundation of Education", 
		tags: ["fear_of_the_lord", "beginning", "knowledge", "fools", "instruction"], 
		source: "Proverbs 1:7",
		sortedsource: "Proverbs 01:07",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A7&version=NASB",
		level: 3
})

CREATE (c:CONTENT {
    
    
	name: "content.KNOWLEDGE", 
	ctype: "PASSAGE",
	en_title: "Knowledge", 
	en_content: "The fear of the LORD is the beginning of knowledge; fools despise wisdom and instruction.", 
	es_title: "CONOCIMIENTO", 
	es_content: "El temor del SEÑOR es el principio del conocimiento; los necios desprecian la sabiduría y la instrucción.", 
	fr_title: "CONNAISSANCE", 
	fr_content: "La crainte de l’Éternel est le commencement de la science ; les insensés méprisent la sagesse et l’instruction.", 
	hi_title: "ज्ञान", 
	hi_content: "प्रभु का भय ज्ञान की शुरुआत है; मूर्ख लोग ज्ञान और शिक्षा को तुच्छ समझते हैं।", 
	zh_title: "Zhīshì", 
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
