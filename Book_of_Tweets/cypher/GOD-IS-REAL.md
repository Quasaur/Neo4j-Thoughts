---
name: "thought.GOD IS REAL"
alias: "Thought: God Is Real"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- real
- truth
- uncertainty
- god
level: 1
neo4j: true
insert: true
---
# God Is Real

> [!Thought-en]
> In these uncertain times GOD IS REAL...but not much else.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jun-2014)
CREATE (t:THOUGHT {
    name: "thought.GOD IS REAL",
    alias: "Thought: God Is Real",
    parent: "topic.THE GODHEAD",
    tags: ['real', 'truth', 'uncertainty', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD IS REAL",
    en_title: "God Is Real",
    en_content: "In these uncertain times GOD IS REAL...but not much else.",
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
WHERE t.name = "thought.GOD IS REAL" AND c.name = "content.GOD IS REAL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS REAL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD IS REAL"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD IS REAL" }]->(child);
```