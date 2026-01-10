---
name: "thought.CHRISTIANITY STEPS"
alias: "Thought: Christianity Steps"
type: THOUGHT
en_content: "Christianity: READ, HEAR, BELIEVE, CONFESS, OBEY, ASK, RECEIVE."
parent: "topic.RELIGION"
tags:
- faith
- steps
- christianity
- obedience
- belief
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.CHRISTIANITY STEPS",
    alias: "Thought: Christianity Steps",
    parent: "topic.RELIGION",
    tags: ['faith', 'steps', 'christianity', 'obedience', 'belief'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRISTIANITY STEPS",
    en_title: "Christianity Steps",
    en_content: "Christianity: READ, HEAR, BELIEVE, CONFESS, OBEY, ASK, RECEIVE.",
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
WHERE t.name = "thought.CHRISTIANITY STEPS" AND c.name = "content.CHRISTIANITY STEPS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTIANITY STEPS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHRISTIANITY STEPS"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHRISTIANITY STEPS" }]->(child);
```
