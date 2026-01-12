---
name: "thought.CHRISTIANS ON CROSSES"
alias: "Thought: Christians On Crosses"
type: THOUGHT
en_content: "True Christians are easy to identify: they're the ones hanging on crosses."
parent: "topic.RELIGION"
tags:
- christians
- cross
- identity
- religion
- sacrifice
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.CHRISTIANS ON CROSSES",
    alias: "Thought: Christians On Crosses",
    parent: "topic.RELIGION",
    tags: ['christians', 'cross', 'identity', 'religion', 'sacrifice'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHRISTIANS ON CROSSES",
    en_title: "Christians On Crosses",
    en_content: "True Christians are easy to identify: they're the ones hanging on crosses.",
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
WHERE t.name = "thought.CHRISTIANS ON CROSSES" AND c.name = "content.CHRISTIANS ON CROSSES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTIANS ON CROSSES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHRISTIANS ON CROSSES"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHRISTIANS ON CROSSES" }]->(child);
```
