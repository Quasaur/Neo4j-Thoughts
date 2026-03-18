---
type: THOUGHT
name: "thought.GOD LOVES KINDNESS"
alias: "Thought: God Loves Kindness"
parent: "topic.THE GODHEAD"
en_content: "God loves Kindness!"
tags: ["kindness", "character", "god", "love", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Jun-2012)
CREATE (t:THOUGHT {    name: "thought.GOD LOVES KINDNESS",
    alias: "Thought: God Loves Kindness",
    parent: "topic.THE GODHEAD",
    tags: ['kindness', 'character', 'god', 'love', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD LOVES KINDNESS",
    ctype: "THOUGHT",
    en_title: "God Loves Kindness",
    en_content: "God loves Kindness!",
    es_title: "Dios Ama la Bondad",
    es_content: "¡Dios ama la Bondad!",
    fr_title: "Dieu Aime la Bonté",
    fr_content: "Dieu aime la Bonté !",
    hi_title: "परमेश्वर दया से प्रेम करते हैं",
    hi_content: "परमेश्वर दया से प्रेम करते हैं!",
    zh_title: "Shàngdì ài shànláng  shàng dì ài shàn liáng",
    zh_content: "Shàngdì rè'ai shànláng!  shàng dì rè ài shàn liáng ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD LOVES KINDNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD LOVES KINDNESS"
RETURN t, parent;
```
