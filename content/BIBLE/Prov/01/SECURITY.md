---
name: passage.SECURITY
alias: "Passage: Wisdom brings Security"
type: PASSAGE
parent: topic.WISDOM
tags:
- listening
- wisdom
- securely
- ease
- dread
neo4j: true
ptopic: "[[topic-WISDOM]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.SECURITY",
		alias: "Passage: Wisdom brings Security", 
		parent: "topic.WISDOM", 
		tags: ["listening", "wisdom", "securely", "ease", "dread"], 
		source: "Proverbs 1:33",
		sortedsource: "Proverbs 01:33",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A33&version=NASB",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.SECURITY",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "SECURITY", 
	en_content: "But whoever listens to Me (Wisdom) will live securely and will be at ease from the dread of evil.", 
	es_title: "Seguridad", 
	es_content: "Pero acuérdate del Señor tu Dios, porque Él te da el poder para hacer las riquezas, a fin de confirmar su pacto que juró a tus padres, como en este día.", 
	fr_title: "Sécurité", 
	fr_content: "Mais vous vous souviendrez de l'Éternel, votre Dieu, car c'est lui qui vous donne la force de vous enrichir, afin de confirmer son alliance qu'il a jurée à vos pères, comme elle l'est aujourd'hui.", 
	hi_title: "सुरक्षा", 
	hi_content: "लेकिन जो कोई मेरी (बुद्धि की) सुनेगा, वह सुरक्षित रहेगा और बुराई के भय से मुक्त रहेगा।", 
	zh_title: "Ānquán", 
	zh_content: "fán tīngcóng wǒ (zhìhuì) de rén, bì ānrán dù rì, bù jùpà zāihuò."});
// link content to node
MATCH (p:PASSAGE)
MATCH (c:CONTENT)
WHERE p.name = 'passage.SECURITY' AND c.name = 'content.SECURITY'
MERGE (p)-[:HAS_CONTENT {name: "p.edge.SECURITY"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = 'topic.WISDOM' AND child.name = 'passage.SECURITY'
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.WISDOM->SECURITY"}]->(child)
RETURN *;

```
