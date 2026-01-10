---
name: "thought.PENALTY VS SIN"
alias: "Thought: Penalty Vs Sin"
type: THOUGHT
en_content: "We want to be saved from the PENALTY of sin but not sin itself."
parent: "topic.GRACE"
tags:
- sin
- penalty
- salvation
- grace
- sanctification
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.PENALTY VS SIN",
    alias: "Thought: Penalty Vs Sin",
    parent: "topic.GRACE",
    tags: ['sin', 'penalty', 'salvation', 'grace', 'sanctification'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PENALTY VS SIN",
    en_title: "Penalty Vs Sin",
    en_content: "We want to be saved from the PENALTY of sin but not sin itself.",
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
WHERE t.name = "thought.PENALTY VS SIN" AND c.name = "content.PENALTY VS SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PENALTY VS SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.PENALTY VS SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >PENALTY VS SIN" }]->(child);
```
