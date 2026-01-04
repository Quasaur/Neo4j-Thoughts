---
name: "thought.SACRIFICE IN SERVICE"
alias: "Thought: Sacrifice In Service"
type: THOUGHT
en_content: "You cannot serve God without sacrificing something of great personal value."
parent: "topic.WORSHIP"
tags:
- sacrifice
- service
- worship
- devotion
- commitment
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.SACRIFICE IN SERVICE",
    alias: "Thought: Sacrifice In Service",
    parent: "topic.WORSHIP",
    tags: ['sacrifice', 'service', 'worship', 'devotion', 'commitment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SACRIFICE IN SERVICE",
    en_title: "Sacrifice In Service",
    en_content: "You cannot serve God without sacrificing something of great personal value.",
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
WHERE t.name = "thought.SACRIFICE IN SERVICE" AND c.name = "content.SACRIFICE IN SERVICE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SACRIFICE IN SERVICE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.SACRIFICE IN SERVICE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WORSHIP >SACRIFICE IN SERVICE" }]->(child);
```
