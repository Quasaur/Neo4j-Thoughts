---
name: "thought.INVISIBLE IN IMPOSSIBLE"
alias: "Thought: Invisible In Impossible"
type: THOUGHT
en_content: "God is invisible except in the impossible."
parent: "topic.THE GODHEAD"
tags:
- god
- miracle
- invisible
- impossible
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.INVISIBLE IN IMPOSSIBLE",
    alias: "Thought: Invisible In Impossible",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'miracle', 'invisible', 'impossible', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.INVISIBLE IN IMPOSSIBLE",
    en_title: "Invisible In Impossible",
    en_content: "God is invisible except in the impossible.",
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
WHERE t.name = "thought.INVISIBLE IN IMPOSSIBLE" AND c.name = "content.INVISIBLE IN IMPOSSIBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INVISIBLE IN IMPOSSIBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.INVISIBLE IN IMPOSSIBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >INVISIBLE IN IMPOSSIBLE" }]->(child);
```
