---
type: THOUGHT
name: "thought.GOD SIRED CHRIST"
alias: "Thought: God Sired Christ"
parent: "topic.THE GODHEAD"
en_content: "God did not create Christ, He SIRED Him! That's why Jesus is called THE ONLY BEGOTTEN of the Father."
tags: ["christ", "begotten", "sired", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Oct-2013)
CREATE (t:THOUGHT {    name: "thought.GOD SIRED CHRIST",
    alias: "Thought: God Sired Christ",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'begotten', 'sired', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD SIRED CHRIST",
    ctype: "THOUGHT",
    en_title: "God Sired Christ",
    en_content: "God did not create Christ, He SIRED Him! That's why Jesus is called THE ONLY BEGOTTEN of the Father.",
    es_title: "Dios Engendró a Cristo",
    es_content: "¡Dios no creó a Cristo, Él lo ENGENDRÓ! Por eso Jesús es llamado EL UNIGÉNITO del Padre.",
    fr_title: "Dieu a Engendré le Christ",
    fr_content: "Dieu n'a pas créé le Christ, Il l'a ENGENDRÉ ! C'est pourquoi Jésus est appelé LE FILS UNIQUE du Père.",
    hi_title: "परमेश्वर ने मसीह को जन्म दिया",
    hi_content: "परमेश्वर ने मसीह को सृजित नहीं किया, उसने उसे जन्म दिया! इसीलिए यीशु को पिता का एकलौता पुत्र कहा जाता है।",
    zh_title: "Shén shēng le Jīdū",
    zh_content: "Shén méiyǒu chuàngzào Jīdū, Tā shēng le Tā! Zhè jiùshì wèishénme Yēsū bèi chēngwéi Fùqīn de dúshēng ér."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD SIRED CHRIST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD SIRED CHRIST"
RETURN t, parent;
```
