---
name: "thought.SALARY VS VALUE"
alias: "Thought: Salary Vs Value"
type: THOUGHT
en_content: "What's more valuable: my salary or me?"
parent: "topic.HUMANITY"
tags:
- value
- identity
- humanity
- wealth
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.SALARY VS VALUE",
    alias: "Thought: Salary Vs Value",
    parent: "topic.HUMANITY",
    tags: ['value', 'identity', 'humanity', 'wealth', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SALARY VS VALUE",
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

MATCH (t:THOUGHT {name: "thought.SALARY VS VALUE"})
MATCH (c:CONTENT {name: "content.SALARY VS VALUE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SALARY VS VALUE" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.SALARY VS VALUE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->SALARY VS VALUE" }]->(child);
```
