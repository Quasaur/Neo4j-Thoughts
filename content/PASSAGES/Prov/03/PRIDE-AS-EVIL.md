---
name: passage.PRIDE-AS-EVIL
alias: "Passage: PRIDE-AS-EVIL"
type: PASSAGE
parent: topic.HUMILITY
tags:
- trust
- faith
- selfdoubt
- acknowledge
- promise
neo4j: true
ptopic: "[[topic-HUMILITY]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.PRIDE-AS-EVIL",
    alias: "Passage: PRIDE-AS-EVIL",
    parent: "topic.HUMILITY",
    tags: ["trust", "faith", "selfdoubt", "acknowledge", "promise"],
    source: "'Proverbs 3:7,8'",
    sortedsource: "'Proverbs 03:07,09'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+3%3A7-8&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PRIDE-AS-EVIL",
    en_title: "PRIDE-AS-EVIL",
    en_content: "Do not be wise in your own eyes; Fear the LORD and turn away from evil. It will be healing to your body And refreshment to your bones.",
 es_title: "ORGULLO COMO MAL",
 es_content: "No seas sabio en tu propia opinión; Teme al Señor y apártate del mal. Será sanidad para tu cuerpo y refrigerio para tus huesos.",
 fr_title: "LA FIERTÉ COMME LE MAL",
 fr_content: "Ne soyez pas sage à vos propres yeux ; Craignez l'Éternel et détournez-vous du mal. Cela guérira votre corps et rafraîchira vos os.",
 hi_title: "अहंकार-जैसा-बुराई",
 hi_content: "अपनी दृष्टि में बुद्धिमान मत बनो; यहोवा का भय मानो और बुराई से दूर रहो। यह आपके शरीर को स्वस्थ करेगा और आपकी हड्डियों को ताज़गी देगा।",
 zh_title: "jiāo ào shì xié è de",
 zh_content: "bú yào zì yǐ wéi cōng míng ； jìng wèi yē hé huá ， yuǎn lí è shì 。 tā jiāng zhì yù nín de shēn tǐ bìng shuā xīn nín de gǔ gé 。",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.PRIDE-AS-EVIL"})
MATCH (c:CONTENT {name: "content.PRIDE-AS-EVIL"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.PRIDE-AS-EVIL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MATCH (child:PASSAGE {name: "passage.PRIDE-AS-EVIL"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.HUMILITY->PRIDE-AS-EVIL"}]->(child);

```
