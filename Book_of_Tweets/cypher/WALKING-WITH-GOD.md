---
name: "thought.WALKING WITH GOD"
alias: "Thought: Walking With God"
type: THOUGHT
en_content: "The Bible doesn't say that God walked with Enoch, but that Enoch walked with God. Enoch was led by the Holy Spirit."
parent: "topic.SPIRITUALITY"
tags:
- holyspirit
- enoch
- spirituality
- obedience
- fellowship
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.WALKING WITH GOD",
    alias: "Thought: Walking With God",
    parent: "topic.SPIRITUALITY",
    tags: ['holyspirit', 'enoch', 'spirituality', 'obedience', 'fellowship'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WALKING WITH GOD",
    en_title: "Walking With God",
    en_content: "The Bible doesn't say that God walked with Enoch, but that Enoch walked with God. Enoch was led by the Holy Spirit.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WALKING WITH GOD" AND c.name = "content.WALKING WITH GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WALKING WITH GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.WALKING WITH GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >WALKING WITH GOD" }]->(child);
```
