---
name: "thought.GOD NOT AMERICAN"
alias: "Thought: God Not American"
type: THOUGHT
en_content: "God is NOT an American."
parent: "topic.THE GODHEAD"
tags:
- god
- politics
- nation
- character
- truth
level: 1
neo4j: true
insert: true
---
# God Not American

> [!Thought-en]
> God is NOT an American.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD NOT AMERICAN",
    alias: "Thought: God Not American",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'politics', 'nation', 'character', 'truth'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD NOT AMERICAN",
    en_title: "God Not American",
    en_content: "God is NOT an American.",
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
WHERE t.name = "thought.GOD NOT AMERICAN" AND c.name = "content.GOD NOT AMERICAN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD NOT AMERICAN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD NOT AMERICAN"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD NOT AMERICAN" }]->(child);
```