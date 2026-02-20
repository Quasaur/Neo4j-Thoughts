---
name: "thought.UNFORGIVABLE SIN"
alias: "Thought: Unforgivable Sin"
type: THOUGHT
parent: "topic.MERCY"
en_content: "What is the Unforgiveable Sin? Unforgiveness."
tags:
- forgiveness
- sin
- grace
- judgment
- mercy
level: 5
neo4j: true
ptopic: "[[topic-MERCY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.UNFORGIVABLE SIN",
    alias: "Thought: Unforgivable Sin",
    parent: "topic.MERCY",
    tags: ['forgiveness', 'sin', 'grace', 'judgment', 'mercy'],
    level: 5
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
    zh_title: "bù kě ráo shù de zuì niè",
    zh_content: "shén me shì bù kě ráo shù de zuì ？ bù kuān shù 。"
});

MATCH (t:THOUGHT {name: "thought.UNFORGIVABLE SIN"})
MATCH (c:CONTENT {name: "content.UNFORGIVABLE SIN"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.UNFORGIVABLE SIN" }]->(c);

MATCH (parent:TOPIC {name: "topic.MERCY"})
MATCH (child:THOUGHT {name: "thought.UNFORGIVABLE SIN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.MERCY->UNFORGIVABLE SIN" }]->(child);
```
