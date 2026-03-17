---
type: THOUGHT
name: "thought.THINK"
alias: "Thought: Think"
parent: "topic.PSYCHOLOGY"
tags: ["think", "howto", "cognition", "critical", "logic"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.THINK",
    alias: "Thought: Think",
    parent: "topic.PSYCHOLOGY",
    tags: ["think", "howto", "cognition", "critical", "logic"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THINK",
    ctype: "THOUGHT",
    en_title: "Think",
    en_content: "",
    es_title: "PENSAR",
    es_content: "¿Crees que sabes pensar?",
    fr_title: "PENSE",
    fr_content: "Pensez-vous que vous savez penser ?",
    hi_title: "सोचना",
    hi_content: "क्या आपको लगता है कि आप सोचना जानते हैं?",
    zh_title: "sī kǎo",
    zh_content: "nǐ rèn wéi nǐ zhī dào rú hé sī kǎo ma ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THINK"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->THINK"
RETURN t, parent;
```
