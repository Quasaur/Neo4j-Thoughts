---
type: THOUGHT
name: "thought.DISAGREEMENT"
alias: "Thought: Disagreement"
parent: "topic.FAITH"
tags: ["faith", "doctrine", "apostasy", "heresy", "conflict"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DISAGREEMENT",
    alias: "Thought: Disagreement",
    parent: "topic.FAITH",
    tags: ["faith", "doctrine", "apostasy", "heresy", "conflict"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DISAGREEMENT",
    ctype: "THOUGHT",
    en_title: "Disagreement",
    en_content: "Arguing with the Devil is extremely dangerous because far too often we share his point of view.",
    es_title: "DESACUERDO",
    es_content: "Discutir con el Diablo es extremadamente peligroso porque con demasiada frecuencia compartimos su punto de vista.",
    fr_title: "DÉSACCORD",
    fr_content: "Discuter avec le Diable est extrêmement dangereux car bien trop souvent nous partageons son point de vue.",
    hi_title: "बहस",
    hi_content: "शैतान के साथ बहस करना बेहद खतरनाक है क्योंकि अक्सर हम उसका दृष्टिकोण साझा करते हैं।",
    zh_title: "fēn qí",
    zh_content: "yǔ mó guǐ zhēng lùn shì jí qí wēi xiǎn de ， yīn wèi wǒ men cháng cháng tóng yì tā de guān diǎn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DISAGREEMENT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITH->DISAGREEMENT"
RETURN t, parent;
```
