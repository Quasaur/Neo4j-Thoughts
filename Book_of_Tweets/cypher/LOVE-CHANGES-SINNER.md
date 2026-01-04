---
name: "thought.LOVE CHANGES SINNER"
alias: "Thought: Love Changes Sinner"
type: THOUGHT
parent: "topic.GRACE"
tags:
- love
- transformation
- grace
- salvation
- character
level: 3
neo4j: true
insert: true
---
# Love Changes Sinner

> [!Thought-en]
> It is the LOVE OF GOD that changes a sinner to a saint.

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.LOVE CHANGES SINNER",
    alias: "Thought: Love Changes Sinner",
    parent: "topic.GRACE",
    tags: ['love', 'transformation', 'grace', 'salvation', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE CHANGES SINNER",
    en_title: "Love Changes Sinner",
    en_content: "It is the LOVE OF GOD that changes a sinner to a saint.",
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
WHERE t.name = "thought.LOVE CHANGES SINNER" AND c.name = "content.LOVE CHANGES SINNER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE CHANGES SINNER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LOVE CHANGES SINNER"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LOVE CHANGES SINNER" }]->(child);
```