---
name: "thought.NOTHING WRONG GOD"
alias: "Thought: Nothing Wrong God"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- character
- perfection
- god
- divinity
- truth
level: 1
neo4j: true
insert: true
---
# Nothing Wrong God

> [!Thought-en]
> There is nothing wrong with God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Feb-2013)
CREATE (t:THOUGHT {
    name: "thought.NOTHING WRONG GOD",
    alias: "Thought: Nothing Wrong God",
    parent: "topic.THE GODHEAD",
    tags: ['character', 'perfection', 'god', 'divinity', 'truth'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOTHING WRONG GOD",
    en_title: "Nothing Wrong God",
    en_content: "There is nothing wrong with God.",
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
WHERE t.name = "thought.NOTHING WRONG GOD" AND c.name = "content.NOTHING WRONG GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING WRONG GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NOTHING WRONG GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NOTHING WRONG GOD" }]->(child);
```