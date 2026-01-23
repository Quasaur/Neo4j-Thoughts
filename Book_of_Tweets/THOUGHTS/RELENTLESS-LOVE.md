---
name: "thought.RELENTLESS LOVE"
alias: "Thought: Relentless Love"
type: THOUGHT
en_content: "Love is ruthless...relentless...persistent and unflagging...thank God!"
parent: "topic.THE GODHEAD"
tags:
- love
- character
- god
- persistence
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.RELENTLESS LOVE",
    alias: "Thought: Relentless Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'character', 'god', 'persistence', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RELENTLESS LOVE",
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

MATCH (t:THOUGHT {name: "thought.RELENTLESS LOVE"})
MATCH (c:CONTENT {name: "content.RELENTLESS LOVE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.RELENTLESS LOVE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.RELENTLESS LOVE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >RELENTLESS LOVE" }]->(child);
```
