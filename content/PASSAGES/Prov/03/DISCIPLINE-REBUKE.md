---
name: passage.DISCIPLINE_AND_REBUKE
alias: "Passage: DISCIPLINE AND REBUKE"
type: PASSAGE
parent: topic.HUMILITY
tags:
- humility
- discipline
- rebuke
- love
- delight
neo4j: true
ptopic: "[[topic-HUMILITY]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.DISCIPLINE_AND_REBUKE",
    alias: "Passage: DISCIPLINE AND REBUKE",
    parent: "topic.HUMILITY",
    tags: ["humility", "discipline", "rebuke", "love", "delight"],
    source: "'Proverbs 3:11,12'",
    sortedsource: "'Proverbs 03:11,12'",
    biblelink: "(https://www.biblegateway.com/passage/?search=proverbs+3%3A11-12&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.DISCIPLINE_AND_REBUKE",
    en_title: "DISCIPLINE AND REBUKE",
    en_content: "My son, do not reject the discipline of the LORD Or loathe His rebuke, For whom the LORD loves He disciplines,",
 es_title: "DISCIPLINA Y REPRODUCCIÓN",
 es_content: "Hijo mío, no rechaces la disciplina de Jehová ni detestes su reprensión; porque Jehová disciplina a quien ama.",
 fr_title: "DISCIPLINE ET RÉprimande",
 fr_content: "Mon fils, ne rejette pas la discipline de l'Éternel, et ne déteste pas ses réprimandes, car il corrige celui que l'Éternel aime.",
 hi_title: "अनुशासन और फटकार",
 hi_content: "हे मेरे पुत्र, यहोवा के अनुशासन को अस्वीकार न करना, और न उसकी घुड़की से घृणा करना, क्योंकि जिस से यहोवा प्रेम रखता है, उसी को वह ताड़ना देता है।",
 zh_title: "guǎn jiào yǔ chì zé",
 zh_content: "wǒ ér ， nǐ bù kě jù jué yē hé huá de guǎn jiào ， yě bù kě yàn wù tā de zé bèi ； yē hé huá suǒ ài de ， tā bì guǎn jiào ；",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.DISCIPLINE_AND_REBUKE"})
MATCH (c:CONTENT {name: "content.DISCIPLINE_AND_REBUKE"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.DISCIPLINE_AND_REBUKE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MATCH (child:PASSAGE {name: "passage.DISCIPLINE_AND_REBUKE"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.HUMILITY->DISCIPLINE_AND_REBUKE"}]->(child);

```
