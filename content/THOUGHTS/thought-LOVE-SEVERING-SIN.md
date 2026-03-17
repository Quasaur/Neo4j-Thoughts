---
type: THOUGHT
name: "thought.LOVE SEVERING SIN"
alias: "Thought: Love Severing Sin"
parent: "topic.LOVE"
en_content: "Only Love can separate sinners from their sins."
tags: ["love", "sin", "separation", "grace", "transformation"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOVE SEVERING SIN",
    alias: "Thought: Love Severing Sin",
    parent: "topic.LOVE",
    tags: ['love', 'sin', 'separation', 'grace', 'transformation'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE SEVERING SIN",
    ctype: "THOUGHT",
    en_title: "Love Severing Sin",
    en_content: "Only Love can separate sinners from their sins.",
    es_title: "El Amor Separando el Pecado",
    es_content: "Sólo el Amor puede separar a los pecadores de sus pecados.",
    fr_title: "L'Amour Séparant le Péché",
    fr_content: "Seul l'Amour peut séparer les pécheurs de leurs péchés.",
    hi_title: "प्रेम पाप को अलग करता है",
    hi_content: "केवल प्रेम ही पापियों को उनके पापों से अलग कर सकता है।",
    zh_title: "Ài Gēduàn Zuì'è",
    zh_content: "Wéiyǒu Ài néng jiāng zuìrén cóng tāmen de zuì'è zhōng fēnlí."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE SEVERING SIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->LOVE SEVERING SIN"
RETURN t, parent;
```
