---
type: THOUGHT
name: "thought.NOT POLITICALLY CORRECT"
alias: "Thought: Not Politically Correct"
parent: "topic.THE GODHEAD"
en_content: "God is not politically correct."
tags: ["truth", "politics", "character", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2011b)
CREATE (t:THOUGHT {    name: "thought.NOT POLITICALLY CORRECT",
    alias: "Thought: Not Politically Correct",
    parent: "topic.THE GODHEAD",
    tags: ['truth', 'politics', 'character', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.NOT POLITICALLY CORRECT",
    ctype: "THOUGHT",
    en_title: "Not Politically Correct",
    en_content: "God is not politically correct.",
    es_title: "No Políticamente Correcto",
    es_content: "Dios no es políticamente correcto.",
    fr_title: "Pas Politiquement Correct",
    fr_content: "Dieu n'est pas politiquement correct.",
    hi_title: "राजनीतिक रूप से सही नहीं",
    hi_content: "परमेश्वर राजनीतिक रूप से सही नहीं है।",
    zh_title: "Bu Zhengzhi Zhengque",
    zh_content: "Shangdi bu zhengzhi zhengque."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOT POLITICALLY CORRECT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->NOT POLITICALLY CORRECT"
RETURN t, parent;
```
