---
name: "thought.GOD LOVES ABUSERS"
alias: "Thought: God Loves Abusers"
type: THOUGHT
en_content: "God loves abusers."
parent: "topic.THE GODHEAD"
tags:
- love
- god
- abusers
- mercy
- character
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Feb-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD LOVES ABUSERS",
    alias: "Thought: God Loves Abusers",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'god', 'abusers', 'mercy', 'character'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD LOVES ABUSERS",
    en_title: "God Loves Abusers",
    en_content: "God loves abusers.",
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
WHERE t.name = "thought.GOD LOVES ABUSERS" AND c.name = "content.GOD LOVES ABUSERS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD LOVES ABUSERS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD LOVES ABUSERS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD LOVES ABUSERS" }]->(child);
```
