---
name: "thought.ORDERS GIVING TAKING"
alias: "Thought: Orders Giving Taking"
type: THOUGHT
en_content: I'm highly suspicious of people who can give orders but not take orders.
parent: topic.WISDOM
tags:
  - authority
  - humility
  - attitude
  - character
  - orders
level: 3
neo4j: true
ptopic: "[[topic-WISDOM]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.ORDERS GIVING TAKING",
    alias: "Thought: Orders Giving Taking",
    parent: "topic.ATTITUDE",
    tags: ['authority', 'humility', 'attitude', 'character', 'orders'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ORDERS GIVING TAKING",
    en_title: "Orders Giving Taking",
    en_content: "I'm highly suspicious of people who can give orders but not take orders.",
    es_title: "Dar y Recibir Órdenes",
    es_content: "Desconfío mucho de las personas que pueden dar órdenes pero no pueden recibirlas.",
    fr_title: "Donner et Recevoir des Ordres",
    fr_content: "Je me méfie beaucoup des gens qui peuvent donner des ordres mais ne peuvent pas en recevoir.",
    hi_title: "आदेश देना और लेना",
    hi_content: "मुझे उन लोगों पर बहुत संदेह है जो आदेश दे सकते हैं लेकिन आदेश नहीं ले सकते।",
    zh_title: "Ming Ling De Gei Yu He Jie Shou",
    zh_content: "Wo dui nei xie neng gou xia ming ling que bu neng jie shou ming ling de ren hen you huai yi."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ORDERS GIVING TAKING" AND c.name = "content.ORDERS GIVING TAKING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ORDERS GIVING TAKING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ORDERS GIVING TAKING"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->ORDERS GIVING TAKING" }]->(child);
```
