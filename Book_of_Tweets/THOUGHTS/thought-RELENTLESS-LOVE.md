---
type: THOUGHT
name: "thought.RELENTLESS LOVE"
alias: "Thought: Relentless Love"
parent: "topic.THE GODHEAD"
en_content: "Love is ruthless...relentless...persistent and unflagging...thank God!"
tags: ["love", "character", "god", "persistence", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2012)
CREATE (t:THOUGHT {    name: "thought.RELENTLESS LOVE",
    alias: "Thought: Relentless Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'character', 'god', 'persistence', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.RELENTLESS LOVE",
    ctype: "THOUGHT",
    en_title: "Relentless Love",
    en_content: "Love is ruthless...relentless...persistent and unflagging...thank God!",
    es_title: "Amor Implacable",
    es_content: "El amor es despiadado...implacable...persistente e incansable...¡gracias a Dios!",
    fr_title: "Amour Implacable",
    fr_content: "L'amour est impitoyable...implacable...persistant et infatigable...Dieu merci !",
    hi_title: "अटल प्रेम",
    hi_content: "प्रेम निर्दयी है...अटल है...दृढ़ और अथक है...भगवान का धन्यवाद!",
    zh_title: "Wú Qíng De Ài",
    zh_content: "Ài shì wú qíng de...jiān chí bù xiè de...chí jiǔ ér bù juàn dài de...gǎn xiè Shàng Dì!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RELENTLESS LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->RELENTLESS LOVE"
RETURN t, parent;
```
