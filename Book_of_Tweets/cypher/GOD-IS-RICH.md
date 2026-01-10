---
name: "thought.GOD IS RICH"
alias: "Thought: God Is Rich"
type: THOUGHT
en_content: "God ain't broke."
parent: "topic.THE GODHEAD"
tags:
- provision
- abundance
- wealth
- god
- majesty
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.GOD IS RICH",
    alias: "Thought: God Is Rich",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'abundance', 'wealth', 'god', 'majesty'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD IS RICH",
    en_title: "God Is Rich",
    en_content: "God ain't broke.",
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
WHERE t.name = "thought.GOD IS RICH" AND c.name = "content.GOD IS RICH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS RICH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD IS RICH"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD IS RICH" }]->(child);
```
