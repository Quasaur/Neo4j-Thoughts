---
type: THOUGHT
name: "thought.DEFINE HOPE"
alias: "Thought: Hope Defined"
parent: "topic.ATTITUDE"
en_content: "Hope equals Desire plus Expectation."
tags: ["hope", "desire", "expectation", "attitude", "philosophy"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE HOPE",
    alias: "Thought: Hope Defined",
    parent: "topic.ATTITUDE",
    tags: ['hope', 'desire', 'expectation', 'attitude', 'philosophy'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE HOPE",
    ctype: "THOUGHT",
    en_title: "Thought: Hope Defined",
    en_content: "Hope equals Desire plus Expectation.",
    es_title: "Pensamiento: Esperanza definida",
    es_content: "La esperanza es igual al Deseo más la Expectativa.",
    fr_title: "Pensée : Définir l'Espoir",
    fr_content: "L'espoir est égal au désir et à l'attente.",
    hi_title: "विचार: आशा परिभाषित",
    hi_content: "आशा, इच्छा और अपेक्षा के बराबर है।",
    zh_title: "sī xiǎng : xī wàng de dìng yì",
    zh_content: "xī wàng děng yú yù wàng jiā qī wàng .
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
