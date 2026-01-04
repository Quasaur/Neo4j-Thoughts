---
name: "thought.EVOLUTION AS RELIGION"
alias: "Thought: Evolution As Religion"
type: THOUGHT
en_content: "Evolution is a RELIGION, evidence for which has been dwindling as scientific observation has grown more sophisticated."
parent: "topic.PHILOSOPHY"
tags:
- evolution
- religion
- philosophy
- truth
- science
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010c)
CREATE (t:THOUGHT {
    name: "thought.EVOLUTION AS RELIGION",
    alias: "Thought: Evolution As Religion",
    parent: "topic.PHILOSOPHY",
    tags: ['evolution', 'religion', 'philosophy', 'truth', 'science'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTION AS RELIGION",
    en_title: "Evolution As Religion",
    en_content: "Evolution is a RELIGION, evidence for which has been dwindling as scientific observation has grown more sophisticated.",
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
WHERE t.name = "thought.EVOLUTION AS RELIGION" AND c.name = "content.EVOLUTION AS RELIGION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVOLUTION AS RELIGION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.EVOLUTION AS RELIGION"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >EVOLUTION AS RELIGION" }]->(child);
```
