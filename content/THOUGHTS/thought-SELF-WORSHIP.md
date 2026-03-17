---
type: THOUGHT
name: "thought.SELF WORSHIP"
alias: "Thought: Self Worship"
parent: "topic.RELIGION"
en_content: "Self-awareness without God-awareness is just self-worship, from which comes humanitarianism and evolutionary theory."
tags: ["narcissism", "self_worship", "religion", "humanitarian", "evolution"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SELF WORSHIP",
    alias: "Thought: Self Worship",
    parent: "topic.RELIGION",
    tags: ["narcissism", "self_worship", "religion", "humanitarian", "evolution"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SELF WORSHIP",
    ctype: "THOUGHT",
    en_title: "Self Worship",
    en_content: "Self-awareness without God-awareness is just self-worship, from which comes humanitarianism and evolutionary theory.",
    es_title: "AUTOADORACIÓN",
    es_content: "La autoconciencia sin conciencia de Dios es sólo adoración a uno mismo, de la que proviene el humanitarismo y la teoría de la evolución.",
    fr_title: "ADORATION DE SOI",
    fr_content: "La conscience de soi sans la conscience de Dieu n’est qu’un culte de soi, d’où découlent l’humanitarisme et la théorie évolutionniste.",
    hi_title: "आत्म पूजा",
    hi_content: "ईश्वर-जागरूकता के बिना आत्म-जागरूकता सिर्फ आत्म-पूजा है, जिससे मानवतावाद और विकासवादी सिद्धांत आता है।",
    zh_title: "zì wǒ chóng bài",
    zh_content: "méi yǒu shàng dì yì shí de zì wǒ yì shí zhǐ shì zì wǒ chóng bài ， yóu cǐ chǎn shēng rén dào zhǔ yì hé jìn huà lùn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SELF WORSHIP"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->SELF WORSHIP"
RETURN t, parent;
```
