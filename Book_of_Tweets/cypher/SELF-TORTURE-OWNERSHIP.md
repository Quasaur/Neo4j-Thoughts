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
insert: true
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
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
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
