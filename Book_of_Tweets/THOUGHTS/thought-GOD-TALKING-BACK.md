---
type: THOUGHT
name: "thought.GOD TALKING BACK"
alias: "Thought: God Talking Back"
parent: "topic.THE GODHEAD"
en_content: "\"YOU DO NOT TALK TO ME.\" - God"
tags: ["communication", "god", "presence", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Nov-2013)
CREATE (t:THOUGHT {    name: "thought.GOD TALKING BACK",
    alias: "Thought: God Talking Back",
    parent: "topic.THE GODHEAD",
    tags: ['communication', 'god', 'presence', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD TALKING BACK",
    ctype: "THOUGHT",
    en_title: "God Talking Back",
    en_content: "\"YOU DO NOT TALK TO ME.\" - God",
    es_title: "Dios respondiendo",
    es_content: "\",
    fr_title: "Dieu répond",
    fr_content: "\",
    hi_title: "भगवान वापस बात कर रहे हैं",
    hi_content: "\",
    zh_title: "shén huí huà",
    zh_content: "\"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD TALKING BACK"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD TALKING BACK"
RETURN t, parent;
```
