---
name: "passage.UNJUST GAIN"
alias: "Passage: Cheating is Deadly"
type: PASSAGE
parent: topic.WEALTH
tags:
- gain
- greed
- unjust
- death
- just
neo4j: true
ptopic: "[[topic-WEALTH]]"
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.UNJUST GAIN",
		alias: "Passage: Cheating is Deadly", 
		parent: "topic.WEALTH", 
		tags: ["gain", "greed", "unjust", "death", "just"], 
		source: "Proverbs 1:19",
		sortedsource: "Proverbs 01:19",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A19&version=NASBNASB",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.UNJUST GAIN",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "UNJUST GAIN", 
	en_content: "Such are the ways of everyone who makes unjust gain; it takes away the life of its possessors.", 
	es_title: "Ganancia injusta", 
	es_content: "Así procede todo el que obtiene ganancia injusta: quita la vida a sus poseedores.", 
	fr_title: "Gain injuste", 
	fr_content: "Telles sont les voies de quiconque se livre à un gain injuste : il enlève la vie à ceux qui le possèdent.", 
	hi_title: "अन्यायपूर्ण लाभ", 
	hi_content: "जो लोग अन्यायपूर्ण लाभ कमाते हैं, उनके तरीके ऐसे ही होते हैं; यह अपने मालिकों के जीवन को छीन लेता है।", 
	zh_title: "Bù yì zhī cái", 
	zh_content: "fán móuqǔ bù yì zhī cái de rén, dōu shì rúcǐ xíngjìng; bù yì zhī cái duó qùle yǒngyǒu zhě de shēngmìng."});
// link content to node
MATCH (p:PASSAGE)
MATCH (c:CONTENT)
WHERE p.name = 'passage.UNJUST GAIN' AND c.name = 'content.UNJUST GAIN'
MERGE (p)-[:HAS_CONTENT {name: "p.edge.UNJUST GAIN"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = 'topic.WEALTH' AND child.name = 'passage.UNJUST GAIN'
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.WEALTH->UNJUST GAIN"}]->(child)
RETURN *;

```
