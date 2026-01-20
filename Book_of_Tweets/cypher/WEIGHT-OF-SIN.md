---
name: "thought.WEIGHT OF SIN"
alias: "Thought: Weight Of Sin"
type: THOUGHT
en_content: "Christ bore in His Body the sins of the 12 billion sinners who have lived since Adam."
parent: "topic.THE GODHEAD"
tags:
- atonement
- sin
- cross
- redemption
- jesus
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011f)
CREATE (t:THOUGHT {
    name: "thought.WEIGHT OF SIN",
    alias: "Thought: Weight Of Sin",
    parent: "topic.THE GODHEAD",
    tags: ['atonement', 'sin', 'cross', 'redemption', 'jesus'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.WEIGHT OF SIN",
    en_title: "Weight Of Sin",
    en_content: "Christ bore in His Body the sins of the 12 billion sinners who have lived since Adam.",
    es_title: "El Peso del Pecado",
    es_content: "Cristo llevó en Su Cuerpo los pecados de los 12 mil millones de pecadores que han vivido desde Adán.",
    fr_title: "Le Poids du Péché",
    fr_content: "Le Christ a porté dans Son Corps les péchés des 12 milliards de pécheurs qui ont vécu depuis Adam.",
    hi_title: "पाप का भार",
    hi_content: "मसीह ने अपने शरीर में आदम के समय से जीवित रहे 12 अरब पापियों के पापों को धारण किया।",
    zh_title: "Zuì'è de Zhòngliàng",
    zh_content: "Jīdū zài Tā de shēntǐ zhōng chéngdān le cóng Yàdāng yǐlái suǒyǒu 120 yì zuìrén de zuì'è."
});

MATCH (t:THOUGHT {name: "thought.WEIGHT OF SIN"})
MATCH (c:CONTENT {name: "content.WEIGHT OF SIN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WEIGHT OF SIN" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.WEIGHT OF SIN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >WEIGHT OF SIN" }]->(child);
```
