---
type: PASSAGE
name: "passage.HOUSE OF THE WICKED"
alias: "Passage: The Two Houses"
parent: "topic.EVIL"
sortedsource: "Proverbs 03:33"
en_content: "The Lord's curse is on the house of the wicked, but He blesses the dwelling of the righteous."
tags: ["wicked", "house", "curse", "dwelling", "righteous"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'p' and 'c' as variables to keep them in memory
CREATE (p:PASSAGE {
    name: "passage.HOUSE OF THE WICKED",
    parent: "topic.EVIL",
		alias: "Passage: The Two Houses", 
		tags: ["wicked", "house", "curse", "dwelling", "righteous"], 
		source: "Proverbs 3:33",
		sortedsource: "Proverbs 03:33",
		biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A33&version=ESV",
		level: 4
})

CREATE (c:CONTENT {
    
	name: "content.HOUSE OF THE WICKED",
	ctype: "PASSAGE",
	en_title: "Passage: The Two Houses", 
	en_content: "The Lord's curse is on the house of the wicked, but He blesses the dwelling of the righteous.", 
	es_title: "Pasaje: Las Dos Casas", 
	es_content: "La maldición del Señor recae sobre la casa de los malvados, pero bendice la morada de los justos.", 
	fr_title: "Passage : Les Deux Maisons",
	fr_content: "La malédiction de l'Éternel est sur la maison du méchant, mais il bénit la demeure des justes.", 
	hi_title: "परिच्छेद: दो सदन",
	hi_content: "दुष्टों के घर पर प्रभु का श्राप है, परन्तु धर्मियों के घर पर वह आशीष देता है।", 
	zh_title: "duàn luò : liǎng zuò fáng zi",
	zh_content: "yēhéhuá zhòu zǔ èrén zhī jiā, cì fú yǔ yì rén de jūsuǒ."
})

// 2. Link Content to Passage using the variables 'p' and 'c'
MERGE (p)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.HOUSE OF THE WICKED"

// 3. Pass 'p' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_PASSAGE]->(p)
ON CREATE SET r2.name = "p.edge.EVIL->HOUSE OF THE WICKED"
RETURN p, parent;
```
