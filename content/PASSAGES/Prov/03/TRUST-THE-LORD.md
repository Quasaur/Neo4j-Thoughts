---
name: passage.TRUST_THE_LORD
alias: "Passage: 'Passage: TRUST THE LORD'"
type: PASSAGE
parent: topic.FAITH
tags:
- trust
- faith
- selfdoubt
- acknowledge
- promise
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.TRUST_THE_LORD",
    alias: "Passage: 'Passage: TRUST THE LORD'",
    parent: "topic.FAITH",
    tags: ["trust", "faith", "selfdoubt", "acknowledge", "promise"],
    source: "'Proverbs 3:5,6'",
    sortedsource: "'Proverbs 03:05-06'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+3%3A5-6&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.TRUST_THE_LORD",
    en_title: "'Passage: TRUST THE LORD'",
    en_content: "Trust in the LORD with all your heart And do not lean on your own understanding. In all your ways acknowledge Him, And He will make your paths straight.",
 es_title: "'Pasaje: CONFÍA EN EL SEÑOR'",
 es_content: "Confía en Jehová con todo tu corazón y no te apoyes en tu propia prudencia. Reconócelo en todos tus caminos, y él enderezará tus veredas.",
 fr_title: "\"Passage : FAITES CONFIANCE AU SEIGNEUR\"",
 fr_content: "Confie-toi à l'Éternel de tout ton cœur, et ne t'appuie pas sur ta propre intelligence. Dans toutes vos voies, reconnaissez-le, et il aplanira vos sentiers.",
 hi_title: "'मार्ग: प्रभु पर भरोसा रखें'",
 hi_content: "पूरे दिल से यहोवा पर भरोसा रखो और अपनी समझ का सहारा मत लो। अपने सभी मार्गों में उसे स्वीकार करो, और वह तुम्हारे लिए मार्ग सीधा करेगा।",
 zh_title: "“ jīng wén ： xiāng xìn yē hé huá ”",
 zh_content: "quán xīn quán yì dì xìn lài zhǔ ， bú yào yī kào zì jǐ de lǐ jiě 。 zài nǐ yī qiè suǒ xíng de lù shàng dōu yào chéng rèn tā ， tā jiù huì zhǐ yǐn nǐ de dào lù 。",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.TRUST_THE_LORD"})
MATCH (c:CONTENT {name: "content.TRUST_THE_LORD"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.TRUST_THE_LORD"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:PASSAGE {name: "passage.TRUST_THE_LORD"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.FAITH->TRUST_THE_LORD"}]->(child);

```
