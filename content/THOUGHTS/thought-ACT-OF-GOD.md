---
type: THOUGHT
name: "thought.ACT OF GOD"
alias: "Thought: Act of God"
parent: "topic.PSYCHOLOGY"
en_content: "If every person is an Act of God, what can my wife teach me about God?"
tags: ["person", "people", "wife", "husband", "image_of_god"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ACT OF GOD",
    alias: "Thought: Act of God",
    parent: "topic.PSYCHOLOGY",
    tags: ["person", "people", "wife", "husband", "image_of_god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ACT OF GOD",
    ctype: "THOUGHT",
    en_title: "Act of God",
    en_content: "If every person is an Act of God, what can my wife teach me about God?",
    es_title: "Caso de fuerza mayor",
    es_content: "Si cada persona es un acto de Dios, ¿qué puede enseñarme mi esposa sobre Dios?",
    fr_title: "Acte de Dieu",
    fr_content: "Si chaque personne est un acte de Dieu, que peut m’apprendre ma femme sur Dieu ?",
    hi_title: "दैवीय घटना",
    hi_content: "यदि प्रत्येक व्यक्ति ईश्वर का कार्य है, तो मेरी पत्नी मुझे ईश्वर के बारे में क्या सिखा सकती है?",
    zh_title: "tiān zāi",
    zh_content: "rú guǒ měi gè rén dōu shì shàng dì de zuò wéi ， wǒ de qī zǐ néng jiào wǒ shén me guān yú shàng dì de shì ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ACT OF GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->ACT OF GOD"
RETURN t, parent;
```
