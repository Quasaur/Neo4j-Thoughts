---
type: THOUGHT
name: "thought.DEFINE HOPE"
alias: "Thought: Define Hope"
parent: "topic.ATTITUDE"
en_content: "HOPE = DESIRE + EXPECTATION"
tags: ["hope", "desire", "expectation", "attitude", "philosophy"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE HOPE",
    alias: "Thought: Define Hope",
    parent: "topic.ATTITUDE",
    tags: ['hope', 'desire', 'expectation', 'attitude', 'philosophy'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE HOPE",
    ctype: "THOUGHT",
    en_title: "Define Hope",
    en_content: "HOPE = DESIRE + EXPECTATION",
    es_title: "Definir Esperanza",
    es_content: "ESPERANZA = DESEO + EXPECTATIVA",
    fr_title: "Définir l'Espoir",
    fr_content: "ESPOIR = DÉSIR + ATTENTE",
    hi_title: "आशा को परिभाषित करें",
    hi_content: "आशा = इच्छा + अपेक्षा",
    zh_title: "Dìngyì xīwàng",
    zh_content: "Xīwàng = Kěwàng + Qīwàng"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE HOPE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->DEFINE HOPE"
RETURN t, parent;
```
