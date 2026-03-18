---
type: THOUGHT
name: "thought.SALARY VS VALUE"
alias: "Thought: Salary Vs Value"
parent: "topic.HUMANITY"
en_content: "What's more valuable: my salary or me?"
tags: ["value", "identity", "humanity", "wealth", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012c)
CREATE (t:THOUGHT {    name: "thought.SALARY VS VALUE",
    alias: "Thought: Salary Vs Value",
    parent: "topic.HUMANITY",
    tags: ['value', 'identity', 'humanity', 'wealth', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SALARY VS VALUE",
    ctype: "THOUGHT",
    en_title: "Salary Vs Value",
    en_content: "What's more valuable: my salary or me?",
    es_title: "Salario Vs Valor",
    es_content: "¿Qué es más valioso: mi salario o yo?",
    fr_title: "Salaire Vs Valeur",
    fr_content: "Qu'est-ce qui est plus précieux : mon salaire ou moi ?",
    hi_title: "वेतन बनाम मूल्य",
    hi_content: "क्या अधिक मूल्यवान है: मेरा वेतन या मैं?",
    zh_title: "Xin Shui Yu Jia Zhi",
    zh_content: "Shen Me Geng You Jia Zhi: Wo De Xin Shui Hai Shi Wo?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SALARY VS VALUE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->SALARY VS VALUE"
RETURN t, parent;
```
