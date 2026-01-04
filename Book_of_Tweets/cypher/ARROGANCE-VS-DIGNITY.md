---
name: "thought.ARROGANCE VS DIGNITY"
alias: "Thought: Arrogance Vs Dignity"
type: THOUGHT
en_content: "Far too many black men have mistaken arrogance for dignity."
parent: "topic.HUMANITY"
tags:
- dignity
- arrogance
- humanity
- character
- race
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.ARROGANCE VS DIGNITY",
    alias: "Thought: Arrogance Vs Dignity",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'arrogance', 'humanity', 'character', 'race'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ARROGANCE VS DIGNITY",
    en_title: "Arrogance Vs Dignity",
    en_content: "Far too many black men have mistaken arrogance for dignity.",
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
WHERE t.name = "thought.ARROGANCE VS DIGNITY" AND c.name = "content.ARROGANCE VS DIGNITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ARROGANCE VS DIGNITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.ARROGANCE VS DIGNITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >ARROGANCE VS DIGNITY" }]->(child);
```
