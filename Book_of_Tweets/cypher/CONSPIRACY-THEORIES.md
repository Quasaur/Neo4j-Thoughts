---
name: "thought.CONSPIRACY THEORIES"
alias: "Thought: Conspiracy Theories"
type: THOUGHT
en_content: "I LOVE conspiracy theories...they allow me to pass responsibility for my failures to someone else!"
parent: "topic.UNDERSTANDING"
tags:
- responsibility
- failure
- wisdom
- truth
- deception
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2010b)
CREATE (t:THOUGHT {
    name: "thought.CONSPIRACY THEORIES",
    alias: "Thought: Conspiracy Theories",
    parent: "topic.UNDERSTANDING",
    tags: ['responsibility', 'failure', 'wisdom', 'truth', 'deception'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONSPIRACY THEORIES",
    en_title: "Conspiracy Theories",
    en_content: "I LOVE conspiracy theories...they allow me to pass responsibility for my failures to someone else!",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONSPIRACY THEORIES" AND c.name = "content.CONSPIRACY THEORIES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONSPIRACY THEORIES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.CONSPIRACY THEORIES"
MERGE (parent)-[:HAS_THOUGHT { "name": "UNDERSTANDING >CONSPIRACY THEORIES" }]->(child);
```
