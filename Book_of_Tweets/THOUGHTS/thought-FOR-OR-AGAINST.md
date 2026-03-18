---
type: THOUGHT
name: "thought.FOR OR AGAINST"
alias: "Thought: For Or Against"
parent: "topic.THE GODHEAD"
en_content: "\"Whoever is not for Me is against Me.\" -- Jesus Christ"
tags: ["jesus", "choice", "allegiance", "christ", "judgment"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Oct-2011)
CREATE (t:THOUGHT {    name: "thought.FOR OR AGAINST",
    alias: "Thought: For Or Against",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'choice', 'allegiance', 'christ', 'judgment'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.FOR OR AGAINST",
    ctype: "THOUGHT",
    en_title: "For Or Against",
    en_content: "\"Whoever is not for Me is against Me.\" -- Jesus Christ",
    es_title: "A favor o en contra",
    es_content: "\",
    fr_title: "Pour ou contre",
    fr_content: "\",
    hi_title: "पक्ष या विपक्ष में",
    hi_content: "\",
    zh_title: "zhī chí huò fǎn duì",
    zh_content: "\"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FOR OR AGAINST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->FOR OR AGAINST"
RETURN t, parent;
```
