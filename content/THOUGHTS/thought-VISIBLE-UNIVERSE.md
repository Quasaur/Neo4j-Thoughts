---
type: THOUGHT
name: "thought.VISIBLE UNIVERSE"
alias: "Thought: Visible Universe"
parent: "topic.COSMOLOGY"
en_content: "The Visible Universe: God Is Great"
tags: ["universe", "creation", "power", "majesty", "sight"]
ptopic: "[[topic-COSMOLOGY]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VISIBLE UNIVERSE",
    alias: "Thought: Visible Universe",
    parent: "topic.COSMOLOGY",
    tags: ['universe', 'creation', 'power', 'majesty', 'sight'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.VISIBLE UNIVERSE",
    ctype: "THOUGHT",
    en_title: "Visible Universe",
    en_content: "The Visible Universe: God Is Great",
    es_title: "Universo Visible",
    es_content: "El Universo Visible: Dios Es Grande",
    fr_title: "Univers Visible",
    fr_content: "L'Univers Visible : Dieu Est Grand",
    hi_title: "दृश्य ब्रह्मांड",
    hi_content: "दृश्य ब्रह्मांड: परमेश्वर महान है",
    zh_title: "Kě Jiàn Yǔ Zhòu",
    zh_content: "Kě Jiàn Yǔ Zhòu: Shàng Dì Shì Wěi Dà De"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VISIBLE UNIVERSE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.COSMOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.COSMOLOGY->VISIBLE UNIVERSE"
RETURN t, parent;
```
