---
type: THOUGHT
name: "thought.COST OF HEAVEN"
alias: "Thought: Cost Of Heaven"
parent: "topic.GRACE"
en_content: "Heaven is free--but it ain't cheap!"
tags: ["heaven", "grace", "sacrifice", "cost", "salvation"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.COST OF HEAVEN",
    alias: "Thought: Cost Of Heaven",
    parent: "topic.GRACE",
    tags: ['heaven', 'grace', 'sacrifice', 'cost', 'salvation'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.COST OF HEAVEN",
    ctype: "THOUGHT",
    en_title: "Cost Of Heaven",
    en_content: "Heaven is free--but it ain't cheap!",
    es_title: "Costo del Cielo",
    es_content: "¡El cielo es gratis--pero no es barato!",
    fr_title: "Coût du Paradis",
    fr_content: "Le paradis est gratuit--mais ce n'est pas bon marché !",
    hi_title: "स्वर्ग की कीमत",
    hi_content: "स्वर्ग मुफ्त है--लेकिन यह सस्ता नहीं है!",
    zh_title: "Tiān Táng de Dàijià",
    zh_content: "Tiān táng shì miǎnfèi de--dàn tā bù piányi!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COST OF HEAVEN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->COST OF HEAVEN"
RETURN t, parent;
```
