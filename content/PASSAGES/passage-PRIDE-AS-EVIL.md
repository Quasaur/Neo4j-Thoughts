---
type: PASSAGE
name: "passage.PRIDE AS EVIL"
alias: "Passage: Pride as evil"
parent: "topic.HUMILITY"
sortedsource: "Proverbs 03:07,09"
en_content: "Do not be wise in your own eyes; Fear the LORD and turn away from evil. It will be healing to your body And refreshment to your bones."
tags: ["trust", "faith", "self_doubt", "acknowledge", "promise"]
ptopic: "[[topic-HUMILITY]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.PRIDE AS EVIL",
    parent: "topic.HUMILITY",
    alias: "Passage: Pride as evil",
    tags: ["trust", "faith", "self_doubt", "acknowledge", "promise"],
    source: "Proverbs 3:7,8",
    sortedsource: "Proverbs 03:07,09",
    biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+3%3A7-8&version=NASB",
    level: 4
})

CREATE (c:CONTENT {
    name: "content.PRIDE AS EVIL",
    ctype: "PASSAGE",
    en_title: "Passage: Pride as evil",
    en_content: "Do not be wise in your own eyes; 
	Fear the LORD and turn away from evil. 
	It will be healing to your body 
	And refreshment to your bones.",
	 es_title: "Pasaje: El orgullo como maldad",
	 es_content: "No seas sabio en tu propia opinión; 
	Teme al Señor y apártate del mal. 
	Será sanador para tu cuerpo. 
	Y refrigerio para tus huesos.",
	 fr_title: "Passage : La fierté comme un mal",
	 fr_content: "Ne soyez pas sage à vos propres yeux ; 
	Craignez l'Éternel et détournez-vous du mal. 
	Cela guérira votre corps 
	Et du rafraîchissement pour vos os.",
	 hi_title: "परिच्छेद: अहंकार बुराई के समान है",
	 hi_content: "अपनी दृष्टि में बुद्धिमान मत बनो; 
	यहोवा का भय मानो और बुराई से दूर रहो। 
	यह आपके शरीर के लिए उपचारकारी होगा 
	और आपकी हड्डियों को ताजगी मिलेगी।",
	 zh_title: "jīng wén : jiāo ào shì xié è de",
	 zh_content: "bú yào zì yǐ wéi cōng míng ; 
	 jìng wèi yē hé huá , yuǎn lí è shì . 
	 tā huì zhì yù nǐ de shēn tǐ hái néng ràng nǐ de gǔ tou huàn rán yì xīn ."
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.PRIDE-AS-EVIL"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.HUMILITY->PRIDE-AS-EVIL"
RETURN b, parent;
```
