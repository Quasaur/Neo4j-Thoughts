---
type: PASSAGE
name: "passage.INHERITED HONOR"
alias: "Passage: Honor and Disgrace"
parent: "topic.WISDOM"
sortedsource: "Proverbs 03:35"
en_content: "The wise will inherit honor, but fools get disgrace."
tags: ["wise", "inherit", "honor", "fools", "disgrace"]
ptopic: "[[topic-WISDOM]]"
level: 3
neo4j: true
verified: true
---
```Cypher
// 1. Create the Passage and Content nodes
// Using 'p' and 'c' as variables to keep them in memory
CREATE (p:PASSAGE {
    name: "passage.INHERITED HONOR",
    parent: "topic.WISDOM",
		alias: "Passage: Honor and Disgrace", 
		tags: ["wise", "inherit", "honor", "fools", "disgrace"], 
		source: "Proverbs 3:35",
		sortedsource: "Proverbs 03:35",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A35&version=ESV",
		level: 3
})

CREATE (c:CONTENT {
    
	name: "content.INHERITED HONOR",
	ctype: "PASSAGE",
	en_title: "Passage: Honor and Disgrace", 
	en_content: "The wise will inherit honor, but fools get disgrace.", 
	es_title: "Pasaje: Honor y Deshonra",
	es_content: "Los sabios heredarán el honor, pero los necios recibirán deshonra.", 
	fr_title: "Passage : Honneur et Disgrâce",
	fr_content: "Les sages hériteront de l'honneur, mais les insensés recevront la honte.", 
	hi_title: "परिच्छेद: सम्मान और अपमान",
	hi_content: "बुद्धिमान को सम्मान मिलेगा, परन्तु मूर्खों को अपमान मिलेगा।", 
	zh_title: "duàn luò : róng yù yǔ chǐ rǔ", 
	zh_content: "zhì zhě jiāng jì chéng róng yù , yú zhě jiāng huò dé chǐ ​​ rǔ ."
})

// 2. Link Content to Passage using the variables 'p' and 'c'
MERGE (p)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.INHERITED HONOR"

// 3. Pass 'p' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_PASSAGE]->(p)
ON CREATE SET r2.name = "p.edge.WISDOM->INHERITED HONOR"
RETURN p, parent;
```
