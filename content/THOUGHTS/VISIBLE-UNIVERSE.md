---
name: "thought.VISIBLE UNIVERSE"
alias: "Thought: Visible Universe"
type: THOUGHT
en_content: "The Visible Universe: God Is Great"
parent: "topic.COSMOLOGY"
tags:
- universe
- creation
- power
- majesty
- sight
level: 3
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.VISIBLE UNIVERSE",
    alias: "Thought: Visible Universe",
    parent: "topic.COSMOLOGY",
    tags: ['universe', 'creation', 'power', 'majesty', 'sight'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VISIBLE UNIVERSE",
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

MATCH (t:THOUGHT {name: "thought.VISIBLE UNIVERSE"})
MATCH (c:CONTENT {name: "content.VISIBLE UNIVERSE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.VISIBLE UNIVERSE" }]->(c);

MATCH (parent:TOPIC {name: "topic.COSMOLOGY"})
MATCH (child:THOUGHT {name: "thought.VISIBLE UNIVERSE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "COSMOLOGY->VISIBLE UNIVERSE" }]->(child);
```
