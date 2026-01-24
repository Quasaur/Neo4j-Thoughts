---
name: "thought.SIMPLE RELATIONSHIP CHRIST"
alias: "Thought: Simple Relationship Christ"
type: THOUGHT
en_content: "A relationship with Christ is simple...I make it complicated."
parent: "topic.SPIRITUALITY"
tags:
- relationship
- christ
- simplicity
- spirituality
- struggle
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.SIMPLE RELATIONSHIP CHRIST",
    alias: "Thought: Simple Relationship Christ",
    parent: "topic.SPIRITUALITY",
    tags: ['relationship', 'christ', 'simplicity', 'spirituality', 'struggle'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SIMPLE RELATIONSHIP CHRIST",
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

MATCH (t:THOUGHT {name: "thought.SIMPLE RELATIONSHIP CHRIST"})
MATCH (c:CONTENT {name: "content.SIMPLE RELATIONSHIP CHRIST"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIMPLE RELATIONSHIP CHRIST" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.SIMPLE RELATIONSHIP CHRIST"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->SIMPLE RELATIONSHIP CHRIST" }]->(child);
```
