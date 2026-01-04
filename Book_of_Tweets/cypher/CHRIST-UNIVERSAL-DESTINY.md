---
name: "thought.CHRIST UNIVERSAL DESTINY"
alias: "Thought: Christ Universal Destiny"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- christ
- destiny
- eternity
- divinity
- hope
level: 1
neo4j: true
insert: true
---
# Christ Universal Destiny

> [!Thought-en]
> Christ is everyone's Destiny...no exceptions!

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2012b)
CREATE (t:THOUGHT {
    name: "thought.CHRIST UNIVERSAL DESTINY",
    alias: "Thought: Christ Universal Destiny",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'destiny', 'eternity', 'divinity', 'hope'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CHRIST UNIVERSAL DESTINY",
    en_title: "Christ Universal Destiny",
    en_content: "Christ is everyone's Destiny...no exceptions!",
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
WHERE t.name = "thought.CHRIST UNIVERSAL DESTINY" AND c.name = "content.CHRIST UNIVERSAL DESTINY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRIST UNIVERSAL DESTINY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CHRIST UNIVERSAL DESTINY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CHRIST UNIVERSAL DESTINY" }]->(child);
```