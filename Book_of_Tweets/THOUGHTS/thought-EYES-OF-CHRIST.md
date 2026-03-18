---
type: THOUGHT
name: "thought.EYES OF CHRIST"
alias: "Thought: Eyes Of Christ"
parent: "topic.THE GODHEAD"
en_content: "From the smallest subatomic particle to the deepest intent of the human heart, the Eyes of Christ miss nothing."
tags: ["omniscience", "christ", "science", "heart", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2012)
CREATE (t:THOUGHT {    name: "thought.EYES OF CHRIST",
    alias: "Thought: Eyes Of Christ",
    parent: "topic.THE GODHEAD",
    tags: ['omniscience', 'christ', 'science', 'heart', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.EYES OF CHRIST",
    ctype: "THOUGHT",
    en_title: "Eyes Of Christ",
    en_content: "From the smallest subatomic particle to the deepest intent of the human heart, the Eyes of Christ miss nothing.",
    es_title: "Los Ojos de Cristo",
    es_content: "Desde la partícula subatómica más pequeña hasta la intención más profunda del corazón humano, los Ojos de Cristo no pasan por alto nada.",
    fr_title: "Les Yeux du Christ",
    fr_content: "De la plus petite particule subatomique à l'intention la plus profonde du cœur humain, les Yeux du Christ ne ratent rien.",
    hi_title: "मसीह की आँखें",
    hi_content: "सबसे छोटे उपपरमाण्विक कण से लेकर मानव हृदय के गहरे से गहरे इरादे तक, मसीह की आँखें कुछ भी नहीं चूकतीं।",
    zh_title: "Jīdū de Yǎnjīng",
    zh_content: "Cóng zuì xiǎo de yàyuánzǐ lìzǐ dào rénlèi xīnlíng zuì shēn de yìtú, Jīdū de Yǎnjīng bù cuòguò rènhé shìwù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EYES OF CHRIST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->EYES OF CHRIST"
RETURN t, parent;
```
