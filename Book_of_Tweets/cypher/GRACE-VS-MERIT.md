---
name: "thought.GRACE VS MERIT"
alias: "Thought: Grace Vs Merit"
type: THOUGHT
en_content: "The merit system and Grace are incompatible...we have to choose one or the other."
parent: "topic.GRACE"
tags:
- grace
- merit
- salvation
- choice
- gospel
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Aug-2010b)
CREATE (t:THOUGHT {
    name: "thought.GRACE VS MERIT",
    alias: "Thought: Grace Vs Merit",
    parent: "topic.GRACE",
    tags: ['grace', 'merit', 'salvation', 'choice', 'gospel'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE VS MERIT",
    en_title: "Grace Vs Merit",
    en_content: "The merit system and Grace are incompatible...we have to choose one or the other.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GRACE VS MERIT" AND c.name = "content.GRACE VS MERIT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GRACE VS MERIT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GRACE VS MERIT"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GRACE VS MERIT" }]->(child);
```
