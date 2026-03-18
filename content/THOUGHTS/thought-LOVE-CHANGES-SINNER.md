---
type: THOUGHT
name: "thought.LOVE CHANGES SINNER"
alias: "Thought: Love Changes Sinner"
parent: "topic.LOVE"
en_content: "It is the LOVE OF GOD that changes a sinner to a saint."
tags: ["love", "transformation", "grace", "salvation", "character"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOVE CHANGES SINNER",
    alias: "Thought: Love Changes Sinner",
    parent: "topic.LOVE",
    tags: ['love', 'transformation', 'grace', 'salvation', 'character'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE CHANGES SINNER",
    ctype: "THOUGHT",
    en_title: "Love Changes Sinner",
    en_content: "It is the LOVE OF GOD that changes a sinner to a saint.",
    es_title: "El Amor Transforma al Pecador",
    es_content: "Es el AMOR DE DIOS el que transforma a un pecador en un santo.",
    fr_title: "L'Amour Transforme le Pécheur",
    fr_content: "C'est l'AMOUR DE DIEU qui transforme un pécheur en saint.",
    hi_title: "प्रेम पापी को बदलता है",
    hi_content: "यह परमेश्वर का प्रेम है जो एक पापी को संत में बदलता है।",
    zh_title: "Ài Gǎibiàn Zuìrén",
    zh_content: "Shì Shàngdì de ài shǐ zuìrén biànchéng shèngdú."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE CHANGES SINNER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->LOVE CHANGES SINNER"
RETURN t, parent;
```
