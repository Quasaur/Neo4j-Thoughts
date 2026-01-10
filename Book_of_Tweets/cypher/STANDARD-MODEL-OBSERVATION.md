---
name: "thought.STANDARD MODEL OBSERVATION"
alias: "Thought: Standard Model Observation"
type: THOUGHT
en_content: "Are you even aware that the Standard Model DOESN'T reflect what's actually being observed in the Cosmos??"
parent: "topic.PHILOSOPHY"
tags:
- science
- philosophy
- observation
- cosmos
- truth
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.STANDARD MODEL OBSERVATION",
    alias: "Thought: Standard Model Observation",
    parent: "topic.PHILOSOPHY",
    tags: ['science', 'philosophy', 'observation', 'cosmos', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.STANDARD MODEL OBSERVATION",
    en_title: "Standard Model Observation",
    en_content: "Are you even aware that the Standard Model DOESN'T reflect what's actually being observed in the Cosmos??",
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
WHERE t.name = "thought.STANDARD MODEL OBSERVATION" AND c.name = "content.STANDARD MODEL OBSERVATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.STANDARD MODEL OBSERVATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.STANDARD MODEL OBSERVATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >STANDARD MODEL OBSERVATION" }]->(child);
```
