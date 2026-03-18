---
type: THOUGHT
name: "thought.PRAYER AS RELIEF"
alias: "Thought: Prayer As Relief"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is my relief."
tags: ["prayer", "relief", "pain", "spirituality", "comfort"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013c)
CREATE (t:THOUGHT {    name: "thought.PRAYER AS RELIEF",
    alias: "Thought: Prayer As Relief",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'relief', 'pain', 'spirituality', 'comfort'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.PRAYER AS RELIEF",
    ctype: "THOUGHT",
    en_title: "Prayer As Relief",
    en_content: "Prayer is my relief.",
    es_title: "La Oración Como Alivio",
    es_content: "La oración es mi alivio.",
    fr_title: "La Prière Comme Soulagement",
    fr_content: "La prière est mon soulagement.",
    hi_title: "राहत के रूप में प्रार्थना",
    hi_content: "प्रार्थना मेरी राहत है।",
    zh_title: "Dǎogào Zuòwéi Ānwèi",
    zh_content: "Dǎogào shì wǒ de ānwèi."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRAYER AS RELIEF"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->PRAYER AS RELIEF"
RETURN t, parent;
```
