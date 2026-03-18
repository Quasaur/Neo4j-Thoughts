---
type: THOUGHT
name: "thought.PURSUIT OF HAPPINESS"
alias: "Thought: Pursuit Of Happiness"
parent: "topic.THE GODHEAD"
en_content: "The pursuit of God is the pursuit of happiness. The pursuit of happiness is the pursuit of God."
tags: ["god", "happiness", "pursuit", "divinity", "truth"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Jul-2013)
CREATE (t:THOUGHT {    name: "thought.PURSUIT OF HAPPINESS",
    alias: "Thought: Pursuit Of Happiness",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'happiness', 'pursuit', 'divinity', 'truth'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.PURSUIT OF HAPPINESS",
    ctype: "THOUGHT",
    en_title: "Pursuit Of Happiness",
    en_content: "The pursuit of God is the pursuit of happiness. The pursuit of happiness is the pursuit of God.",
    es_title: "Búsqueda de la Felicidad",
    es_content: "La búsqueda de Dios es la búsqueda de la felicidad. La búsqueda de la felicidad es la búsqueda de Dios.",
    fr_title: "Poursuite du Bonheur",
    fr_content: "La poursuite de Dieu est la poursuite du bonheur. La poursuite du bonheur est la poursuite de Dieu.",
    hi_title: "खुशी की खोज",
    hi_content: "भगवान की खोज खुशी की खोज है। खुशी की खोज भगवान की खोज है।",
    zh_title: "Zhuiqiu Xingfu",
    zh_content: "Zhuiqiu Shangdi jiu shi zhuiqiu xingfu. Zhuiqiu xingfu jiu shi zhuiqiu Shangdi."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PURSUIT OF HAPPINESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->PURSUIT OF HAPPINESS"
RETURN t, parent;
```
