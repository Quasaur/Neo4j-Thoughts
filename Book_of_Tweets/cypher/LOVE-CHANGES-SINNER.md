---
name: "thought.LOVE CHANGES SINNER"
alias: "Thought: Love Changes Sinner"
type: THOUGHT
en_content: "It is the LOVE OF GOD that changes a sinner to a saint."
parent: "topic.GRACE"
tags:
- love
- transformation
- grace
- salvation
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.LOVE CHANGES SINNER",
    alias: "Thought: Love Changes Sinner",
    parent: "topic.GRACE",
    tags: ['love', 'transformation', 'grace', 'salvation', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE CHANGES SINNER",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE CHANGES SINNER" AND c.name = "content.LOVE CHANGES SINNER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE CHANGES SINNER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LOVE CHANGES SINNER"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LOVE CHANGES SINNER" }]->(child);
```
