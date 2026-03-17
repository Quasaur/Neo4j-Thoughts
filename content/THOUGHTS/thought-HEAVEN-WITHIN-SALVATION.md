---
type: THOUGHT
name: "thought.HEAVEN WITHIN SALVATION"
alias: "Thought: Heaven Within Salvation"
parent: "topic.GRACE"
en_content: "The objective of Salvation is not to get you into Heaven, but to get Heaven into you."
tags: ["salvation", "heaven", "transformation", "grace", "presence"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN WITHIN SALVATION",
    alias: "Thought: Heaven Within Salvation",
    parent: "topic.GRACE",
    tags: ['salvation', 'heaven', 'transformation', 'grace', 'presence'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HEAVEN WITHIN SALVATION",
    ctype: "THOUGHT",
    en_title: "Heaven Within Salvation",
    en_content: "The objective of Salvation is not to get you into Heaven, but to get Heaven into you.",
    es_title: "El Cielo Dentro de la Salvación",
    es_content: "El objetivo de la Salvación no es llevarte al Cielo, sino traer el Cielo dentro de ti.",
    fr_title: "Le Ciel Dans le Salut",
    fr_content: "L'objectif du Salut n'est pas de vous amener au Ciel, mais d'amener le Ciel en vous.",
    hi_title: "मोक्ष के भीतर स्वर्ग",
    hi_content: "मोक्ष का उद्देश्य आपको स्वर्ग में ले जाना नहीं है, बल्कि स्वर्ग को आप के भीतर लाना है।",
    zh_title: "Jiù'ēn zhī zhōng de tiāntáng",
    zh_content: "Jiù'ēn de mùdì bùshì ràng nǐ jìnrù tiāntáng, ér shì ràng tiāntáng jìnrù nǐ de nèixīn."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEAVEN WITHIN SALVATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->HEAVEN WITHIN SALVATION"
RETURN t, parent;
```
