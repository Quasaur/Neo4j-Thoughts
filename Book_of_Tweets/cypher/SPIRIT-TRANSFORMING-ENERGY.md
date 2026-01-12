---
name: "thought.SPIRIT TRANSFORMING ENERGY"
alias: "Thought: Spirit Transforming Energy"
type: THOUGHT
en_content: "SPIRIT is so powerful; He can take frozen energy and transform it into Living Energy!"
parent: "topic.THE GODHEAD"
tags:
- spirit
- energy
- transformation
- power
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT TRANSFORMING ENERGY",
    alias: "Thought: Spirit Transforming Energy",
    parent: "topic.THE GODHEAD",
    tags: ['spirit', 'energy', 'transformation', 'power', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SPIRIT TRANSFORMING ENERGY",
    en_title: "Spirit Transforming Energy",
    en_content: "SPIRIT is so powerful; He can take frozen energy and transform it into Living Energy!",
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
WHERE t.name = "thought.SPIRIT TRANSFORMING ENERGY" AND c.name = "content.SPIRIT TRANSFORMING ENERGY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT TRANSFORMING ENERGY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.SPIRIT TRANSFORMING ENERGY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >SPIRIT TRANSFORMING ENERGY" }]->(child);
```
