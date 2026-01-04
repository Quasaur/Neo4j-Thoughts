---
name: "thought.JESUS THE MONARCH"
alias: "Thought: Jesus The Monarch"
type: THOUGHT
en_content: "Jesus is neither a Republican nor a Democrat; Jesus is God...an Absolute Monarch."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- monarchy
- authority
- politics
- divinity
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Aug-2010a)
CREATE (t:THOUGHT {
    name: "thought.JESUS THE MONARCH",
    alias: "Thought: Jesus The Monarch",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'monarchy', 'authority', 'politics', 'divinity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JESUS THE MONARCH",
    en_title: "Jesus The Monarch",
    en_content: "Jesus is neither a Republican nor a Democrat; Jesus is God...an Absolute Monarch.",
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
WHERE t.name = "thought.JESUS THE MONARCH" AND c.name = "content.JESUS THE MONARCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS THE MONARCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.JESUS THE MONARCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >JESUS THE MONARCH" }]->(child);
```
