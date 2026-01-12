---
name: "thought.SPIRIT IS LIFE"
alias: "Thought: Spirit Is Life"
type: THOUGHT
en_content: "Spirit, not electricity, is Life."
parent: "topic.THE GODHEAD"
tags:
- spirit
- life
- science
- power
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT IS LIFE",
    alias: "Thought: Spirit Is Life",
    parent: "topic.THE GODHEAD",
    tags: ['spirit', 'life', 'science', 'power', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SPIRIT IS LIFE",
    en_title: "Spirit Is Life",
    en_content: "Spirit, not electricity, is Life.",
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
WHERE t.name = "thought.SPIRIT IS LIFE" AND c.name = "content.SPIRIT IS LIFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT IS LIFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.SPIRIT IS LIFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >SPIRIT IS LIFE" }]->(child);
```
