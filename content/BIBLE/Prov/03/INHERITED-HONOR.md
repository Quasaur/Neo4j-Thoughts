---
name: "passage.INHERITED HONOR"
alias: "Passage: HONOR AND DISGRACE"
type: PASSAGE
parent: topic.WISDOM
tags:
- wise
- inherit
- honor
- fools
- disgrace
neo4j: true
level: 3
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.INHERITED HONOR",
		alias: "Passage: HONOR AND DISGRACE", 
		parent: "topic.WISDOM", 
		tags: ["wise", "inherit", "honor", "fools", "disgrace"], 
		source: "Proverbs 3:35",
		sortedsource: "Proverbs 03:35",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A35&version=ESV",
		notes: "",
		level: 3});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.INHERITED HONOR",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "INHERITED HONOR", 
	en_content: "The wise will inherit honor,  
    but fools get disgrace.", 
	es_title: "Honor Heredado", 
	es_content: "Los sabios heredarán el honor,
pero los necios recibirán deshonra.", 
	fr_title: "L'honneur hérité", 
	fr_content: "Les sages hériteront de l'honneur, mais les insensés recevront la honte.", 
	hi_title: "विरासत में मिला सम्मान", 
	hi_content: "बुद्धिमान को सम्मान मिलेगा,
परन्तु मूर्खों को अपमान मिलेगा।", 
	zh_title: "Shì shìdài dài de zūn róng", 
	zh_content: "zhìzhě dé zūn róng, yúzhě shòurǔ."});
// link content to node
MATCH (p:PASSAGE)
MATCH (c:CONTENT)
WHERE p.name = 'passage.INHERITED HONOR' AND c.name = 'content.INHERITED HONOR'
MERGE (p)-[:HAS_CONTENT {name: "p.edge.INERITED HONOR"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC)
MATCH (child:PASSAGE)
WHERE parent.name = 'topic.WISDOM' AND child.name = 'passage.INHERITED HONOR'
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.WISDOM->INHERITED HONOR"}]->(child)
RETURN *;

```
