---
name: "thought.RELENTLESS LOVE"
alias: "Thought: Relentless Love"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- love
- character
- god
- persistence
- divinity
level: 1
neo4j: true
insert: true
---
# Relentless Love

> [!Thought-en]
> Love is ruthless...relentless...persistent and unflagging...thank God!

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.RELENTLESS LOVE",
    alias: "Thought: Relentless Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'character', 'god', 'persistence', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RELENTLESS LOVE",
    en_title: "Relentless Love",
    en_content: "Love is ruthless...relentless...persistent and unflagging...thank God!",
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
WHERE t.name = "thought.RELENTLESS LOVE" AND c.name = "content.RELENTLESS LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RELENTLESS LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.RELENTLESS LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >RELENTLESS LOVE" }]->(child);
```