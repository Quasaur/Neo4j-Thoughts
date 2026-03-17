---
type: THOUGHT
name: "thought.ENDING"
alias: "Thought: Ending"
parent: "topic.APOCALYPSE"
en_content: "","
 es_title: "FINAL"
 es_content: ""
 fr_title: "FIN"
 fr_content: ""
 hi_title: "ख़त्म होना"
 hi_content: ""
 zh_title: "jié shù"
 zh_content: ""
tags: ["ending", "bible", "apocalypse", "judgment", "newjerusalem"]
ptopic: "[[topic-APOCALYPSE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ENDING",
    alias: "Thought: Ending",
    parent: "topic.APOCALYPSE",
    tags: ["ending", "bible", "apocalypse", "judgment", "newjerusalem"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ENDING",
    ctype: "THOUGHT",
    en_title: "Ending",
    en_content: "",
    es_title: "FINAL",
    es_content: "",
    fr_title: "FIN",
    fr_content: "",
    hi_title: "ख़त्म होना",
    hi_content: "",
    zh_title: "jié shù",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ENDING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.APOCALYPSE->ENDING"
RETURN t, parent;
```
