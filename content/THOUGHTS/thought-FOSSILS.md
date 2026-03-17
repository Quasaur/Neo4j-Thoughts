---
type: THOUGHT
name: "thought.FOSSILS"
alias: "Thought: Fossils"
parent: "topic.GEOLOGY"
tags: ["geology", "fossils", "creationism", "intelligentdesign", "evidence"]
ptopic: "[[topic-GEOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FOSSILS",
    alias: "Thought: Fossils",
    parent: "topic.GEOLOGY",
    tags: ["geology", "fossils", "creationism", "intelligentdesign", "evidence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOSSILS",
    ctype: "THOUGHT",
    en_title: "Fossils",
    en_content: "",
    es_title: "FÓSILES",
    es_content: "¡Los fósiles, que según los evolucionistas demuestran cuán antigua es la Tierra, HAN SIDO DISEÑADOS EN LABORATORIOS EN 24 HORAS!",
    fr_title: "FOSSILES",
    fr_content: "Les fossiles, qui, selon les évolutionnistes, prouvent l'ancienneté de la Terre, ONT ÉTÉ CONÇUS DANS DES LABORATOIRES EN 24 HEURES !",
    hi_title: "जीवाश्मों",
    hi_content: "जीवाश्म, जिनके बारे में विकासवादियों का कहना है कि यह साबित करते हैं कि पृथ्वी कितनी प्राचीन है, 24 घंटों के भीतर प्रयोगशालाओं में इंजीनियर किए गए हैं!",
    zh_title: "huà shí",
    zh_content: "jìn huà lùn zhě chēng huà shí zhèng míng liǎo dì qiú yǒu duō gǔ lǎo ， ér huà shí yǐ zài  24  xiǎo shí nèi zài shí yàn shì zhōng dàn shēng ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FOSSILS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GEOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GEOLOGY->FOSSILS"
RETURN t, parent;
```
