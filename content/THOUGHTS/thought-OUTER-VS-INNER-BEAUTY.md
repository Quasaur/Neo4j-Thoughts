---
type: THOUGHT
name: "thought.OUTER VS INNER BEAUTY"
alias: "Thought: Outer vs Inner Beauty"
parent: "topic.ATTITUDE"
en_content: "Outer beauty doesn't make up for inner ugly."
tags: ["beauty", "character", "appearance", "aesthetics", "holiness"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.OUTER VS INNER BEAUTY",
    alias: "Thought: Outer vs Inner Beauty",
    parent: "topic.ATTITUDE",
    tags: ["beauty", "character", "appearance", "aesthetics", "holiness"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OUTER VS INNER BEAUTY",
    ctype: "THOUGHT",
    en_title: "Thought: Outer vs Inner Beauty",
    en_content: "Outer beauty doesn't make up for inner ugly.",
    es_title: "Pensamiento: belleza exterior versus belleza interior",
    es_content: "La belleza exterior no compensa la fealdad interior.",
    fr_title: "Pensée : beauté extérieure ou beauté intérieure",
    fr_content: "La beauté extérieure ne compense pas la laideur intérieure.",
    hi_title: "विचार: बाहरी बनाम आंतरिक सुंदरता",
    hi_content: "बाहरी सुंदरता भीतरी कुरूपता की भरपाई नहीं करती।",
    zh_title: "sī kǎo : wài zài měi yǔ nèi zài měi",
    zh_content: "Wai zai de mei li bu neng mi bu nei zai de chou lou."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OUTER VS INNER BEAUTY";
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->OUTER VS INNER BEAUTY"
RETURN t, parent;
```
