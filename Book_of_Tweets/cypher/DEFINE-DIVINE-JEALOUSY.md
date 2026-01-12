---
name: "thought.DEFINE DIVINE JEALOUSY"
alias: "Thought: Define Divine Jealousy"
type: THOUGHT
en_content: "Divine Jealousy: Ownership in Love with Responsibility and Accountability."
parent: "topic.THE GODHEAD"
tags:
- jealousy
- ownership
- love
- responsibility
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.DEFINE DIVINE JEALOUSY",
    alias: "Thought: Define Divine Jealousy",
    parent: "topic.THE GODHEAD",
    tags: ['jealousy', 'ownership', 'love', 'responsibility', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.DEFINE DIVINE JEALOUSY",
    en_title: "Define Divine Jealousy",
    en_content: "Divine Jealousy: Ownership in Love with Responsibility and Accountability.",
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
WHERE t.name = "thought.DEFINE DIVINE JEALOUSY" AND c.name = "content.DEFINE DIVINE JEALOUSY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE DIVINE JEALOUSY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.DEFINE DIVINE JEALOUSY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >DEFINE DIVINE JEALOUSY" }]->(child);
```
