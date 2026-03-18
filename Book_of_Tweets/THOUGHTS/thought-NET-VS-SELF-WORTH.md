---
type: THOUGHT
name: "thought.NET VS SELF WORTH"
alias: "Thought: Net Vs Self Worth"
parent: "topic.HUMANITY"
en_content: "Don't confuse net worth with self-worth."
tags: ["wealth", "value", "self_worth", "humanity", "confusion"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Apr-2012b)
CREATE (t:THOUGHT {    name: "thought.NET VS SELF WORTH",
    alias: "Thought: Net Vs Self Worth",
    parent: "topic.HUMANITY",
    tags: ['wealth', 'value', 'self_worth', 'humanity', 'confusion'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.NET VS SELF WORTH",
    ctype: "THOUGHT",
    en_title: "Net Vs Self Worth",
    en_content: "Don't confuse net worth with self-worth.",
    es_title: "Patrimonio Neto Vs Valor Personal",
    es_content: "No confundas el patrimonio neto con el valor personal.",
    fr_title: "Valeur Nette Vs Estime de Soi",
    fr_content: "Ne confondez pas la valeur nette avec l'estime de soi.",
    hi_title: "संपत्ति बनाम आत्म-मूल्य",
    hi_content: "शुद्ध संपत्ति को आत्म-मूल्य के साथ भ्रमित न करें।",
    zh_title: "Jingzichan Yu Ziwo Jiazhi",
    zh_content: "Bu yao ba jingzichan yu ziwo jiazhi hunxiao."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NET VS SELF WORTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->NET VS SELF WORTH"
RETURN t, parent;
```
