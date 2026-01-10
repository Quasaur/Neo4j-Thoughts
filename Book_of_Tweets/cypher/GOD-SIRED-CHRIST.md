---
name: "thought.GOD SIRED CHRIST"
alias: "Thought: God Sired Christ"
type: THOUGHT
en_content: "God did not create Christ, He SIRED Him! That's why Jesus is called THE ONLY BEGOTTEN of the Father."
parent: "topic.THE GODHEAD"
tags:
- christ
- begotten
- sired
- god
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD SIRED CHRIST",
    alias: "Thought: God Sired Christ",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'begotten', 'sired', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD SIRED CHRIST",
    en_title: "God Sired Christ",
    en_content: "God did not create Christ, He SIRED Him! That's why Jesus is called THE ONLY BEGOTTEN of the Father.",
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
WHERE t.name = "thought.GOD SIRED CHRIST" AND c.name = "content.GOD SIRED CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD SIRED CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD SIRED CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD SIRED CHRIST" }]->(child);
```
