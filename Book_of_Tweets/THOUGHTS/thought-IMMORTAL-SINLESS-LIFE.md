---
type: THOUGHT
name: "thought.IMMORTAL SINLESS LIFE"
alias: "Thought: Immortal Sinless Life"
parent: "topic.THE GODHEAD"
en_content: "An immortal life is a sinless life."
tags: ["immortality", "holiness", "life", "sin", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jan-2012)
CREATE (t:THOUGHT {    name: "thought.IMMORTAL SINLESS LIFE",
    alias: "Thought: Immortal Sinless Life",
    parent: "topic.THE GODHEAD",
    tags: ['immortality', 'holiness', 'life', 'sin', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.IMMORTAL SINLESS LIFE",
    ctype: "THOUGHT",
    en_title: "Immortal Sinless Life",
    en_content: "An immortal life is a sinless life.",
    es_title: "Vida Inmortal Sin Pecado",
    es_content: "Una vida inmortal es una vida sin pecado.",
    fr_title: "Vie Immortelle Sans Péché",
    fr_content: "Une vie immortelle est une vie sans péché.",
    hi_title: "अमर निष्पाप जीवन",
    hi_content: "एक अमर जीवन एक निष्पाप जीवन है।",
    zh_title: "Bu xiu wu zui sheng ming",
    zh_content: "Bu xiu de sheng ming shi wu zui de sheng ming."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IMMORTAL SINLESS LIFE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->IMMORTAL SINLESS LIFE"
RETURN t, parent;
```
