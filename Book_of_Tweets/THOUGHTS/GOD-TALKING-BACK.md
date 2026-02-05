---
name: "thought.GOD TALKING BACK"
alias: "Thought: God Talking Back"
type: THOUGHT
en_content: "\"YOU DO NOT TALK TO ME.\" - God"
parent: "topic.THE GODHEAD"
tags:
- communication
- god
- presence
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD TALKING BACK",
    alias: "Thought: God Talking Back",
    parent: "topic.THE GODHEAD",
    tags: ['communication', 'god', 'presence', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD TALKING BACK",
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

MATCH (t:THOUGHT {name: "thought.GOD TALKING BACK"})
MATCH (c:CONTENT {name: "content.GOD TALKING BACK"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD TALKING BACK" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD TALKING BACK"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD TALKING BACK" }]->(child);
```
