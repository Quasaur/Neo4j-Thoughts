---
type: THOUGHT
name: "thought.PROBLEM AND SOLUTION"
alias: "Thought: Problem And Solution"
parent: "topic.WISDOM"
en_content: "Identifying the problem is only half the solution."
tags: ["problem", "solution", "wisdom", "identification", "logic"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Jul-2013)
CREATE (t:THOUGHT {    name: "thought.PROBLEM AND SOLUTION",
    alias: "Thought: Problem And Solution",
    parent: "topic.WISDOM",
    tags: ['problem', 'solution', 'wisdom', 'identification', 'logic'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PROBLEM AND SOLUTION",
    ctype: "THOUGHT",
    en_title: "Problem And Solution",
    en_content: "Identifying the problem is only half the solution.",
    es_title: "Problema Y Solución",
    es_content: "Identificar el problema es solo la mitad de la solución.",
    fr_title: "Problème Et Solution",
    fr_content: "Identifier le problème n'est que la moitié de la solution.",
    hi_title: "समस्या और समाधान",
    hi_content: "समस्या की पहचान करना केवल समाधान का आधा हिस्सा है।",
    zh_title: "Wèntí Hé Jiějué",
    zh_content: "Shíbié wèntí zhǐshì jiějué fāng'àn de yībàn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PROBLEM AND SOLUTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->PROBLEM AND SOLUTION"
RETURN t, parent;
```
