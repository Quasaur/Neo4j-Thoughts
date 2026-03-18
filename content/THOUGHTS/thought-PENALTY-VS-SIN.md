---
type: THOUGHT
name: "thought.PENALTY VS SIN"
alias: "Thought: Penalty Vs Sin"
parent: "topic.GRACE"
en_content: "We want to be saved from the PENALTY of sin but not sin itself."
tags: ["sin", "penalty", "salvation", "grace", "sanctification"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PENALTY VS SIN",
    alias: "Thought: Penalty Vs Sin",
    parent: "topic.GRACE",
    tags: ['sin', 'penalty', 'salvation', 'grace', 'sanctification'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PENALTY VS SIN",
    ctype: "THOUGHT",
    en_title: "Penalty Vs Sin",
    en_content: "We want to be saved from the PENALTY of sin but not sin itself.",
    es_title: "Castigo Vs Pecado",
    es_content: "Queremos ser salvos del CASTIGO del pecado pero no del pecado mismo.",
    fr_title: "Châtiment Vs Péché",
    fr_content: "Nous voulons être sauvés du CHÂTIMENT du péché mais pas du péché lui-même.",
    hi_title: "दंड बनाम पाप",
    hi_content: "हम पाप के दंड से मुक्ति चाहते हैं लेकिन पाप से नहीं।",
    zh_title: "Xingfa Dui Zuie",
    zh_content: "Women xiang cong zuie de XINGFA zhong dedao zhengiu, dan bu xiang cong zuie benshen zhong dedao zhengiu."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PENALTY VS SIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->PENALTY VS SIN"
RETURN t, parent;
```
