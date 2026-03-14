---
type: PASSAGE
name: "passage.TRUST THE LORD"
alias: "Passage: Trust the Lord"
parent: "topic.FAITH"
en_content: "Trust in the LORD with all your heart And do not lean on your own understanding. In all your ways acknowledge Him, And He will make your paths straight."
tags: ["trust", "faith", "self_doubt", "acknowledge", "promise"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.TRUST THE LORD",
    parent: "topic.FAITH",
    alias: "Passage: Trust the Lord",
    tags: ["trust", "faith", "self_doubt", "acknowledge", "promise"],
    source: "'Proverbs 3:5,6'",
    sortedsource: "'Proverbs 03:05-06'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+3%3A5-6&version=NASB)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.TRUST THE LORD",
    ctype: "PASSAGE",
    en_title: "'Passage: TRUST THE LORD'",
    en_content: "Trust in the LORD with all your heart And do not lean on your own understanding. In all your ways acknowledge Him, And He will make your paths straight.",
 es_title: "'Pasaje: CONFÍA EN EL SEÑOR'",
 es_content: "Confía en Jehová con todo tu corazón y no te apoyes en tu propia prudencia. Reconócelo en todos tus caminos, y él enderezará tus veredas.",
 fr_title: "Passage : FAITES CONFIANCE AU SEIGNEUR",
 fr_content: "Confie-toi à l'Éternel de tout ton cœur, et ne t'appuie pas sur ta propre intelligence. Dans toutes vos voies, reconnaissez-le, et il aplanira vos sentiers.",
 hi_title: "'मार्ग: प्रभु पर भरोसा रखें'",
 hi_content: "पूरे दिल से यहोवा पर भरोसा रखो और अपनी समझ का सहारा मत लो। अपने सभी मार्गों में उसे स्वीकार करो, और वह तुम्हारे लिए मार्ग सीधा करेगा।",
 zh_title: "“ jīng wén ： xiāng xìn yē hé huá ”",
 zh_content: "quán xīn quán yì dì xìn lài zhǔ ， bú yào yī kào zì jǐ de lǐ jiě 。 zài nǐ yī qiè suǒ xíng de lù shàng dōu yào chéng rèn tā ， tā jiù huì zhǐ yǐn nǐ de dào lù 。",


})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.TRUST THE LORD"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.FAITH->TRUST THE LORD"
RETURN b, parent;
```
