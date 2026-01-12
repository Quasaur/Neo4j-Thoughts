---
name: "thought.THE FIRST SIN"
alias: "Thought: The First Sin"
type: THOUGHT
en_content: "The First Sinner committed the First Sin by taking the credit for that which he did not create: himself."
parent: "topic.HUMANITY"
tags:
- sin
- pride
- creation
- identity
- humanity
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.THE FIRST SIN",
    alias: "Thought: The First Sin",
    parent: "topic.HUMANITY",
    tags: ['sin', 'pride', 'creation', 'identity', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THE FIRST SIN",
    en_title: "The First Sin",
    en_content: "The First Sinner committed the First Sin by taking the credit for that which he did not create: himself.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE FIRST SIN" AND c.name = "content.THE FIRST SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE FIRST SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.THE FIRST SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >THE FIRST SIN" }]->(child);
```
