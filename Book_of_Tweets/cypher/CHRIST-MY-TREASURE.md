---
name: "thought.CHRIST MY TREASURE"
alias: "Thought: Christ My Treasure"
type: THOUGHT
en_content: "Christ is my Treasure, my Fortune, my Wealth, my NestEgg and my Riches!"
parent: "topic.THE GODHEAD"
tags:
- christ
- wealth
- treasure
- divinity
- value
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-May-2012)
CREATE (t:THOUGHT {
    name: "thought.CHRIST MY TREASURE",
    alias: "Thought: Christ My Treasure",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'wealth', 'treasure', 'divinity', 'value'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CHRIST MY TREASURE",
    en_title: "Christ My Treasure",
    en_content: "Christ is my Treasure, my Fortune, my Wealth, my NestEgg and my Riches!",
    es_title: "Cristo Mi Tesoro",
    es_content: "¡Cristo es mi Tesoro, mi Fortuna, mi Riqueza, mi Ahorro y mis Riquezas!",
    fr_title: "Le Christ Mon Trésor",
    fr_content: "Le Christ est mon Trésor, ma Fortune, ma Richesse, ma Réserve et mes Richesses !",
    hi_title: "मसीह मेरा खज़ाना",
    hi_content: "मसीह मेरा खज़ाना है, मेरा भाग्य, मेरी संपत्ति, मेरी बचत और मेरा धन!",
    zh_title: "Jīdū Shì Wǒ de Bǎo Zàng",
    zh_content: "Jīdū shì wǒ de Bǎo Zàng, wǒ de Cáifù, wǒ de Cáifu, wǒ de Chǔxù hé wǒ de Fùguì!"
});

MATCH (t:THOUGHT {name: "thought.CHRIST MY TREASURE"})
MATCH (c:CONTENT {name: "content.CHRIST MY TREASURE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRIST MY TREASURE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.CHRIST MY TREASURE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CHRIST MY TREASURE" }]->(child);
```
