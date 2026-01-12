---
name: "thought.PENALTY VS SIN"
alias: "Thought: Penalty Vs Sin"
type: THOUGHT
en_content: "We want to be saved from the PENALTY of sin but not sin itself."
parent: "topic.GRACE"
tags:
- sin
- penalty
- salvation
- grace
- sanctification
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.PENALTY VS SIN",
    alias: "Thought: Penalty Vs Sin",
    parent: "topic.GRACE",
    tags: ['sin', 'penalty', 'salvation', 'grace', 'sanctification'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PENALTY VS SIN",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PENALTY VS SIN" AND c.name = "content.PENALTY VS SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PENALTY VS SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.PENALTY VS SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >PENALTY VS SIN" }]->(child);
```
