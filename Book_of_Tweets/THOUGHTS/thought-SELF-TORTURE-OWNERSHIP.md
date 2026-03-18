---
type: THOUGHT
name: "thought.SELF TORTURE OWNERSHIP"
alias: "Thought: Self Torture Ownership"
parent: "topic.HUMANITY"
en_content: "Self-torture implies self-ownership."
tags: ["ownership", "identity", "self", "humanity", "philosophy"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2011b)
CREATE (t:THOUGHT {    name: "thought.SELF TORTURE OWNERSHIP",
    alias: "Thought: Self Torture Ownership",
    parent: "topic.HUMANITY",
    tags: ['ownership', 'identity', 'self', 'humanity', 'philosophy'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SELF TORTURE OWNERSHIP",
    ctype: "THOUGHT",
    en_title: "Self Torture Ownership",
    en_content: "Self-torture implies self-ownership.",
    es_title: "Propiedad de la Auto-Tortura",
    es_content: "La auto-tortura implica auto-propiedad.",
    fr_title: "Propriété de l'Auto-Torture",
    fr_content: "L'auto-torture implique la propriété de soi.",
    hi_title: "आत्म-यंत्रणा स्वामित्व",
    hi_content: "आत्म-यंत्रणा आत्म-स्वामित्व को दर्शाता है।",
    zh_title: "Zi Wo Zhe Mo Suo You Quan",
    zh_content: "Zi wo zhe mo an han zi wo suo you quan."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SELF TORTURE OWNERSHIP"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->SELF TORTURE OWNERSHIP"
RETURN t, parent;
```
