---
type: THOUGHT
name: "thought.JESUS TAKES OVER"
alias: "Thought: Jesus Takes Over"
parent: "topic.THE GODHEAD"
en_content: "\"I come: not to take sides, but to take over.\" - Jesus Christ"
tags: ["jesus", "power", "sovereignty", "kingdom", "takeover"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Sep-2012)
CREATE (t:THOUGHT {    name: "thought.JESUS TAKES OVER",
    alias: "Thought: Jesus Takes Over",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'power', 'sovereignty', 'kingdom', 'takeover'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.JESUS TAKES OVER",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.JESUS TAKES OVER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->JESUS TAKES OVER"
RETURN t, parent;
```
