---
name: "thought.NATURE OF REALITY"
alias: "Thought: Nature Of Reality"
type: THOUGHT
en_content: "Reality: perhaps matter is only real to other matter...?"
parent: "topic.PHILOSOPHY"
tags:
- reality
- matter
- philosophy
- ontology
- perception
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2010b)
CREATE (t:THOUGHT {
    name: "thought.NATURE OF REALITY",
    alias: "Thought: Nature Of Reality",
    parent: "topic.PHILOSOPHY",
    tags: ['reality', 'matter', 'philosophy', 'ontology', 'perception'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NATURE OF REALITY",
    en_title: "Nature Of Reality",
    en_content: "Reality: perhaps matter is only real to other matter...?",
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
WHERE t.name = "thought.NATURE OF REALITY" AND c.name = "content.NATURE OF REALITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATURE OF REALITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.NATURE OF REALITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >NATURE OF REALITY" }]->(child);
```
