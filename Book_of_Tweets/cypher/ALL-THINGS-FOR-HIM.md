---
name: "thought.ALL THINGS FOR HIM"
alias: "Thought: All Things For Him"
type: THOUGHT
en_content: "All things are from, to and for Him; this is fitting, for He is worthy."
parent: "topic.THE GODHEAD"
tags:
- worthyship
- glory
- divinity
- creation
- worship
level: 1
neo4j: true
insert: true
---
# All Things For Him

> [!Thought-en]
> All things are from, to and for Him; this is fitting, for He is worthy.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011b)
CREATE (t:THOUGHT {
    name: "thought.ALL THINGS FOR HIM",
    alias: "Thought: All Things For Him",
    parent: "topic.THE GODHEAD",
    tags: ['worthyship', 'glory', 'divinity', 'creation', 'worship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ALL THINGS FOR HIM",
    en_title: "All Things For Him",
    en_content: "All things are from, to and for Him; this is fitting, for He is worthy.",
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
WHERE t.name = "thought.ALL THINGS FOR HIM" AND c.name = "content.ALL THINGS FOR HIM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALL THINGS FOR HIM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ALL THINGS FOR HIM"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ALL THINGS FOR HIM" }]->(child);
```