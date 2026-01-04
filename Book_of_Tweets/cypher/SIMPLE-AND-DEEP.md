---
name: "thought.SIMPLE AND DEEP"
alias: "Thought: Simple And Deep"
type: THOUGHT
parent: "topic.WISDOM"
tags:
- wisdom
- simplicity
- depth
- truth
- philosophy
level: 3
neo4j: true
insert: true
---
# Simple And Deep

> [!Thought-en]
> The simplest things are the most deep; the deepest things are the most simple.

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.SIMPLE AND DEEP",
    alias: "Thought: Simple And Deep",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'simplicity', 'depth', 'truth', 'philosophy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIMPLE AND DEEP",
    en_title: "Simple And Deep",
    en_content: "The simplest things are the most deep; the deepest things are the most simple.",
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
WHERE t.name = "thought.SIMPLE AND DEEP" AND c.name = "content.SIMPLE AND DEEP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIMPLE AND DEEP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.SIMPLE AND DEEP"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >SIMPLE AND DEEP" }]->(child);
```