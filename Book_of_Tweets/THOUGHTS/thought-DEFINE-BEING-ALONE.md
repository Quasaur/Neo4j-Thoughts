---
type: THOUGHT
name: "thought.DEFINE BEING ALONE"
alias: "Thought: Define Being Alone"
parent: "topic.SPIRITUALITY"
en_content: "The true definition of being alone is being unaware of God's Loving Presence."
tags: ["alone", "presence", "god", "awareness", "spirituality"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013a)
CREATE (t:THOUGHT {    name: "thought.DEFINE BEING ALONE",
    alias: "Thought: Define Being Alone",
    parent: "topic.SPIRITUALITY",
    tags: ['alone', 'presence', 'god', 'awareness', 'spirituality'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.DEFINE BEING ALONE",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE BEING ALONE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->DEFINE BEING ALONE"
RETURN t, parent;
```
