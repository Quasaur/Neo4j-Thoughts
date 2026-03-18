---
type: THOUGHT
name: "thought.DEFINE FAITH WILL"
alias: "Thought: Define Faith Will"
parent: "topic.FAITH"
en_content: "New Definition of Faith: KNOWING God's General Will for me in every situation."
tags: ["faith", "will", "god", "knowledge"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE FAITH WILL",
    alias: "Thought: Define Faith Will",
    parent: "topic.FAITH",
    tags: ['faith', 'will', 'god', 'knowledge'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE FAITH WILL",
    ctype: "THOUGHT",
    en_title: "Define Faith Will",
    en_content: "New Definition of Faith: KNOWING God's Will for me in every situation.",
    es_title: "Definir Fe Voluntad",
    es_content: "Nueva Definición de Fe: CONOCER la Voluntad de Dios para mí en toda situación.",
    fr_title: "Définir la Foi Volonté",
    fr_content: "Nouvelle Définition de la Foi : CONNAÎTRE la Volonté de Dieu pour moi dans chaque situation.",
    hi_title: "विश्वास इच्छा को परिभाषित करें",
    hi_content: "विश्वास की नई परिभाषा: हर स्थिति में मेरे लिए भगवान की इच्छा जानना।",
    zh_title: "Dìngyì xìnxīn yìzhì",
    zh_content: "Xìnxīn de xīn dìngyì: Zài měi gè qíngkuàng xià dōuzhī shàngdì duì wǒ de yìzhì."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE FAITH WILL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITH->DEFINE FAITH WILL"
RETURN t, parent;
```
