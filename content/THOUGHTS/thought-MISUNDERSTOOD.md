---
type: THOUGHT
name: "thought.MISUNDERSTOOD"
alias: "Thought: Misunderstood"
parent: "topic.UNDERSTANDING"
tags: ["misunderfstood", "understanding", "communication", "fellowship", "intimacy"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MISUNDERSTOOD",
    alias: "Thought: Misunderstood",
    parent: "topic.UNDERSTANDING",
    tags: ["misunderfstood", "understanding", "communication", "fellowship", "intimacy"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MISUNDERSTOOD",
    ctype: "THOUGHT",
    en_title: "Misunderstood",
    en_content: "",
    es_title: "INCOMPRENDIDO",
    es_content: "Una de las mayores agonías de la vida es la de ser incomprendido.",
    fr_title: "MAL COMPRIS",
    fr_content: "L'une des plus grandes souffrances de la vie est celle d'être mal comprise.",
    hi_title: "गलत समझा",
    hi_content: "जीवन की सबसे बड़ी पीड़ाओं में से एक है गलत समझा जाना।",
    zh_title: "bèi wù jiě",
    zh_content: "rén shēng zuì dà de tòng kǔ zhī yī jiù shì bèi wù jiě 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MISUNDERSTOOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.UNDERSTANDING->MISUNDERSTOOD"
RETURN t, parent;
```
