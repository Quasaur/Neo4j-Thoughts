---
type: THOUGHT
name: "thought.GODS PRIORITIES VS OURS"
alias: "Thought: Gods Priorities Vs Ours"
parent: "topic.THE GODHEAD"
en_content: "The things that are important to God are rarely important to us."
tags: ["priorities", "importance", "god", "humanity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2013)
CREATE (t:THOUGHT {    name: "thought.GODS PRIORITIES VS OURS",
    alias: "Thought: Gods Priorities Vs Ours",
    parent: "topic.THE GODHEAD",
    tags: ['priorities', 'importance', 'god', 'humanity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GODS PRIORITIES VS OURS",
    ctype: "THOUGHT",
    en_title: "Gods Priorities Vs Ours",
    en_content: "The things that are important to God are rarely important to us.",
    es_title: "Las Prioridades de Dios Vs las Nuestras",
    es_content: "Las cosas que son importantes para Dios rara vez son importantes para nosotros.",
    fr_title: "Les Priorités de Dieu Vs les Nôtres",
    fr_content: "Les choses qui sont importantes pour Dieu sont rarement importantes pour nous.",
    hi_title: "परमेश्वर की प्राथमिकताएं बनाम हमारी",
    hi_content: "जो बातें परमेश्वर के लिए महत्वपूर्ण हैं वे शायद ही कभी हमारे लिए महत्वपूर्ण होती हैं।",
    zh_title: "Shàngdì de Yōuxiān Shìxiàng Yǔ Wǒmen de",
    zh_content: "Duì Shàngdì zhòngyào de shìqíng duì wǒmen lái shuō hěn shǎo shì zhòngyào de."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GODS PRIORITIES VS OURS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GODS PRIORITIES VS OURS"
RETURN t, parent;
```
