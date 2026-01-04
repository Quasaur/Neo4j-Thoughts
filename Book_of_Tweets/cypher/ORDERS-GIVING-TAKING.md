---
name: "thought.ORDERS GIVING TAKING"
alias: "Thought: Orders Giving Taking"
type: THOUGHT
en_content: "I'm highly suspicious of people who can give orders but not take orders."
parent: "topic.ATTITUDE"
tags:
- authority
- humility
- attitude
- character
- orders
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.ORDERS GIVING TAKING",
    alias: "Thought: Orders Giving Taking",
    parent: "topic.ATTITUDE",
    tags: ['authority', 'humility', 'attitude', 'character', 'orders'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ORDERS GIVING TAKING",
    en_title: "Orders Giving Taking",
    en_content: "I'm highly suspicious of people who can give orders but not take orders.",
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
WHERE t.name = "thought.ORDERS GIVING TAKING" AND c.name = "content.ORDERS GIVING TAKING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ORDERS GIVING TAKING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ORDERS GIVING TAKING"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ORDERS GIVING TAKING" }]->(child);
```
