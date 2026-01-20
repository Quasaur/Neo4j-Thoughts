---
name: "thought.UNFORGIVABLE SIN"
alias: "Thought: Unforgivable Sin"
type: THOUGHT
en_content: "What is the Unforgiveable Sin? Unforgiveness."
parent: "topic.GRACE"
tags:
- forgiveness
- sin
- grace
- judgment
- mercy
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.UNFORGIVABLE SIN",
    alias: "Thought: Unforgivable Sin",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'sin', 'grace', 'judgment', 'mercy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNFORGIVABLE SIN",
    en_title: "Unforgivable Sin",
    en_content: "What is the Unforgiveable Sin? Unforgiveness.",
    es_title: "Pecado imperdonable",
    es_content: "¿Cuál es el pecado imperdonable?Falta de perdón.",
    fr_title: "Péché impardonnable",
    fr_content: "Quel est le péché impardonnable ?Le manque de pardon.",
    hi_title: "अक्षम्य पाप",
    hi_content: "अक्षम्य पाप क्या है?क्षमा न करना।",
    zh_title: "不可饶恕的罪孽",
    zh_content: "什么是不可饶恕的罪？不宽恕。"
});

MATCH (t:THOUGHT {name: "thought.UNFORGIVABLE SIN"})
MATCH (c:CONTENT {name: "content.UNFORGIVABLE SIN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNFORGIVABLE SIN" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.UNFORGIVABLE SIN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >UNFORGIVABLE SIN" }]->(child);
```
