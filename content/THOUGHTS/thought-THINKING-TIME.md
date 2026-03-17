---
type: THOUGHT
name: "thought.THINKING TIME"
alias: "Thought: Thinking Time"
parent: "topic.PSYCHOLOGY"
en_content: "God spends 100% of His Time thinking about us...how much time do we spend thinking about Him?"
tags: ["thinking", "time", "focus", "priorities", "god"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.THINKING TIME",
    alias: "Thought: Thinking Time",
    parent: "topic.PSYCHOLOGY",
    tags: ["thinking", "time", "focus", "priorities", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THINKING TIME",
    ctype: "THOUGHT",
    en_title: "Thinking Time",
    en_content: "God spends 100% of His Time thinking about us...how much time do we spend thinking about Him?",
    es_title: "TIEMPO PARA PENSAR",
    es_content: "Dios pasa el 100% de Su Tiempo pensando en nosotros... ¿cuánto tiempo pasamos nosotros pensando en Él?",
    fr_title: "TEMPS DE RÉFLEXION",
    fr_content: "Dieu passe 100 % de son temps à penser à nous... combien de temps passons-nous à penser à lui ?",
    hi_title: "सोचने का समय",
    hi_content: "भगवान अपना 100% समय हमारे बारे में सोचने में बिताते हैं... हम उनके बारे में सोचने में कितना समय बिताते हैं?",
    zh_title: "sī kǎo shí jiān",
    zh_content: "shàng dì yòng  100%  de shí jiān sī kǎo wǒ men …… wǒ men huā le duō shǎo shí jiān sī kǎo tā ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THINKING TIME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->THINKING TIME"
RETURN t, parent;
```
