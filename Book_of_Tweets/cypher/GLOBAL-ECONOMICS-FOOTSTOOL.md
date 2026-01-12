---
name: "thought.GLOBAL ECONOMICS FOOTSTOOL"
alias: "Thought: Global Economics Footstool"
type: THOUGHT
en_content: "Global economics: God is making Christ's enemies His Footstool."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- economics
- prophecy
- jesus
- victory
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL ECONOMICS FOOTSTOOL",
    alias: "Thought: Global Economics Footstool",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'economics', 'prophecy', 'jesus', 'victory'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLOBAL ECONOMICS FOOTSTOOL",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GLOBAL ECONOMICS FOOTSTOOL" AND c.name = "content.GLOBAL ECONOMICS FOOTSTOOL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLOBAL ECONOMICS FOOTSTOOL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.GLOBAL ECONOMICS FOOTSTOOL"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >GLOBAL ECONOMICS FOOTSTOOL" }]->(child);
```
