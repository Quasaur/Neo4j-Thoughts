---
name: "thought.GOD NOT DEADBEAT"
alias: "Thought: God Not Deadbeat"
type: THOUGHT
en_content: "God is not a deadbeat... He takes care of His own."
parent: "topic.THE GODHEAD"
tags:
- provision
- care
- god
- character
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Jun-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD NOT DEADBEAT",
    alias: "Thought: God Not Deadbeat",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'care', 'god', 'character', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD NOT DEADBEAT",
    en_title: "God Not Deadbeat",
    en_content: "God is not a deadbeat... He takes care of His own.",
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
WHERE t.name = "thought.GOD NOT DEADBEAT" AND c.name = "content.GOD NOT DEADBEAT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD NOT DEADBEAT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD NOT DEADBEAT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD NOT DEADBEAT" }]->(child);
```
