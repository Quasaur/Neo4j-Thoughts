---
type: THOUGHT
name: "thought.GODS"
alias: "Thought: Gods"
parent: "topic.PSYCHOLOGY"
tags: ["behavior", "intelligence", "power", "mercy", "compassion"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GODS",
    alias: "Thought: Gods",
    parent: "topic.PSYCHOLOGY",
    tags: ["behavior", "intelligence", "power", "mercy", "compassion"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GODS",
    ctype: "THOUGHT",
    en_title: "Gods",
    en_content: "",
    es_title: "GALLINERO",
    es_content: "No es la inteligencia ni el poder lo que nos convierte en dioses... sino la Misericordia y la Compasión.",
    fr_title: "DIEUX",
    fr_content: "Ce n'est ni l'intelligence ni le pouvoir qui font de nous des dieux... mais la Miséricorde et la Compassion.",
    hi_title: "भगवान",
    hi_content: "यह न तो बुद्धि है और न ही शक्ति जो हमें देवता बनाती है...बल्कि दया और करुणा है।",
    zh_title: "shén",
    zh_content: "shǐ wǒ men chéng wéi shén de jì bú shì zhì huì ， yě bú shì lì liàng …… ér shì rén cí hé tóng qíng xīn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GODS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->GODS"
RETURN t, parent;
```
