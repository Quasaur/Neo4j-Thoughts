---
type: THOUGHT
name: "thought.GOD NOT AMERICAN"
alias: "Thought: God Not American"
parent: "topic.THE GODHEAD"
en_content: "God is NOT an American."
tags: ["god", "politics", "nation", "character", "truth"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Mar-2012)
CREATE (t:THOUGHT {    name: "thought.GOD NOT AMERICAN",
    alias: "Thought: God Not American",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'politics', 'nation', 'character', 'truth'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD NOT AMERICAN",
    ctype: "THOUGHT",
    en_title: "God Not American",
    en_content: "God is NOT an American.",
    es_title: "Dios No Es Estadounidense",
    es_content: "Dios NO es estadounidense.",
    fr_title: "Dieu N'est Pas Américain",
    fr_content: "Dieu N'EST PAS américain.",
    hi_title: "भगवान अमेरिकी नहीं हैं",
    hi_content: "भगवान अमेरिकी नहीं हैं।",
    zh_title: "Shàng Dì Bú Shì Měi Guó Rén",
    zh_content: "Shàng Dì BÚ SHÌ Měi guó rén."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD NOT AMERICAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD NOT AMERICAN"
RETURN t, parent;
```
