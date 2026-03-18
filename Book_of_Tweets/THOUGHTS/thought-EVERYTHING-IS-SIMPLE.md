---
type: THOUGHT
name: "thought.EVERYTHING IS SIMPLE"
alias: "Thought: Everything Is Simple"
parent: "topic.THE GODHEAD"
en_content: "To God complexity itself does not exists...everything is simple to God."
tags: ["simplicity", "complexity", "knowledge", "divinity", "god"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Oct-2011a)
CREATE (t:THOUGHT {    name: "thought.EVERYTHING IS SIMPLE",
    alias: "Thought: Everything Is Simple",
    parent: "topic.THE GODHEAD",
    tags: ['simplicity', 'complexity', 'knowledge', 'divinity', 'god'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.EVERYTHING IS SIMPLE",
    ctype: "THOUGHT",
    en_title: "Everything Is Simple",
    en_content: "To God complexity itself does not exists...everything is simple to God.",
    es_title: "Todo Es Simple",
    es_content: "Para Dios la complejidad en sí misma no existe...todo es simple para Dios.",
    fr_title: "Tout Est Simple",
    fr_content: "Pour Dieu la complexité elle-même n'existe pas...tout est simple pour Dieu.",
    hi_title: "सब कुछ सरल है",
    hi_content: "परमेश्वर के लिए जटिलता स्वयं अस्तित्व में नहीं है...परमेश्वर के लिए सब कुछ सरल है।",
    zh_title: "Yiqie Dou Shi Jiandan De",
    zh_content: "Dui yu Shangdi lai shuo, fuza xing benshen bing bu cunzai...dui yu Shangdi lai shuo yiqie dou shi jiandan de."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVERYTHING IS SIMPLE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->EVERYTHING IS SIMPLE"
RETURN t, parent;
```
