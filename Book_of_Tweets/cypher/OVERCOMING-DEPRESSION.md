---
name: "thought.OVERCOMING DEPRESSION"
alias: "Thought: Overcoming Depression"
type: THOUGHT
en_content: "Long after the point when Depression ceases to be a memory...I will still be here."
parent: "topic.PSYCHOLOGY"
tags:
- depression
- healing
- persistence
- psychology
- hope
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011a)
CREATE (t:THOUGHT {
    name: "thought.OVERCOMING DEPRESSION",
    alias: "Thought: Overcoming Depression",
    parent: "topic.PSYCHOLOGY",
    tags: ['depression', 'healing', 'persistence', 'psychology', 'hope'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OVERCOMING DEPRESSION",
    en_title: "Overcoming Depression",
    en_content: "Long after the point when Depression ceases to be a memory...I will still be here.",
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
WHERE t.name = "thought.OVERCOMING DEPRESSION" AND c.name = "content.OVERCOMING DEPRESSION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OVERCOMING DEPRESSION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.OVERCOMING DEPRESSION"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >OVERCOMING DEPRESSION" }]->(child);
```
