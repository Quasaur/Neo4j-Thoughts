---
type: THOUGHT
name: "thought.PREEMINENCE OF GOODNESS"
alias: "Thought: Preeminence Of Goodness"
parent: "topic.THE GODHEAD"
en_content: "That which comes first has the preeminence; righteousness came before sin and goodness came before evil."
tags: ["goodness", "righteousness", "eternity", "character", "preeminence"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Nov-2011)
CREATE (t:THOUGHT {    name: "thought.PREEMINENCE OF GOODNESS",
    alias: "Thought: Preeminence Of Goodness",
    parent: "topic.THE GODHEAD",
    tags: ['goodness', 'righteousness', 'eternity', 'character', 'preeminence'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.PREEMINENCE OF GOODNESS",
    ctype: "THOUGHT",
    en_title: "Preeminence Of Goodness",
    en_content: "That which comes first has the preeminence; righteousness came before sin and goodness came before evil.",
    es_title: "Preeminencia de la Bondad",
    es_content: "Lo que viene primero tiene la preeminencia; la justicia vino antes que el pecado y la bondad vino antes que el mal.",
    fr_title: "Prééminence de la Bonté",
    fr_content: "Ce qui vient en premier a la prééminence ; la justice est venue avant le péché et la bonté est venue avant le mal.",
    hi_title: "भलाई की श्रेष्ठता",
    hi_content: "जो पहले आता है उसकी श्रेष्ठता होती है; धार्मिकता पाप से पहले आई और भलाई बुराई से पहले आई।",
    zh_title: "shan liang de shou wei",
    zh_content: "xian lai de you shou wei; gong yi zai zui qian, shan liang zai e qian."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PREEMINENCE OF GOODNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->PREEMINENCE OF GOODNESS"
RETURN t, parent;
```
