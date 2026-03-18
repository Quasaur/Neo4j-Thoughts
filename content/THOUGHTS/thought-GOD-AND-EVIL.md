---
type: THOUGHT
name: "thought.GOD AND EVIL"
alias: "Thought: God And Evil"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "God can use evil without being evil."
tags: ["sovereignty", "evil", "providence", "justice", "divinity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD AND EVIL",
    alias: "Thought: God And Evil",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'evil', 'providence', 'justice', 'divinity'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD AND EVIL",
    ctype: "THOUGHT",
    en_title: "God And Evil",
    en_content: "God can use evil without being evil.",
    es_title: "Dios y el Mal",
    es_content: "Dios puede usar el mal sin ser malo.",
    fr_title: "Dieu et le Mal",
    fr_content: "Dieu peut utiliser le mal sans être mauvais.",
    hi_title: "ईश्वर और बुराई",
    hi_content: "भगवान बुरा होने बिना बुराई का उपयोग कर सकते हैं।",
    zh_title: "shàng dì yǔ è",
    zh_content: "shàng dì kě yǐ shǐ yòng è ér bù shì è de."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD AND EVIL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->GOD AND EVIL"
RETURN t, parent;
```
