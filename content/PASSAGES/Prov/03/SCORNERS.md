---
name: passage.SCORNERS
alias: "Passage: SCORNERS"
type: PASSAGE
parent: topic.EVIL
tags:
- scorners
- scornful
- humble
- gift
- favor
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.SCORNERS",
    alias: "Passage: SCORNERS",
    parent: "topic.EVIL",
    tags: ["scorners", "scornful", "humble", "gift", "favor"],
    source: "'Proverbs 3:34'",
    sortedsource: "'Proverbs 03:34'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A34&version=ESV)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SCORNERS",
    en_title: "SCORNERS",
    en_content: "Toward the scorners He [The LORD] is scornful,",
 es_title: "SCORNERADORES",
 es_content: "Con los escarnecedores Él [Jehová] es escarnecedor,",
 fr_title: "Les moqueurs",
 fr_content: "Il [l'Éternel] se moque des moqueurs,",
 hi_title: "उपहास करने वाले",
 hi_content: "वह [प्रभु] ठट्ठा करनेवालों के प्रति तिरस्कार करता है,",
 zh_title: "miè shì zhě",
 zh_content: "tā ［ yē hé huá ］ miǎo shì xiè màn de rén ，",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.SCORNERS"})
MATCH (c:CONTENT {name: "content.SCORNERS"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.SCORNERS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.SCORNERS"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->SCORNERS"}]->(child);

```
