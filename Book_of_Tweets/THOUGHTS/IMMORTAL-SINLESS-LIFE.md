---
name: "thought.IMMORTAL SINLESS LIFE"
alias: "Thought: Immortal Sinless Life"
type: THOUGHT
en_content: "An immortal life is a sinless life."
parent: "topic.THE GODHEAD"
tags:
- immortality
- holiness
- life
- sin
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.IMMORTAL SINLESS LIFE",
    alias: "Thought: Immortal Sinless Life",
    parent: "topic.THE GODHEAD",
    tags: ['immortality', 'holiness', 'life', 'sin', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.IMMORTAL SINLESS LIFE",
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

MATCH (t:THOUGHT {name: "thought.IMMORTAL SINLESS LIFE"})
MATCH (c:CONTENT {name: "content.IMMORTAL SINLESS LIFE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.IMMORTAL SINLESS LIFE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.IMMORTAL SINLESS LIFE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >IMMORTAL SINLESS LIFE" }]->(child);
```
