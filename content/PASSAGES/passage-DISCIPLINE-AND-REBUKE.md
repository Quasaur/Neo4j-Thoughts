---
type: PASSAGE
name: "passage.DISCIPLINE AND REBUKE"
alias: "Passage: Discipline and Rebuke"
parent: "topic.HUMILITY"
sortedsource: "Proverbs 03:11,12"
en_content: "My son, do not reject the discipline of the LORD Or loathe His rebuke, For whom the LORD loves He disciplines, Just as a father disciplines the son in whom he delights."
tags: ["humility", "discipline", "rebuke", "love", "delight"]
ptopic: "[[topic-HUMILITY]]"
level: 4
neo4j: true
verified: true
--- 

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.DISCIPLINE AND REBUKE",
    parent: "topic.HUMILITY",
    alias: "Passage: Discipline and Rebuke",
    tags: ["humility", "discipline", "rebuke", "love", "delight"],
    source: "Proverbs 3:11,12",
    sortedsource: "Proverbs 03:11,12",
    biblelink: "https://www.biblegateway.com/passage/?search=proverbs+3%3A11-12&version=NASB",
    level: 4
})

CREATE (c:CONTENT {
    name: "content.DISCIPLINE AND REBUKE",
    ctype: "PASSAGE",
    en_title: "Passage: Discipline and Rebuke",
    en_content: "My son, do not reject the discipline of the LORD
	Or loathe His rebuke,
	For whom the LORD loves He disciplines,
	Just as a father disciplines the son in whom he delights.",
 es_title: "Pasaje: Disciplina y reprensión",
 es_content: "Hijo mío, no rechaces la disciplina del SEÑOR
	O aborrecer su reprensión,
	Al que ama, el Señor disciplina,
	Así como un padre disciplina al hijo en quien se deleita.",
 fr_title: "Passage : Discipline et réprimande",
 fr_content: "Mon fils, ne rejette pas la discipline de l'Éternel
	Ou détester ses réprimandes,
	Pour celui que l'Éternel aime, il discipline,
	Tout comme un père discipline son fils en qui il prend plaisir.",
 hi_title: "परिच्छेद: अनुशासन और फटकार",
 hi_content: "मेरे बेटे, प्रभु के अनुशासन को अस्वीकार मत करो
	या उसकी डांट से घृणा करो,
	यहोवा जिस से प्रेम रखता है, उस को ताड़ना देता है,
	ठीक वैसे ही जैसे एक पिता अपने बेटे को अनुशासित करता है जिससे वह प्रसन्न होता है।",
 zh_title: "jīng wén : guǎn jiào yǔ zé bèi",
 zh_content: "wǒ ér , bù kě jù jué zhǔ de guǎn jiào huò zhě yàn wù tā de zé bèi ,
	  zhǔ suǒ ài de , 
	  tā bì guǎn jiào , 
	  zhèng rú fù qīn guǎn jiào tā suǒ xǐ ài de ér zi yī yàng ."
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.DISCIPLINE AND REBUKE"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.HUMILITY->DISCIPLINE AND REBUKE"
RETURN b, parent;
```
