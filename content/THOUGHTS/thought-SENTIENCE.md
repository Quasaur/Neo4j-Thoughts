---
type: THOUGHT
name: "thought.SENTIENCE"
alias: "Thought: Sentience"
parent: "topic.SPIRITS"
tags: ["spirits", "sentience", "god", "selfaware", "iam"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SENTIENCE",
    alias: "Thought: Sentience",
    parent: "topic.SPIRITS",
    tags: ["spirits", "sentience", "god", "selfaware", "iam"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SENTIENCE",
    ctype: "THOUGHT",
    en_title: "Sentience",
    en_content: "",
    es_title: "SENTENCIA",
    es_content: "¡Qué maravilla es la sensibilidad: no sólo soy para Dios, sino que lo soy para mí mismo!",
    fr_title: "SENTIENCE",
    fr_content: "Quelle merveille que la sensibilité : non seulement je suis pour Dieu, mais je le suis pour moi-même !",
    hi_title: "चेतना",
    hi_content: "भावना क्या आश्चर्य है: न केवल मैं ईश्वर के प्रति हूँ, बल्कि मैं स्वयं के प्रति भी हूँ!",
    zh_title: "zhī jué",
    zh_content: "zhī jué shì duō me qí miào a ： wǒ bù jǐn duì shàng dì ér yán ， ér qiě duì wǒ zì jǐ yě rú cǐ ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SENTIENCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITS->SENTIENCE"
RETURN t, parent;
```
