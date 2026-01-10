---
name: "thought.THE SUFFERING GOD"
alias: "Thought: The Suffering God"
type: THOUGHT
en_content: "In Christ God has suffered more than any human."
parent: "topic.THE GODHEAD"
tags:
- suffering
- empathy
- christ
- incarnation
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011e)
CREATE (t:THOUGHT {
    name: "thought.THE SUFFERING GOD",
    alias: "Thought: The Suffering God",
    parent: "topic.THE GODHEAD",
    tags: ['suffering', 'empathy', 'christ', 'incarnation', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE SUFFERING GOD",
    en_title: "The Suffering God",
    en_content: "In Christ God has suffered more than any human.",
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
WHERE t.name = "thought.THE SUFFERING GOD" AND c.name = "content.THE SUFFERING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE SUFFERING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE SUFFERING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >THE SUFFERING GOD" }]->(child);
```
