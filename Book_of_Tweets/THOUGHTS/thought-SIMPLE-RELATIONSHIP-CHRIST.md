---
type: THOUGHT
name: "thought.SIMPLE RELATIONSHIP CHRIST"
alias: "Thought: Simple Relationship Christ"
parent: "topic.SPIRITUALITY"
en_content: "A relationship with Christ is simple...I make it complicated."
tags: ["relationship", "christ", "simplicity", "spirituality", "struggle"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Dec-2011)
CREATE (t:THOUGHT {    name: "thought.SIMPLE RELATIONSHIP CHRIST",
    alias: "Thought: Simple Relationship Christ",
    parent: "topic.SPIRITUALITY",
    tags: ['relationship', 'christ', 'simplicity', 'spirituality', 'struggle'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.SIMPLE RELATIONSHIP CHRIST",
    ctype: "THOUGHT",
    en_title: "Simple Relationship Christ",
    en_content: "A relationship with Christ is simple...I make it complicated.",
    es_title: "Relación Simple con Cristo",
    es_content: "Una relación con Cristo es simple...yo la complico.",
    fr_title: "Relation Simple avec le Christ",
    fr_content: "Une relation avec le Christ est simple...je la complique.",
    hi_title: "मसीह के साथ सरल रिश्ता",
    hi_content: "मसीह के साथ रिश्ता सरल है...मैं इसे जटिल बनाता हूँ।",
    zh_title: "Yu Jidu de Jiandan Guanxi",
    zh_content: "Yu Jidu de guanxi shi jiandan de...wo ba ta nong fule le."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SIMPLE RELATIONSHIP CHRIST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->SIMPLE RELATIONSHIP CHRIST"
RETURN t, parent;
```
