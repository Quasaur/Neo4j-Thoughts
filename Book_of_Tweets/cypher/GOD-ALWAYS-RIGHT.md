---
name: "thought.GOD ALWAYS RIGHT"
alias: "Thought: God Always Right"
type: THOUGHT
en_content: "Only God is right about everything."
parent: "topic.THE GODHEAD"
tags:
- truth
- perfection
- god
- divinity
- wisdom
level: 1
neo4j: true
insert: true
---
# God Always Right

> [!Thought-en]
> Only God is right about everything.

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Mar-2013a)
CREATE (t:THOUGHT {
    name: "thought.GOD ALWAYS RIGHT",
    alias: "Thought: God Always Right",
    parent: "topic.THE GODHEAD",
    tags: ['truth', 'perfection', 'god', 'divinity', 'wisdom'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD ALWAYS RIGHT",
    en_title: "God Always Right",
    en_content: "Only God is right about everything.",
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
WHERE t.name = "thought.GOD ALWAYS RIGHT" AND c.name = "content.GOD ALWAYS RIGHT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD ALWAYS RIGHT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD ALWAYS RIGHT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD ALWAYS RIGHT" }]->(child);
```