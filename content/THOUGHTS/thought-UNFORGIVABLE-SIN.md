---
type: THOUGHT
name: "thought.UNFORGIVABLE SIN"
alias: "Thought: Unforgivable Sin"
parent: "topic.MERCY"
en_content: "What is the Unforgiveable Sin? Unforgiveness."
tags: ["forgiveness", "sin", "grace", "judgment", "mercy"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNFORGIVABLE SIN",
    alias: "Thought: Unforgivable Sin",
    parent: "topic.MERCY",
    tags: ['forgiveness', 'sin', 'grace', 'judgment', 'mercy'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.UNFORGIVABLE SIN",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNFORGIVABLE SIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MERCY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MERCY->UNFORGIVABLE SIN"
RETURN t, parent;
```
