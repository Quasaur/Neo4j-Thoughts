---
type: THOUGHT
name: "thought.AMERICAN POVERTY LINE"
alias: "Thought: American Poverty Line"
parent: "topic.MORALITY"
en_content: "46 million Americans are at or below the poverty line."
tags: ["poverty", "economy", "society", "justice", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Sep-2011)
CREATE (t:THOUGHT {    name: "thought.AMERICAN POVERTY LINE",
    alias: "Thought: American Poverty Line",
    parent: "topic.MORALITY",
    tags: ['poverty', 'economy', 'society', 'justice', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.AMERICAN POVERTY LINE",
    ctype: "THOUGHT",
    en_title: "American Poverty Line",
    en_content: "46 million Americans are at or below the poverty line.",
    es_title: "Línea de Pobreza Estadounidense",
    es_content: "46 millones de estadounidenses están en o por debajo de la línea de pobreza.",
    fr_title: "Seuil de Pauvreté Américain",
    fr_content: "46 millions d'Américains sont au niveau ou en dessous du seuil de pauvreté.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "4 करोड़ 60 लाख अमेरिकी गरीबी रेखा पर या उससे नीचे हैं।",
    zh_title: "Měiguó pínkùn xiàn",
    zh_content: "Sì qiān liù bǎi wàn Měiguó rén chǔyú huò dīyú pínkùn xiàn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AMERICAN POVERTY LINE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->AMERICAN POVERTY LINE"
RETURN t, parent;
```
