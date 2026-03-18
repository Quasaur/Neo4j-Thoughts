---
type: THOUGHT
name: "thought.SHERBERT AND BLOWTORCH"
alias: "Thought: Sherbert And Blowtorch"
parent: "topic.WISDOM"
en_content: "You can't make sherbert with a blowtorch."
tags: ["wisdom", "logic", "metaphor", "patience", "methodology"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Jan-2011)
CREATE (t:THOUGHT {    name: "thought.SHERBERT AND BLOWTORCH",
    alias: "Thought: Sherbert And Blowtorch",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'logic', 'metaphor', 'patience', 'methodology'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SHERBERT AND BLOWTORCH",
    ctype: "THOUGHT",
    en_title: "Sherbert And Blowtorch",
    en_content: "You can't make sherbert with a blowtorch.",
    es_title: "Sorbete y Soplete",
    es_content: "No puedes hacer sorbete con un soplete.",
    fr_title: "Sorbet et Chalumeau",
    fr_content: "On ne peut pas faire du sorbet avec un chalumeau.",
    hi_title: "शर्बत और गैस टॉर्च",
    hi_content: "आप गैस टॉर्च से शर्बत नहीं बना सकते।",
    zh_title: "Bing Sha He Pen Deng",
    zh_content: "Ni bu neng yong pen deng zuo bing sha."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SHERBERT AND BLOWTORCH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->SHERBERT AND BLOWTORCH"
RETURN t, parent;
```
