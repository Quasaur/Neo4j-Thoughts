---
name: "passage.HOUSE OF THE WICKED"
alias: "Passage: The Two Houses"
type: PASSAGE
parent: topic.EVIL
tags:
- wicked
- house
- curse
- dwelling
- righteous
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
//create the Passage with the same fields as a normal thought
CREATE (p:PASSAGE {
	    name: "passage.HOUSE OF THE WICKED",
		alias: "Passage: The Two Houses", 
		parent: "topic.EVIL", 
		tags: ["wicked", "house", "curse", "dwelling", "righteous"], 
		source: "Proverbs 3:33",
		sortedsource: "Proverbs 03:33",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A33&version=ESV",
		notes: "",
		level: 4});
// create multi-lingual content		
CREATE (c:CONTENT {
	name: "content.HOUSE OF THE WICKED",
	ctype: 3, // 1=thought; 2=quote; 3=passage
	en_title: "HOUSE OF THE WICKED", 
	en_content: "The Lord's curse is on the house of the wicked, but He blesses the dwelling of the righteous.", 
	es_title: "La casa de los malvados", 
	es_content: "La maldición del Señor recae sobre la casa de los malvados, pero bendice la morada de los justos.", 
	fr_title: "La maison du méchant",
	fr_content: "La malédiction de l'Éternel est sur la maison du méchant, mais il bénit la demeure des justes.", 
	hi_title: "दुष्टों का घर",
	hi_content: "दुष्टों के घर पर प्रभु का श्राप है, परन्तु धर्मियों के घर पर वह आशीष देता है।", 
	zh_title: "Èrén zhī jiā",
	zh_content: "yēhéhuá zhòu zǔ èrén zhī jiā, cì fú yǔ yì rén de jūsuǒ."});
// link content to node
MATCH (p:PASSAGE {name: 'passage.HOUSE OF THE WICKED'})
MATCH (c:CONTENT {name: 'content.HOUSE OF THE WICKED'})
MERGE (p)-[:HAS_CONTENT {name: "p.edge.HOUSE OF THE WICKED"}]->(c)
RETURN *;
// link node to parent node
MATCH (parent:TOPIC {name: 'topic.EVIL'})
MATCH (child:PASSAGE {name: 'passage.HOUSE OF THE WICKED'})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.EVIL->HOUSE OF THE WICKED"}]->(child)
RETURN *;

```
