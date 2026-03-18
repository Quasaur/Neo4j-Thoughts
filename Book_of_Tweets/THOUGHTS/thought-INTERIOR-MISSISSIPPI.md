---
type: THOUGHT
name: "thought.INTERIOR MISSISSIPPI"
alias: "Thought: Interior Mississippi"
parent: "topic.MORALITY"
en_content: "\"You know what they say: 'Between Pittsburgh and Philadelphia is Mississippi!'\" -- Anonymous"
tags: ["society", "geography", "culture", "morality", "reflection"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2011)
CREATE (t:THOUGHT {    name: "thought.INTERIOR MISSISSIPPI",
    alias: "Thought: Interior Mississippi",
    parent: "topic.MORALITY",
    tags: ['society', 'geography', 'culture', 'morality', 'reflection'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.INTERIOR MISSISSIPPI",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INTERIOR MISSISSIPPI"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->INTERIOR MISSISSIPPI"
RETURN t, parent;
```
