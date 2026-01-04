---
name: "thought.REJECTED CORNER STONE"
alias: "Thought: Rejected Corner Stone"
type: THOUGHT
en_content: "The Stone that the builders rejected...(smile)!"
parent: "topic.RELIGION"
tags:
- stone
- builders
- rejection
- jesus
level: 3
neo4j: true
insert: true
---
# Rejected Corner Stone

> [!Thought-en]
> The Stone that the builders rejected...(smile)!

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.REJECTED CORNER STONE",
    alias: "Thought: Rejected Corner Stone",
    parent: "topic.RELIGION",
    tags: ['stone', 'builders', 'rejection', 'jesus'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.REJECTED CORNER STONE",
    en_title: "Rejected Corner Stone",
    en_content: "The Stone that the builders rejected...(smile)!",
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
WHERE t.name = "thought.REJECTED CORNER STONE" AND c.name = "content.REJECTED CORNER STONE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REJECTED CORNER STONE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.REJECTED CORNER STONE"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >REJECTED CORNER STONE" }]->(child);
```