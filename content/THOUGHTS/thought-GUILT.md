---
type: THOUGHT
name: "thought.GUILT"
alias: "Thought: Guilt"
parent: "topic.PSYCHOLOGY"
tags: ["guilt", "expression", "ego", "self", "conscience"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GUILT",
    alias: "Thought: Guilt",
    parent: "topic.PSYCHOLOGY",
    tags: ["guilt", "expression", "ego", "self", "conscience"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GUILT",
    ctype: "THOUGHT",
    en_title: "Guilt",
    en_content: "",
    es_title: "CULPA",
    es_content: "La culpa es sólo otra expresión del ego.",
    fr_title: "CULPABILITÉ",
    fr_content: "La culpabilité n'est qu'une autre expression de l'ego.",
    hi_title: "अपराध",
    hi_content: "अपराध बोध अहंकार की ही एक और अभिव्यक्ति है।",
    zh_title: "yǒu zuì",
    zh_content: "nèi jiù zhǐ shì zì wǒ de lìng yī zhǒng biǎo dá 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GUILT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->GUILT"
RETURN t, parent;
```
