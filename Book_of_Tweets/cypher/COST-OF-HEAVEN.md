---
name: "thought.COST OF HEAVEN"
alias: "Thought: Cost Of Heaven"
type: THOUGHT
en_content: "Heaven is free--but it ain't cheap!"
parent: "topic.GRACE"
tags:
- heaven
- grace
- sacrifice
- cost
- salvation
level: 3
neo4j: true
insert: true
---
# Cost Of Heaven

> [!Thought-en]
> Heaven is free--but it ain't cheap!

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.COST OF HEAVEN",
    alias: "Thought: Cost Of Heaven",
    parent: "topic.GRACE",
    tags: ['heaven', 'grace', 'sacrifice', 'cost', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.COST OF HEAVEN",
    en_title: "Cost Of Heaven",
    en_content: "Heaven is free--but it ain't cheap!",
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
WHERE t.name = "thought.COST OF HEAVEN" AND c.name = "content.COST OF HEAVEN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COST OF HEAVEN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.COST OF HEAVEN"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >COST OF HEAVEN" }]->(child);
```