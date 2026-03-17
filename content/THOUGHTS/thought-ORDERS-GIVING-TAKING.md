---
type: THOUGHT
name: "thought.ORDERS GIVING TAKING"
alias: "Thought: Orders Giving Taking"
parent: "topic.WISDOM"
en_content: "I'm highly suspicious of people who can give orders but not take orders."
tags: ["authority", "humility", "attitude", "character", "orders"]
ptopic: "[[topic-WISDOM]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ORDERS GIVING TAKING",
    alias: "Thought: Orders Giving Taking",
    parent: "topic.WISDOM",
    tags: ['authority', 'humility', 'attitude', 'character', 'orders'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ORDERS GIVING TAKING",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ORDERS GIVING TAKING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ORDERS GIVING TAKING"
RETURN t, parent;
```
