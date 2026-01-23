---
name: "thought.UNEQUALLY YOKED MARRIAGE"
alias: "Thought: Unequally Yoked Marriage"
type: THOUGHT
en_content: "The Christian who marries a unbeliever has the Devil for a father-in-law!"
parent: "topic.MORALITY"
tags:
- marriage
- unbeliever
- devil
- morality
- family
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012c)
CREATE (t:THOUGHT {
    name: "thought.UNEQUALLY YOKED MARRIAGE",
    alias: "Thought: Unequally Yoked Marriage",
    parent: "topic.MORALITY",
    tags: ['marriage', 'unbeliever', 'devil', 'morality', 'family'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNEQUALLY YOKED MARRIAGE",
    en_title: "Unequally Yoked Marriage",
    en_content: "The Christian who marries a unbeliever has the Devil for a father-in-law!",
    es_title: "Matrimonio en Yugo Desigual",
    es_content: "¡El cristiano que se casa con un incrédulo tiene al Diablo como suegro!",
    fr_title: "Mariage sous un Joug Inégal",
    fr_content: "Le chrétien qui épouse un non-croyant a le Diable pour beau-père !",
    hi_title: "असमान जुए में विवाह",
    hi_content: "जो मसीही अविश्वासी से विवाह करता है, उसका ससुर शैतान होता है!",
    zh_title: "Bu Pei De E Lian He",
    zh_content: "Ji Du Tu Yu Bu Xin Zhe Jie Hun, Mo Gui Jiu Cheng Le Ta De Yue Fu!"
});

MATCH (t:THOUGHT {name: "thought.UNEQUALLY YOKED MARRIAGE"})
MATCH (c:CONTENT {name: "content.UNEQUALLY YOKED MARRIAGE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNEQUALLY YOKED MARRIAGE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.UNEQUALLY YOKED MARRIAGE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >UNEQUALLY YOKED MARRIAGE" }]->(child);
```
