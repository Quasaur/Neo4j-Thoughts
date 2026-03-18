---
type: THOUGHT
name: "thought.INCONVENIENT WILL"
alias: "Thought: Inconvenient Will"
parent: "topic.SPIRITUALITY"
en_content: "Accomplishing God's Will is rarely convenient."
tags: ["will", "obedience", "spirituality", "sacrifice", "convenience"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Oct-2011)
CREATE (t:THOUGHT {    name: "thought.INCONVENIENT WILL",
    alias: "Thought: Inconvenient Will",
    parent: "topic.SPIRITUALITY",
    tags: ['will', 'obedience', 'spirituality', 'sacrifice', 'convenience'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.INCONVENIENT WILL",
    ctype: "THOUGHT",
    en_title: "Inconvenient Will",
    en_content: "Accomplishing God's Will is rarely convenient.",
    es_title: "Voluntad Inconveniente",
    es_content: "Cumplir la Voluntad de Dios rara vez es conveniente.",
    fr_title: "Volonté Incommode",
    fr_content: "Accomplir la Volonté de Dieu est rarement pratique.",
    hi_title: "असुविधाजनक इच्छा",
    hi_content: "परमेश्वर की इच्छा को पूरा करना शायद ही कभी सुविधाजनक होता है।",
    zh_title: "Bù Biàn de Yìzhì",
    zh_content: "Chéngjiù Shàngdì de Yìzhì hěn shǎo shì fāngbiàn de."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INCONVENIENT WILL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->INCONVENIENT WILL"
RETURN t, parent;
```
