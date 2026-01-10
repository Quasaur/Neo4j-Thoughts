---
name: "thought.PRAYER AND CHOCOLATE"
alias: "Thought: Prayer And Chocolate"
type: THOUGHT
en_content: "Is there a better way to start a day than with prayer and chocolate? I think not!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- chocolate
- joy
- spirituality
- humor
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.PRAYER AND CHOCOLATE",
    alias: "Thought: Prayer And Chocolate",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'chocolate', 'joy', 'spirituality', 'humor'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER AND CHOCOLATE",
    en_title: "Prayer And Chocolate",
    en_content: "Is there a better way to start a day than with prayer and chocolate? I think not!",
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
WHERE t.name = "thought.PRAYER AND CHOCOLATE" AND c.name = "content.PRAYER AND CHOCOLATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER AND CHOCOLATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER AND CHOCOLATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER AND CHOCOLATE" }]->(child);
```
