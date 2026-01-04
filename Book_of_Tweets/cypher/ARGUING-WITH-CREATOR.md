---
name: "thought.ARGUING WITH CREATOR"
alias: "Thought: Arguing With Creator"
type: THOUGHT
en_content: "Humanity's constant pastime is to argue with its Creator."
parent: "topic.HUMANITY"
tags:
- humanity
- rebellion
- creation
- argument
- pride
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.ARGUING WITH CREATOR",
    alias: "Thought: Arguing With Creator",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'rebellion', 'creation', 'argument', 'pride'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ARGUING WITH CREATOR",
    en_title: "Arguing With Creator",
    en_content: "Humanity's constant pastime is to argue with its Creator.",
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
WHERE t.name = "thought.ARGUING WITH CREATOR" AND c.name = "content.ARGUING WITH CREATOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ARGUING WITH CREATOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.ARGUING WITH CREATOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >ARGUING WITH CREATOR" }]->(child);
```
