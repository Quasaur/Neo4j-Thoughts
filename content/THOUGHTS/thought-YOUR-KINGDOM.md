---
type: THOUGHT
name: "thought.YOUR KINGDOM"
alias: "Thought: Your Kingdom"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "To establish the Kingdom of the Heavens on this Earth, Christ must destroy your kingdom."
tags: ["kingdom", "heaven", "earth", "destruction", "jesus_christ"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.YOUR KINGDOM",
    alias: "Thought: Your Kingdom",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["kingdom", "heaven", "earth", "destruction", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.YOUR KINGDOM",
    ctype: "THOUGHT",
    en_title: "Your Kingdom",
    en_content: "To establish the Kingdom of the Heavens on this Earth, Christ must destroy your kingdom.",
    es_title: "TU REINO",
    es_content: "Para establecer el Reino de los Cielos en esta Tierra, Cristo debe destruir vuestro reino.",
    fr_title: "VOTRE ROYAUME",
    fr_content: "Pour établir le Royaume des Cieux sur cette Terre, le Christ doit détruire votre royaume.",
    hi_title: "आपका साम्राज्य",
    hi_content: "इस पृथ्वी पर स्वर्ग का राज्य स्थापित करने के लिए, मसीह को आपके राज्य को नष्ट करना होगा।",
    zh_title: "nǐ de wáng guó",
    zh_content: "wèi le zài dì qiú shàng jiàn lì tiān guó ， jī dū bì xū cuī huǐ nǐ men de wáng guó 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.YOUR KINGDOM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->YOUR KINGDOM"
RETURN t, parent;
```
