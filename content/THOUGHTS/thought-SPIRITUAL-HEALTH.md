---
type: THOUGHT
name: "thought.SPIRITUAL HEALTH"
alias: "Thought: Spiritual Health"
parent: "topic.SPIRITUALITY"
en_content: "Spiritual Health: Doing what I know pleases God all of the time."
tags: ["health", "spiritual", "god", "allpleasing", "character"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SPIRITUAL HEALTH",
    alias: "Thought: Spiritual Health",
    parent: "topic.SPIRITUALITY",
    tags: ["health", "spiritual", "god", "allpleasing", "character"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPIRITUAL HEALTH",
    ctype: "THOUGHT",
    en_title: "Spiritual Health",
    en_content: "Spiritual Health: Doing what I know pleases God all of the time.",
    es_title: "SALUD ESPIRITUAL",
    es_content: "Salud Espiritual: Hacer lo que sé agrada a Dios todo el tiempo.",
    fr_title: "SANTÉ SPIRITUELLE",
    fr_content: "Santé spirituelle : Faire ce que je sais plaît à Dieu à tout moment.",
    hi_title: "आध्यात्मिक स्वास्थ्य",
    hi_content: "आध्यात्मिक स्वास्थ्य: जो मैं जानता हूं उसे करने से ईश्वर हर समय प्रसन्न होता है।",
    zh_title: "jīng shén jiàn kāng",
    zh_content: "jīng shén jiàn kāng ： zuò wǒ suǒ zhī dào de shì zǒng shì lìng shàng dì gāo xìng 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SPIRITUAL HEALTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->SPIRITUAL HEALTH"
RETURN t, parent;
```
