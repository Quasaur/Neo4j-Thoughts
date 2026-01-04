---
name: "thought.GODS SUPERIOR VALUE"
alias: "Thought: Gods Superior Value"
type: THOUGHT
en_content: "In the REAL WORLD, God is more valuable than all of us put together."
parent: "topic.THE GODHEAD"
tags:
- value
- reality
- god
- majesty
- divinity
level: 1
neo4j: true
insert: true
---
# Gods Superior Value

> [!Thought-en]
> In the REAL WORLD, God is more valuable than all of us put together.

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.GODS SUPERIOR VALUE",
    alias: "Thought: Gods Superior Value",
    parent: "topic.THE GODHEAD",
    tags: ['value', 'reality', 'god', 'majesty', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS SUPERIOR VALUE",
    en_title: "Gods Superior Value",
    en_content: "In the REAL WORLD, God is more valuable than all of us put together.",
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
WHERE t.name = "thought.GODS SUPERIOR VALUE" AND c.name = "content.GODS SUPERIOR VALUE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS SUPERIOR VALUE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS SUPERIOR VALUE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS SUPERIOR VALUE" }]->(child);
```