---
name: "thought.SHERBERT AND BLOWTORCH"
alias: "Thought: Sherbert And Blowtorch"
type: THOUGHT
en_content: "You can't make sherbert with a blowtorch."
parent: "topic.WISDOM"
tags:
- wisdom
- logic
- metaphor
- patience
- methodology
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.SHERBERT AND BLOWTORCH",
    alias: "Thought: Sherbert And Blowtorch",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'logic', 'metaphor', 'patience', 'methodology'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHERBERT AND BLOWTORCH",
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

MATCH (t:THOUGHT {name: "thought.SHERBERT AND BLOWTORCH"})
MATCH (c:CONTENT {name: "content.SHERBERT AND BLOWTORCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHERBERT AND BLOWTORCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.SHERBERT AND BLOWTORCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >SHERBERT AND BLOWTORCH" }]->(child);
```
