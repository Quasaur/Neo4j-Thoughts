---
name: "thought.PURSUIT OF HAPPINESS"
alias: "Thought: Pursuit Of Happiness"
type: THOUGHT
en_content: "The pursuit of God is the pursuit of happiness. The pursuit of happiness is the pursuit of God."
parent: "topic.THE GODHEAD"
tags:
- god
- happiness
- pursuit
- divinity
- truth
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.PURSUIT OF HAPPINESS",
    alias: "Thought: Pursuit Of Happiness",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'happiness', 'pursuit', 'divinity', 'truth'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PURSUIT OF HAPPINESS",
    en_title: "Pursuit Of Happiness",
    en_content: "The pursuit of God is the pursuit of happiness. The pursuit of happiness is the pursuit of God.",
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
WHERE t.name = "thought.PURSUIT OF HAPPINESS" AND c.name = "content.PURSUIT OF HAPPINESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PURSUIT OF HAPPINESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.PURSUIT OF HAPPINESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >PURSUIT OF HAPPINESS" }]->(child);
```
