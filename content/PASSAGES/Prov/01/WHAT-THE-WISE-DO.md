---
name: "passage.WHAT THE WISE DO"
alias: "Passage: Wisdom Brings Growth"
type: PASSAGE
parent: topic.UNDERSTANDING
tags:
- wise
- listening
- learning
- collecting
- counsel
neo4j: true
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.WHAT THE WISE DO",
		alias: "Passage: Wisdom Brings Growth", 
		parent: "topic.UNDERSTANDING", 
		tags: ["wise", "listening", "learning", "collecting", "counsel"], 
		source: "Proverbs 1:5",
		sortedsource: "Proverbs 01:05",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A5&version=NASB",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.WHAT THE WISE DO",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "WHAT THE WISE DO", 
	en_content: "A wise person will hear and increase in learning, and a person of understanding will acquire wise counsel.", 
	es_title: "Lo que hacen los sabios", 
	es_content: "El sabio oirá y aumentará su conocimiento, y el entendido adquirirá consejo sabio.", 
	fr_title: "Ce que font les sages", 
	fr_content: "L’homme sage entendra et grandira en connaissance, et l’homme intelligent acquerra de sages conseils.", 
	hi_title: "बुद्धिमान क्या करते हैं", 
	hi_content: "बुद्धिमान व्यक्ति सुनेगा और अपनी शिक्षा बढ़ाएगा, और समझदार व्यक्ति बुद्धिमानी भरी सलाह ग्रहण करेगा।", 
	zh_title: "Zhìzhě zhī dào", 
	zh_content: "zhìzhě shànyú qīngtīng, zēngzhǎng xuéshì; tōngdá rén néng huòdé míngzhì de jiànyì."});
// link content to node
MATCH (p:PASSAGE {name: 'passage.WHAT THE WISE DO'})
MATCH (c:CONTENT {name: 'content.WHAT THE WISE DO'})
MERGE (p)-[:HAS_CONTENT {name: "p.edge.WHAT THE WISE DO"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC {name: 'topic.UNDERSTANDING'})
MATCH (child:PASSAGE {name: 'passage.WHAT THE WISE DO'})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.UNDERSTANDING->WHAT THE WISE DO"}]->(child)
RETURN *;

```
