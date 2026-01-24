---
name: "thought.DEFINE BEING ALONE"
alias: "Thought: Define Being Alone"
type: THOUGHT
en_content: "The true definition of being alone is being unaware of God's Loving Presence."
parent: "topic.SPIRITUALITY"
tags:
- alone
- presence
- god
- awareness
- spirituality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.DEFINE BEING ALONE",
    alias: "Thought: Define Being Alone",
    parent: "topic.SPIRITUALITY",
    tags: ['alone', 'presence', 'god', 'awareness', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEFINE BEING ALONE",
    en_title: "Define Being Alone",
    en_content: "The true definition of being alone is being unaware of God's Loving Presence.",
    es_title: "Definir Estar Solo",
    es_content: "La verdadera definición de estar solo es estar inconsciente de la Presencia Amorosa de Dios.",
    fr_title: "Définir Être Seul",
    fr_content: "La vraie définition d'être seul est d'être inconscient de la Présence Aimante de Dieu.",
    hi_title: "अकेले होने को परिभाषित करें",
    hi_content: "अकेले होने की सच्ची परिभाषा परमेश्वर की प्रेमपूर्ण उपस्थिति से अनजान होना है।",
    zh_title: "Dìngyì Gūdān",
    zh_content: "Gūdān de zhēnzhèng dìngyì shì bù zhī Shàngdì de ài xīn chūzài."
});

MATCH (t:THOUGHT {name: "thought.DEFINE BEING ALONE"})
MATCH (c:CONTENT {name: "content.DEFINE BEING ALONE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE BEING ALONE" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.DEFINE BEING ALONE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->DEFINE BEING ALONE" }]->(child);
```
