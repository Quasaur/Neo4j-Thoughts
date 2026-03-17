---
type: THOUGHT
name: "thought.UNREASONABLE PRIDE"
alias: "Thought: Unreasonable Pride"
parent: "topic.EVIL"
en_content: "Self Pride is always unreasonable."
tags: ["pride", "attitude", "reason", "character", "arrogance"]
ptopic: "[[topic-EVIL]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNREASONABLE PRIDE",
    alias: "Thought: Unreasonable Pride",
    parent: "topic.EVIL",
    tags: ['pride', 'attitude', 'reason', 'character', 'arrogance'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNREASONABLE PRIDE",
    ctype: "THOUGHT",
    en_title: "Unreasonable Pride",
    en_content: "Self Pride is always unreasonable.",
    es_title: "Orgullo Irrazonable",
    es_content: "El orgullo propio siempre es irrazonable.",
    fr_title: "Orgueil Déraisonnable",
    fr_content: "L'orgueil de soi est toujours déraisonnable.",
    hi_title: "अनुचित गर्व",
    hi_content: "स्वयं का गर्व हमेशा अनुचित होता है।",
    zh_title: "Bu He Li De Jiao Ao",
    zh_content: "Zi Wo Jiao Ao Zong Shi Bu He Li De."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNREASONABLE PRIDE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->UNREASONABLE PRIDE"
RETURN t, parent;
```
