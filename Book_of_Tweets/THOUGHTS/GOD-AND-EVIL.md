---
name: "thought.GOD AND EVIL"
alias: "Thought: God And Evil"
type: THOUGHT
en_content: "God can use evil without being evil."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- evil
- providence
- justice
- divinity
level: 2
neo4j: false
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.GOD AND EVIL",
    alias: "Thought: God And Evil",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'evil', 'providence', 'justice', 'divinity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD AND EVIL",
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

MATCH (t:THOUGHT {name: "thought.GOD AND EVIL"})
MATCH (c:CONTENT {name: "content.GOD AND EVIL"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD AND EVIL" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.GOD AND EVIL"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY->GOD AND EVIL" }]->(child);
```
