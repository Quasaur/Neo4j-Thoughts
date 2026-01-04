---
name: "thought.GOD THE RECYCLER"
alias: "Thought: God The Recycler"
type: THOUGHT
parent: "topic.CREATION"
tags:
- recycling
- creation
- god
- restoration
- humor
level: 2
neo4j: true
insert: true
---
# God The Recycler

> [!Thought-en]
> God recycles.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.GOD THE RECYCLER",
    alias: "Thought: God The Recycler",
    parent: "topic.CREATION",
    tags: ['recycling', 'creation', 'god', 'restoration', 'humor'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD THE RECYCLER",
    en_title: "God The Recycler",
    en_content: "God recycles.",
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
WHERE t.name = "thought.GOD THE RECYCLER" AND c.name = "content.GOD THE RECYCLER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD THE RECYCLER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.GOD THE RECYCLER"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >GOD THE RECYCLER" }]->(child);
```