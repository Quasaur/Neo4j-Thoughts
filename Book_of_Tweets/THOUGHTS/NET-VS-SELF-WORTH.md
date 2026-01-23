---
name: "thought.NET VS SELF WORTH"
alias: "Thought: Net Vs Self Worth"
type: THOUGHT
en_content: "Don't confuse net worth with self-worth."
parent: "topic.HUMANITY"
tags:
- wealth
- value
- self_worth
- humanity
- confusion
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.NET VS SELF WORTH",
    alias: "Thought: Net Vs Self Worth",
    parent: "topic.HUMANITY",
    tags: ['wealth', 'value', 'self_worth', 'humanity', 'confusion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NET VS SELF WORTH",
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

MATCH (t:THOUGHT {name: "thought.NET VS SELF WORTH"})
MATCH (c:CONTENT {name: "content.NET VS SELF WORTH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NET VS SELF WORTH" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.NET VS SELF WORTH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NET VS SELF WORTH" }]->(child);
```
