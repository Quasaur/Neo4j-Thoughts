---
name: "thought.SEAT OF POWER"
alias: "Thought: Seat Of Power"
type: THOUGHT
en_content: "The Seat of True Power is in Heaven, where the Christ patiently waits for His Daddy to turn His Enemies into His footrest."
parent: "topic.THE GODHEAD"
tags:
- power
- heaven
- christ
- enemies
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Apr-2014)
CREATE (t:THOUGHT {
    name: "thought.SEAT OF POWER",
    alias: "Thought: Seat Of Power",
    parent: "topic.THE GODHEAD",
    tags: ['power', 'heaven', 'christ', 'enemies'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SEAT OF POWER",
    en_title: "Seat Of Power",
    en_content: "The Seat of True Power is in Heaven, where the Christ patiently waits for His Daddy to turn His Enemies into His footrest.",
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
WHERE t.name = "thought.SEAT OF POWER" AND c.name = "content.SEAT OF POWER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SEAT OF POWER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.SEAT OF POWER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >SEAT OF POWER" }]->(child);
```
