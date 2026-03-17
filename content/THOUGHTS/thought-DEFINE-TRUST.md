---
type: THOUGHT
name: "thought.DEFINE TRUST"
alias: "Thought: Define Trust"
parent: "topic.FAITH"
en_content: "TRUST is born of confidence in the midst ignorance."
tags: ["trust", "confidence", "ignorance", "faith", "philosophy"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE TRUST",
    alias: "Thought: Define Trust",
    parent: "topic.FAITH",
    tags: ['trust', 'confidence', 'ignorance', 'faith', 'philosophy'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE TRUST",
    ctype: "THOUGHT",
    en_title: "Define Trust",
    en_content: "TRUST is born of confidence in the midst of ignorance.",
    es_title: "Definición de confianza",
    es_content: "a confianza nace de la seguridad en medio de la incertidumbre.",
    fr_title: "Définir la confiance",
    fr_content: "La confiance naît de la certitude au milieu de l'incertitude.",
    hi_title: "विश्वास को परिभाषित करें",
    hi_content: "विश्वास अज्ञानता के बीच भरोसे से पैदा होता है।",
    zh_title: "Dìngyì xìnrèn",
    zh_content: "xìnrèn yuán yú zài wèizhī zhōng chǎnshēng de xìnxīn."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE TRUST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DEFINE TRUST"
RETURN t, parent;
```
