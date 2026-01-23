---
name: "thought.GOD IS RICH"
alias: "Thought: God Is Rich"
type: THOUGHT
en_content: "God ain't broke."
parent: "topic.THE GODHEAD"
tags:
- provision
- abundance
- wealth
- god
- majesty
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.GOD IS RICH",
    alias: "Thought: God Is Rich",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'abundance', 'wealth', 'god', 'majesty'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD IS RICH",
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

MATCH (t:THOUGHT {name: "thought.GOD IS RICH"})
MATCH (c:CONTENT {name: "content.GOD IS RICH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS RICH" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD IS RICH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD IS RICH" }]->(child);
```
