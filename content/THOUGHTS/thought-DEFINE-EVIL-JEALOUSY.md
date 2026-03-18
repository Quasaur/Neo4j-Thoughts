---
type: THOUGHT
name: "thought.DEFINE EVIL JEALOUSY"
alias: "Thought: Define Evil Jealousy"
parent: "topic.EVIL"
en_content: "Evil Jealousy: fear of loss."
tags: ["jealousy", "fear", "evil", "character", "philosophy"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE EVIL JEALOUSY",
    alias: "Thought: Define Evil Jealousy",
    parent: "topic.EVIL",
    tags: ['jealousy', 'fear', 'evil', 'character', 'philosophy'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE EVIL JEALOUSY",
    ctype: "THOUGHT",
    en_title: "Define Evil Jealousy",
    en_content: "Evil Jealousy: fear of loss.",
    es_title: "Definir Celos Malvados",
    es_content: "Celos Malvados: miedo a la pérdida.",
    fr_title: "Définir la Jalousie Maléfique",
    fr_content: "Jalousie Maléfique : peur de la perte.",
    hi_title: "बुराई ईर्ष्या को परिभाषित करें",
    hi_content: "बुराई ईर्ष्या: हानि का डर।",
    zh_title: "Dìngyì è'è de jídù",
    zh_content: "È'è de jídù: Pà shīqù."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE EVIL JEALOUSY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->DEFINE EVIL JEALOUSY"
RETURN t, parent;
```
