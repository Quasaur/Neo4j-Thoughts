---
type: THOUGHT
name: "thought.ACCOUNTABILITY"
alias: "Thought: Accountability"
parent: "topic.HUMANITY"
en_content: "The idea of God introduces the concept of accountability."
tags: ["god", "lord", "judgment", "accountable", "responsible"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ACCOUNTABILITY",
    alias: "Thought: Accountability",
    parent: "topic.HUMANITY",
    tags: ["god", "lord", "judgment", "accountable", "responsible"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    ctype: "THOUGHT",
    en_title: "Accountability",
    en_content: "The idea of God introduces the concept of accountability.",
    es_title: "Responsabilidad",
    es_content: "Dios no te libra de las consecuencias de mis acciones.",
    fr_title: "Responsabilité",
    fr_content: "Dieu ne t'épargne pas les conséquences de mes actions.",
    hi_title: "जवाबदेही",
    hi_content: "भगवान आपको मेरे कार्यों के परिणामों से नहीं बचाते।",
    zh_title: "问责制",
    zh_content: "上帝不会让你免受我行为的后果。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ACCOUNTABILITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->ACCOUNTABILITY"
RETURN t, parent;
```
