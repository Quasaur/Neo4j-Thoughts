---
type: THOUGHT
name: "thought.GRACE VS MERIT"
alias: "Thought: Grace Vs Merit"
parent: "topic.GRACE"
en_content: "The merit system and Grace are incompatible...we have to choose one or the other."
tags: ["grace", "merit", "salvation", "choice", "gospel"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GRACE VS MERIT",
    alias: "Thought: Grace Vs Merit",
    parent: "topic.GRACE",
    tags: ['grace', 'merit', 'salvation', 'choice', 'gospel'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE VS MERIT",
    ctype: "THOUGHT",
    en_title: "Grace Vs Merit",
    en_content: "The merit system and Grace are incompatible...we have to choose one or the other.",
    es_title: "Gracia versus Mérito",
    es_content: "El sistema de méritos y la Gracia son incompatibles... tenemos que elegir uno u otro.",
    fr_title: "Grâce contre Mérite",
    fr_content: "Le système de mérite et la Grâce sont incompatibles... nous devons choisir l'un ou l'autre.",
    hi_title: "कृपा बनाम योग्यता",
    hi_content: "योग्यता प्रणाली और कृपा असंगत हैं... हमें एक या दूसरा चुनना होगा।",
    zh_title: "Ēndiǎn yǔ gōngjixué  ēn diǎn yǔ gōng jì shuō",
    zh_content: "Gōngjixué zhìduù hé ēndiǎn shì bù xiāng róng de... wǒmen bìxū xuǎnzé qí yī.  gōng jì shuō zhì dù hé ēn diǎn shì bù xiāng róng de ... wǒ men bì xū xuǎn zé qí yī 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GRACE VS MERIT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GRACE VS MERIT"
RETURN t, parent;
```
