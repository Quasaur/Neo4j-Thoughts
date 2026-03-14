---
type: PASSAGE
name: "passage.DISCIPLINE AND REBUKE"
alias: "Passage: Discipline and Rebuke"
parent: "topic.HUMILITY"
en_content: "My son, do not reject the discipline of the LORD Or loathe His rebuke, For whom the LORD loves He disciplines,"
tags: ["humility", "discipline", "rebuke", "love", "delight"]
ptopic: "[[topic-HUMILITY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.DISCIPLINE AND REBUKE",
    parent: "topic.HUMILITY",
    alias: "Passage: Discipline and Rebuke",
    tags: ["humility", "discipline", "rebuke", "love", "delight"],
    source: "'Proverbs 3:11,12'",
    sortedsource: "'Proverbs 03:11,12'",
    biblelink: "(https://www.biblegateway.com/passage/?search=proverbs+3%3A11-12&version=NASB)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.DISCIPLINE AND REBUKE",
    ctype: "PASSAGE",
    en_title: "Discipline and Rebuke",
    en_content: "My son, do not reject the discipline of the LORD Or loathe His rebuke, For whom the LORD loves He disciplines,",
 es_title: "DISCIPLINA Y REPRODUCCIÓN",
 es_content: "Hijo mío, no rechaces la disciplina de Jehová ni detestes su reprensión; porque Jehová disciplina a quien ama.",
 fr_title: "DISCIPLINE ET RÉprimande",
 fr_content: "Mon fils, ne rejette pas la discipline de l'Éternel, et ne déteste pas ses réprimandes, car il corrige celui que l'Éternel aime.",
 hi_title: "अनुशासन और फटकार",
 hi_content: "हे मेरे पुत्र, यहोवा के अनुशासन को अस्वीकार न करना, और न उसकी घुड़की से घृणा करना, क्योंकि जिस से यहोवा प्रेम रखता है, उसी को वह ताड़ना देता है।",
 zh_title: "guǎn jiào yǔ chì zé",
 zh_content: "wǒ ér ， nǐ bù kě jù jué yē hé huá de guǎn jiào ， yě bù kě yàn wù tā de zé bèi ； yē hé huá suǒ ài de ， tā bì guǎn jiào ；",


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
