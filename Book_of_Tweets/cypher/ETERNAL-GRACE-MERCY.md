---
name: "thought.ETERNAL GRACE MERCY"
alias: "Thought: Eternal Grace Mercy"
type: THOUGHT
en_content: "Psalm 136: Grace, Mercy and Kindness will never be obsolete; they endure forever."
parent: "topic.THE GODHEAD"
tags:
- grace
- mercy
- kindness
- eternity
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.ETERNAL GRACE MERCY",
    alias: "Thought: Eternal Grace Mercy",
    parent: "topic.THE GODHEAD",
    tags: ['grace', 'mercy', 'kindness', 'eternity', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ETERNAL GRACE MERCY",
    en_title: "Eternal Grace Mercy",
    en_content: "Psalm 136: Grace, Mercy and Kindness will never be obsolete; they endure forever.",
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
WHERE t.name = "thought.ETERNAL GRACE MERCY" AND c.name = "content.ETERNAL GRACE MERCY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ETERNAL GRACE MERCY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ETERNAL GRACE MERCY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ETERNAL GRACE MERCY" }]->(child);
```
