---
type: THOUGHT
name: "thought.GOD LOVES HOMOSEXUALS"
alias: "Thought: God Loves Homosexuals"
parent: "topic.THE GODHEAD"
en_content: "God loves homosexuals."
tags: ["love", "character", "god", "humanity", "inclusion"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jan-2012)
CREATE (t:THOUGHT {    name: "thought.GOD LOVES HOMOSEXUALS",
    alias: "Thought: God Loves Homosexuals",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'character', 'god', 'humanity', 'inclusion'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD LOVES HOMOSEXUALS",
    ctype: "THOUGHT",
    en_title: "God Loves Homosexuals",
    en_content: "God loves homosexuals.",
    es_title: "Dios Ama a los Homosexuales",
    es_content: "Dios ama a los homosexuales.",
    fr_title: "Dieu Aime les Homosexuels",
    fr_content: "Dieu aime les homosexuels.",
    hi_title: "ईश्वर समलैंगिकों से प्रेम करता है",
    hi_content: "ईश्वर समलैंगिकों से प्रेम करता है।",
    zh_title: "Shàngdì ài tóngxìngliàn zhě",
    zh_content: "Shàngdì ài tóngxìngliàn zhě."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD LOVES HOMOSEXUALS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD LOVES HOMOSEXUALS"
RETURN t, parent;
```
