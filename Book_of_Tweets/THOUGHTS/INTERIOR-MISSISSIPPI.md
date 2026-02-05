---
name: "thought.INTERIOR MISSISSIPPI"
alias: "Thought: Interior Mississippi"
type: THOUGHT
en_content: "\"You know what they say: 'Between Pittsburgh and Philadelphia is Mississippi!'\" -- Anonymous"
parent: "topic.MORALITY"
tags:
- society
- geography
- culture
- morality
- reflection
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.INTERIOR MISSISSIPPI",
    alias: "Thought: Interior Mississippi",
    parent: "topic.MORALITY",
    tags: ['society', 'geography', 'culture', 'morality', 'reflection'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INTERIOR MISSISSIPPI",
    en_title: "Interior Mississippi",
    en_content: "\"You know what they say: 'Between Pittsburgh and Philadelphia is Mississippi!'\" -- Anonymous",
    es_title: "El interior del Misisipi",
    es_content: "\",
    fr_title: "L'intérieur du Mississippi",
    fr_content: "\",
    hi_title: "मिसिसिपी का आंतरिक भाग",
    hi_content: "\",
    zh_title: "mì xī xī bǐ hé de nèi bù",
    zh_content: "\"
});

MATCH (t:THOUGHT {name: "thought.INTERIOR MISSISSIPPI"})
MATCH (c:CONTENT {name: "content.INTERIOR MISSISSIPPI"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTERIOR MISSISSIPPI" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.INTERIOR MISSISSIPPI"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->INTERIOR MISSISSIPPI" }]->(child);
```
