---
name: "thought.GODS SUPERIOR VALUE"
alias: "Thought: Gods Superior Value"
type: THOUGHT
en_content: "In the REAL WORLD, God is more valuable than all of us put together."
parent: "topic.THE GODHEAD"
tags:
- value
- reality
- god
- majesty
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.GODS SUPERIOR VALUE",
    alias: "Thought: Gods Superior Value",
    parent: "topic.THE GODHEAD",
    tags: ['value', 'reality', 'god', 'majesty', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS SUPERIOR VALUE",
    en_title: "Gods Superior Value",
    en_content: "In the REAL WORLD, God is more valuable than all of us put together.",
    es_title: "El Valor Superior de Dios",
    es_content: "En el MUNDO REAL, Dios es más valioso que todos nosotros juntos.",
    fr_title: "La Valeur Supérieure de Dieu",
    fr_content: "Dans le MONDE RÉEL, Dieu a plus de valeur que nous tous réunis.",
    hi_title: "परमेश्वर का उच्च मूल्य",
    hi_content: "वास्तविक दुनिया में, परमेश्वर हम सभी को एक साथ रखने से कहीं अधिक मूल्यवान हैं।",
    zh_title: "Shàngdì de chāoyujiàzhí 上帝的超越价值",
    zh_content: "Zài zhēnshí shìjiè zhōng, Shàngdì bǐ wǒmen suǒyǒu rén jiā qǐlái gèng yǒu jiàzhí. 在真实世界中，上帝比我们所有人加起来更有价值。"
});

MATCH (t:THOUGHT {name: "thought.GODS SUPERIOR VALUE"})
MATCH (c:CONTENT {name: "content.GODS SUPERIOR VALUE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS SUPERIOR VALUE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GODS SUPERIOR VALUE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS SUPERIOR VALUE" }]->(child);
```
