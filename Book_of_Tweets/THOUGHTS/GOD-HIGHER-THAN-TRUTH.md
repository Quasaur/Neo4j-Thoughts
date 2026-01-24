---
name: "thought.GOD HIGHER THAN TRUTH"
alias: "Thought: God Higher Than Truth"
type: THOUGHT
en_content: "\"There is no god higher than Truth.\" - Gandhi. \"There is no truth higher than God.\" - Mitchell"
parent: "topic.THE GODHEAD"
tags:
- truth
- god
- gandhi
- mitchell
- philosophy
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD HIGHER THAN TRUTH",
    alias: "Thought: God Higher Than Truth",
    parent: "topic.THE GODHEAD",
    tags: ['truth', 'god', 'gandhi', 'mitchell', 'philosophy'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD HIGHER THAN TRUTH",
    en_title: "God Higher Than Truth",
    en_content: "\"There is no god higher than Truth.\" - Gandhi. \"There is no truth higher than God.\" - Mitchell",
    es_title: "Dios más alto que la verdad",
    es_content: "\",
    fr_title: "Dieu plus haut que la vérité",
    fr_content: "\",
    hi_title: "ईश्वर सत्य से भी ऊंचा है",
    hi_content: "\",
    zh_title: "神高于真理",
    zh_content: "\"
});

MATCH (t:THOUGHT {name: "thought.GOD HIGHER THAN TRUTH"})
MATCH (c:CONTENT {name: "content.GOD HIGHER THAN TRUTH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD HIGHER THAN TRUTH" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD HIGHER THAN TRUTH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD HIGHER THAN TRUTH" }]->(child);
```
