---
type: THOUGHT
name: "thought.WHY"
alias: "Thought: Why"
parent: "topic.PSYCHOLOGY"
tags: ["children", "adults", "demanded", "cause", "why"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WHY",
    alias: "Thought: Why",
    parent: "topic.PSYCHOLOGY",
    tags: ["children", "adults", "demanded", "cause", "why"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WHY",
    ctype: "THOUGHT",
    en_title: "Why",
    en_content: "",
    es_title: "POR QUÉ",
    es_content: "¿Qué es lo que los niños suelen pasar por alto pero que los adultos exigen con frecuencia?
Una explicación.",
    fr_title: "POURQUOI",
    fr_content: "Qu'est-ce qui est souvent négligé par les enfants mais fréquemment exigé par les adultes ?
Une explication.",
    hi_title: "क्यों",
    hi_content: "वह कौन सी चीज़ है जिसे अक्सर बच्चे नज़रअंदाज़ कर देते हैं लेकिन बड़े लोग अक्सर उसकी मांग करते हैं?
एक स्पष्टीकरण.",
    zh_title: "wèi shén me",
    zh_content: "shén me shì hái zi men cháng cháng hū shì dàn dà rén cháng cháng yāo qiú de ？
 yí gè jiě shì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WHY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->WHY"
RETURN t, parent;
```
