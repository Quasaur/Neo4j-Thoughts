---
name: "thought.AMERICAN POVERTY LINE"
alias: "Thought: American Poverty Line"
type: THOUGHT
en_content: "46 million Americans are at or below the poverty line."
parent: "topic.MORALITY"
tags:
- poverty
- economy
- society
- justice
- morality
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.AMERICAN POVERTY LINE",
    alias: "Thought: American Poverty Line",
    parent: "topic.MORALITY",
    tags: ['poverty', 'economy', 'society', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AMERICAN POVERTY LINE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMERICAN POVERTY LINE" AND c.name = "content.AMERICAN POVERTY LINE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AMERICAN POVERTY LINE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AMERICAN POVERTY LINE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AMERICAN POVERTY LINE" }]->(child);
```
