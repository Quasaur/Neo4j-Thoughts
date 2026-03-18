---
type: THOUGHT
name: "thought.GOD IS REAL"
alias: "Thought: God Is Real"
parent: "topic.THE GODHEAD"
en_content: "In these uncertain times GOD IS REAL...but not much else."
tags: ["real", "truth", "uncertainty", "god"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jun-2014)
CREATE (t:THOUGHT {    name: "thought.GOD IS REAL",
    alias: "Thought: God Is Real",
    parent: "topic.THE GODHEAD",
    tags: ['real', 'truth', 'uncertainty', 'god'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD IS REAL",
    ctype: "THOUGHT",
    en_title: "God Is Real",
    en_content: "In these uncertain times GOD IS REAL...but not much else.",
    es_title: "Dios Es Real",
    es_content: "En estos tiempos inciertos DIOS ES REAL...pero no mucho más.",
    fr_title: "Dieu Est Réel",
    fr_content: "En ces temps incertains DIEU EST RÉEL...mais pas grand-chose d'autre.",
    hi_title: "ईश्वर सत्य है",
    hi_content: "इन अनिश्चित समयों में ईश्वर सत्य है...लेकिन और बहुत कुछ नहीं।",
    zh_title: "Shàngdì shì zhēnshí de",
    zh_content: "Zài zhèxiē bù quèdìng de shíguāng lǐ, Shàngdì shì zhēnshí de...dàn qítā de dōngxī què bùduō."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD IS REAL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD IS REAL"
RETURN t, parent;
```
