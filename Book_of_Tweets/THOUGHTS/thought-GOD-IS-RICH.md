---
type: THOUGHT
name: "thought.GOD IS RICH"
alias: "Thought: God Is Rich"
parent: "topic.THE GODHEAD"
en_content: "God ain't broke."
tags: ["provision", "abundance", "wealth", "god", "majesty"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Jan-2012a)
CREATE (t:THOUGHT {    name: "thought.GOD IS RICH",
    alias: "Thought: God Is Rich",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'abundance', 'wealth', 'god', 'majesty'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD IS RICH",
    ctype: "THOUGHT",
    en_title: "God Is Rich",
    en_content: "God ain't broke.",
    es_title: "Dios Es Rico",
    es_content: "Dios no está quebrado.",
    fr_title: "Dieu Est Riche",
    fr_content: "Dieu n'est pas fauché.",
    hi_title: "ईश्वर धनी है",
    hi_content: "ईश्वर दरिद्र नहीं है।",
    zh_title: "Shén shì fùyǒu de",
    zh_content: "Shén bù pínqióng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD IS RICH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD IS RICH"
RETURN t, parent;
```
