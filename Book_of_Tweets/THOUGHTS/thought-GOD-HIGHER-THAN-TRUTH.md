---
type: THOUGHT
name: "thought.GOD HIGHER THAN TRUTH"
alias: "Thought: God Higher Than Truth"
parent: "topic.THE GODHEAD"
en_content: "\"There is no god higher than Truth.\" - Gandhi. \"There is no truth higher than God.\" - Mitchell"
tags: ["truth", "god", "gandhi", "mitchell", "philosophy"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2013)
CREATE (t:THOUGHT {    name: "thought.GOD HIGHER THAN TRUTH",
    alias: "Thought: God Higher Than Truth",
    parent: "topic.THE GODHEAD",
    tags: ['truth', 'god', 'gandhi', 'mitchell', 'philosophy'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD HIGHER THAN TRUTH",
    ctype: "THOUGHT",
    en_title: "God Higher Than Truth",
    en_content: "\"There is no god higher than Truth.\" - Gandhi. \"There is no truth higher than God.\" - Mitchell",
    es_title: "Dios más alto que la verdad",
    es_content: "\",
    fr_title: "Dieu plus haut que la vérité",
    fr_content: "\",
    hi_title: "ईश्वर सत्य से भी ऊंचा है",
    hi_content: "\",
    zh_title: "shén gāo yú zhēn lǐ",
    zh_content: "\"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD HIGHER THAN TRUTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD HIGHER THAN TRUTH"
RETURN t, parent;
```
