---
name: "thought.SHADOWS OF CHRIST"
alias: "Thought: Shadows Of Christ"
type: THOUGHT
en_content: "That which is most precious to us...and those whom we love more than life are but shadows of the Figure of Christ!"
parent: "topic.THE GODHEAD"
tags:
- christ
- shadows
- reality
- love
- figure
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.SHADOWS OF CHRIST",
    alias: "Thought: Shadows Of Christ",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'shadows', 'reality', 'love', 'figure'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SHADOWS OF CHRIST",
    en_title: "Shadows Of Christ",
    en_content: "That which is most precious to us...and those whom we love more than life are but shadows of the Figure of Christ!",
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
WHERE t.name = "thought.SHADOWS OF CHRIST" AND c.name = "content.SHADOWS OF CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHADOWS OF CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.SHADOWS OF CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >SHADOWS OF CHRIST" }]->(child);
```
