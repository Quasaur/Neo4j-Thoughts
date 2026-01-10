---
name: "thought.EMULATING GODS CHARACTER"
alias: "Thought: Emulating Gods Character"
type: THOUGHT
en_content: "What kind of person is God? The kind I've always admired and desired to emulate."
parent: "topic.THE GODHEAD"
tags:
- character
- emulation
- admiration
- god
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2012b)
CREATE (t:THOUGHT {
    name: "thought.EMULATING GODS CHARACTER",
    alias: "Thought: Emulating Gods Character",
    parent: "topic.THE GODHEAD",
    tags: ['character', 'emulation', 'admiration', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EMULATING GODS CHARACTER",
    en_title: "Emulating Gods Character",
    en_content: "What kind of person is God? The kind I've always admired and desired to emulate.",
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
WHERE t.name = "thought.EMULATING GODS CHARACTER" AND c.name = "content.EMULATING GODS CHARACTER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EMULATING GODS CHARACTER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EMULATING GODS CHARACTER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >EMULATING GODS CHARACTER" }]->(child);
```
