---
type: THOUGHT
name: "thought.BEHIND"
alias: "Thought: Behind"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["divine", "sovereignty", "impetus", "control", "all"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BEHIND",
    alias: "Thought: Behind",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["divine", "sovereignty", "impetus", "control", "all"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BEHIND",
    ctype: "THOUGHT",
    en_title: "Behind",
    en_content: "",
    es_title: "DETRÁS",
    es_content: "Dios está detrás de todo",
    fr_title: "DERRIÈRE",
    fr_content: "Dieu est derrière tout",
    hi_title: "पीछे",
    hi_content: "हर चीज़ के पीछे भगवान है",
    zh_title: "zài hòu miàn",
    zh_content: "shén shì yī qiè de bèi hòu"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BEHIND"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->BEHIND"
RETURN t, parent;
```
