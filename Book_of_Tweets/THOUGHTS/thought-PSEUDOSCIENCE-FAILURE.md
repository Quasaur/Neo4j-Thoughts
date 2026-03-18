---
type: THOUGHT
name: "thought.PSEUDOSCIENCE FAILURE"
alias: "Thought: Pseudoscience Failure"
parent: "topic.PHILOSOPHY"
en_content: "The Standard Model: pseudo-science's failure to convince the world of a God-less universe."
tags: ["science", "philosophy", "atheism", "truth", "creation"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Aug-2010)
CREATE (t:THOUGHT {    name: "thought.PSEUDOSCIENCE FAILURE",
    alias: "Thought: Pseudoscience Failure",
    parent: "topic.PHILOSOPHY",
    tags: ['science', 'philosophy', 'atheism', 'truth', 'creation'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.PSEUDOSCIENCE FAILURE",
    ctype: "THOUGHT",
    en_title: "Pseudoscience Failure",
    en_content: "The Standard Model: pseudo-science's failure to convince the world of a God-less universe.",
    es_title: "Fracaso de la pseudociencia",
    es_content: "El modelo estándar: el fracaso de la pseudociencia a la hora de convencer al mundo de un universo sin Dios.",
    fr_title: "Échec de la pseudoscience",
    fr_content: "Le modèle standard : l'échec de la pseudo-science à convaincre le monde d'un univers sans Dieu.",
    hi_title: "छद्म विज्ञान विफलता",
    hi_content: "मानक मॉडल: दुनिया को ईश्वर-विहीन ब्रह्मांड के बारे में समझाने में छद्म विज्ञान की विफलता।",
    zh_title: "wěi kē xué de shī bài",
    zh_content: "biāo zhǔn mó xíng ： wěi kē xué wèi néng ràng shì jiè xiāng xìn yǔ zhòu shì wú shén de 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PSEUDOSCIENCE FAILURE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->PSEUDOSCIENCE FAILURE"
RETURN t, parent;
```
