---
name: "thought.GOD TALKING BACK"
alias: "Thought: God Talking Back"
type: THOUGHT
en_content: "\"YOU DO NOT TALK TO ME.\" - God"
parent: "topic.THE GODHEAD"
tags:
- communication
- god
- presence
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD TALKING BACK",
    alias: "Thought: God Talking Back",
    parent: "topic.THE GODHEAD",
    tags: ['communication', 'god', 'presence', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD TALKING BACK",
    en_title: "God Talking Back",
    en_content: "\"YOU DO NOT TALK TO ME.\" - God",
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
WHERE t.name = "thought.GOD TALKING BACK" AND c.name = "content.GOD TALKING BACK"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD TALKING BACK" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD TALKING BACK"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD TALKING BACK" }]->(child);
```
