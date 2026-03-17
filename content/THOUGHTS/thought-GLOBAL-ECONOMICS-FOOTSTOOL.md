---
type: THOUGHT
name: "thought.GLOBAL ECONOMICS FOOTSTOOL"
alias: "Thought: Global Economics Footstool"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "Global economics: God is making Christ's enemies His Footstool."
tags: ["sovereignty", "economics", "prophecy", "jesus", "victory"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL ECONOMICS FOOTSTOOL",
    alias: "Thought: Global Economics Footstool",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'economics', 'prophecy', 'jesus', 'victory'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLOBAL ECONOMICS FOOTSTOOL",
    ctype: "THOUGHT",
    en_title: "Global Economics Footstool",
    en_content: "Global economics: God is making Christ's enemies His Footstool.",
    es_title: "Economía Global: El Estrado de Cristo",
    es_content: "Economía global: Dios está haciendo de los enemigos de Cristo Su estrado.",
    fr_title: "Économie Mondiale : Le Marchepied du Christ",
    fr_content: "Économie mondiale : Dieu fait des ennemis du Christ son marchepied.",
    hi_title: "वैश्विक अर्थव्यवस्था: मसीह की चरणपीठ",
    hi_content: "वैश्विक अर्थव्यवस्था: परमेश्वर मसीह के शत्रुओं को उनकी चरणपीठ बना रहे हैं।",
    zh_title: "Quánqiú jīngjì: Jīdū de jiǎodèng 全球经济：基督的脚凳",
    zh_content: "Quánqiú jīngjì: Shàngdì zhèng shǐ Jīdū de dírén chéngwéi tā de jiǎodèng. 全球经济：上帝正使基督的敌人成为他的脚凳。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GLOBAL ECONOMICS FOOTSTOOL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GLOBAL ECONOMICS FOOTSTOOL"
RETURN t, parent;
```
