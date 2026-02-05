---
name: "thought.JESUS TAKES OVER"
alias: "Thought: Jesus Takes Over"
type: THOUGHT
en_content: "\"I come: not to take sides, but to take over.\" - Jesus Christ"
parent: "topic.THE GODHEAD"
tags:
- jesus
- power
- sovereignty
- kingdom
- takeover
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.JESUS TAKES OVER",
    alias: "Thought: Jesus Takes Over",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'power', 'sovereignty', 'kingdom', 'takeover'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.JESUS TAKES OVER",
    en_title: "Jesus Takes Over",
    en_content: "\"I come: not to take sides, but to take over.\" - Jesus Christ",
    es_title: "Jesús toma el control",
    es_content: "\",
    fr_title: "Jésus prend le relais",
    fr_content: "\",
    hi_title: "यीशु ने कब्ज़ा कर लिया",
    hi_content: "\",
    zh_title: "yē sū jiē guǎn",
    zh_content: "\"
});

MATCH (t:THOUGHT {name: "thought.JESUS TAKES OVER"})
MATCH (c:CONTENT {name: "content.JESUS TAKES OVER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS TAKES OVER" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.JESUS TAKES OVER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->JESUS TAKES OVER" }]->(child);
```
