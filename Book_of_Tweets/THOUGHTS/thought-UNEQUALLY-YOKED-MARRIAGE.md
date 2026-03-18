---
type: THOUGHT
name: "thought.UNEQUALLY YOKED MARRIAGE"
alias: "Thought: Unequally Yoked Marriage"
parent: "topic.MORALITY"
en_content: "The Christian who marries a unbeliever has the Devil for a father-in-law!"
tags: ["marriage", "unbeliever", "devil", "morality", "family"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012c)
CREATE (t:THOUGHT {    name: "thought.UNEQUALLY YOKED MARRIAGE",
    alias: "Thought: Unequally Yoked Marriage",
    parent: "topic.MORALITY",
    tags: ['marriage', 'unbeliever', 'devil', 'morality', 'family'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.UNEQUALLY YOKED MARRIAGE",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNEQUALLY YOKED MARRIAGE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->UNEQUALLY YOKED MARRIAGE"
RETURN t, parent;
```
