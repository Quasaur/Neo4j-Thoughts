---
type: PASSAGE
name: "passage.PRIDE-AS-EVIL"
alias: "Passage: Pride-as-evil"
parent: "topic.HUMILITY"
en_content: "Do not be wise in your own eyes; Fear the LORD and turn away from evil. It will be healing to your body And refreshment to your bones."
tags: ["trust", "faith", "self_doubt", "acknowledge", "promise"]
ptopic: "[[topic-HUMILITY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.PRIDE-AS-EVIL",
    parent: "topic.HUMILITY",
    alias: "Passage: Pride-as-evil",
    tags: ["trust", "faith", "self_doubt", "acknowledge", "promise"],
    source: "'Proverbs 3:7,8'",
    sortedsource: "'Proverbs 03:07,09'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+3%3A7-8&version=NASB)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.PRIDE-AS-EVIL",
    ctype: "PASSAGE",
    en_title: "Pride-as-evil",
    en_content: "Do not be wise in your own eyes; Fear the LORD and turn away from evil. It will be healing to your body And refreshment to your bones.",
 es_title: "ORGULLO COMO MAL",
 es_content: "No seas sabio en tu propia opinión; Teme al Señor y apártate del mal. Será sanidad para tu cuerpo y refrigerio para tus huesos.",
 fr_title: "LA FIERTÉ COMME LE MAL",
 fr_content: "Ne soyez pas sage à vos propres yeux ; Craignez l'Éternel et détournez-vous du mal. Cela guérira votre corps et rafraîchira vos os.",
 hi_title: "अहंकार-जैसा-बुराई",
 hi_content: "अपनी दृष्टि में बुद्धिमान मत बनो; यहोवा का भय मानो और बुराई से दूर रहो। यह आपके शरीर को स्वस्थ करेगा और आपकी हड्डियों को ताज़गी देगा।",
 zh_title: "jiāo ào shì xié è de",
 zh_content: "bú yào zì yǐ wéi cōng míng ； jìng wèi yē hé huá ， yuǎn lí è shì 。 tā jiāng zhì yù nín de shēn tǐ bìng shuā xīn nín de gǔ gé 。",


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
