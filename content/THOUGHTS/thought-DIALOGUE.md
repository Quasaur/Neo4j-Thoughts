---
type: THOUGHT
name: "thought.DIALOGUE"
alias: "Thought: Dialogue"
parent: "topic.EVIL"
tags: ["devil", "ego", "slave", "sin", "tongue"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DIALOGUE",
    alias: "Thought: Dialogue",
    parent: "topic.EVIL",
    tags: ["devil", "ego", "slave", "sin", "tongue"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DIALOGUE",
    ctype: "THOUGHT",
    en_title: "Dialogue",
    en_content: "",
    es_title: "DIÁLOGO",
    es_content: "Discutir con el Diablo es extremadamente peligroso porque con demasiada frecuencia compartimos su punto de vista.",
    fr_title: "DIALOGUE",
    fr_content: "Discuter avec le Diable est extrêmement dangereux car bien trop souvent nous partageons son point de vue.",
    hi_title: "वार्ता",
    hi_content: "शैतान के साथ बहस करना बेहद खतरनाक है क्योंकि अक्सर हम उसका दृष्टिकोण साझा करते हैं।",
    zh_title: "duì huà",
    zh_content: "yǔ mó guǐ zhēng lùn shì jí qí wēi xiǎn de ， yīn wèi wǒ men cháng cháng tóng yì tā de guān diǎn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIALOGUE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->DIALOGUE"
RETURN t, parent;
```
