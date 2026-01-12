---
name: "thought.FOR OR AGAINST"
alias: "Thought: For Or Against"
type: THOUGHT
en_content: "\"Whoever is not for Me is against Me.\" -- Jesus Christ"
parent: "topic.THE GODHEAD"
tags:
- jesus
- choice
- allegiance
- christ
- judgment
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.FOR OR AGAINST",
    alias: "Thought: For Or Against",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'choice', 'allegiance', 'christ', 'judgment'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.FOR OR AGAINST",
    en_title: "For Or Against",
    en_content: "\"Whoever is not for Me is against Me.\" -- Jesus Christ",
    es_title: "A favor o en contra",
    es_content: "\",
    fr_title: "Pour ou contre",
    fr_content: "\",
    hi_title: "पक्ष या विपक्ष में",
    hi_content: "\",
    zh_title: "支持或反对",
    zh_content: "\"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FOR OR AGAINST" AND c.name = "content.FOR OR AGAINST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FOR OR AGAINST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.FOR OR AGAINST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >FOR OR AGAINST" }]->(child);
```
