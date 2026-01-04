---
name: "thought.GOD ACTUALLY EXISTS"
alias: "Thought: God Actually Exists"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- existence
- god
- fear
- truth
- divinity
level: 1
neo4j: true
insert: true
---
# God Actually Exists

> [!Thought-en]
> The idea that a Being such as That described in the Bible (God) actually exists should frighten us all...and it will.

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD ACTUALLY EXISTS",
    alias: "Thought: God Actually Exists",
    parent: "topic.THE GODHEAD",
    tags: ['existence', 'god', 'fear', 'truth', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD ACTUALLY EXISTS",
    en_title: "God Actually Exists",
    en_content: "The idea that a Being such as That described in the Bible (God) actually exists should frighten us all...and it will.",
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
WHERE t.name = "thought.GOD ACTUALLY EXISTS" AND c.name = "content.GOD ACTUALLY EXISTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD ACTUALLY EXISTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD ACTUALLY EXISTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD ACTUALLY EXISTS" }]->(child);
```