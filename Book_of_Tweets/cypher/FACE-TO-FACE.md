---
name: "thought.FACE TO FACE"
alias: "Thought: Face To Face"
type: THOUGHT
en_content: "When you meet God face to Face you will not ask any questions; His Glory is the answer to every question and the end of every dispute."
parent: "topic.THE GODHEAD"
tags:
- glory
- encounter
- presence
- truth
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011b)
CREATE (t:THOUGHT {
    name: "thought.FACE TO FACE",
    alias: "Thought: Face To Face",
    parent: "topic.THE GODHEAD",
    tags: ['glory', 'encounter', 'presence', 'truth', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.FACE TO FACE",
    en_title: "Face To Face",
    en_content: "When you meet God face to Face you will not ask any questions; His Glory is the answer to every question and the end of every dispute.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FACE TO FACE" AND c.name = "content.FACE TO FACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FACE TO FACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.FACE TO FACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >FACE TO FACE" }]->(child);
```
