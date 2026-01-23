---
name: "thought.GOD IS REAL"
alias: "Thought: God Is Real"
type: THOUGHT
en_content: "In these uncertain times GOD IS REAL...but not much else."
parent: "topic.THE GODHEAD"
tags:
- real
- truth
- uncertainty
- god
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jun-2014)
CREATE (t:THOUGHT {
    name: "thought.GOD IS REAL",
    alias: "Thought: God Is Real",
    parent: "topic.THE GODHEAD",
    tags: ['real', 'truth', 'uncertainty', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD IS REAL",
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

MATCH (t:THOUGHT {name: "thought.GOD IS REAL"})
MATCH (c:CONTENT {name: "content.GOD IS REAL"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS REAL" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD IS REAL"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD IS REAL" }]->(child);
```
