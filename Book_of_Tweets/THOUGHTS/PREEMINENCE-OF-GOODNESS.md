---
name: "thought.PREEMINENCE OF GOODNESS"
alias: "Thought: Preeminence Of Goodness"
type: THOUGHT
en_content: "That which comes first has the preeminence; righteousness came before sin and goodness came before evil."
parent: "topic.THE GODHEAD"
tags:
- goodness
- righteousness
- eternity
- character
- preeminence
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.PREEMINENCE OF GOODNESS",
    alias: "Thought: Preeminence Of Goodness",
    parent: "topic.THE GODHEAD",
    tags: ['goodness', 'righteousness', 'eternity', 'character', 'preeminence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PREEMINENCE OF GOODNESS",
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

MATCH (t:THOUGHT {name: "thought.PREEMINENCE OF GOODNESS"})
MATCH (c:CONTENT {name: "content.PREEMINENCE OF GOODNESS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PREEMINENCE OF GOODNESS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.PREEMINENCE OF GOODNESS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >PREEMINENCE OF GOODNESS" }]->(child);
```
