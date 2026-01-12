---
name: "thought.SELF TORTURE OWNERSHIP"
alias: "Thought: Self Torture Ownership"
type: THOUGHT
en_content: "Self-torture implies self-ownership."
parent: "topic.HUMANITY"
tags:
- ownership
- identity
- self
- humanity
- philosophy
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.SELF TORTURE OWNERSHIP",
    alias: "Thought: Self Torture Ownership",
    parent: "topic.HUMANITY",
    tags: ['ownership', 'identity', 'self', 'humanity', 'philosophy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF TORTURE OWNERSHIP",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF TORTURE OWNERSHIP" AND c.name = "content.SELF TORTURE OWNERSHIP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SELF TORTURE OWNERSHIP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.SELF TORTURE OWNERSHIP"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >SELF TORTURE OWNERSHIP" }]->(child);
```
