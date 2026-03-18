---
type: THOUGHT
name: "thought.UNEMPLOYMENT STATS"
alias: "Thought: Unemployment Stats"
parent: "topic.MORALITY"
en_content: "White Unemployment : 9%...Black Unemployment : 16%."
tags: ["justice", "economy", "race", "society", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011c)
CREATE (t:THOUGHT {    name: "thought.UNEMPLOYMENT STATS",
    alias: "Thought: Unemployment Stats",
    parent: "topic.MORALITY",
    tags: ['justice', 'economy', 'race', 'society', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.UNEMPLOYMENT STATS",
    ctype: "THOUGHT",
    en_title: "Unemployment Stats",
    en_content: "White Unemployment : 9%...Black Unemployment : 16%.",
    es_title: "Estadísticas de desempleo",
    es_content: "Desempleo de blancos: 9%... Desempleo de negros: 16%.",
    fr_title: "Statistiques du chômage",
    fr_content: "Chômage des Blancs : 9%...Chômage des Noirs : 16%.",
    hi_title: "बेरोज़गारी आँकड़े",
    hi_content: "श्वेत बेरोज़गारी: 9%...काली बेरोज़गारी: 16%।",
    zh_title: "shī yè tǒng jì",
    zh_content: "bái rén shī yè lǜ ：9%... hēi rén shī yè lǜ ：16%。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNEMPLOYMENT STATS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->UNEMPLOYMENT STATS"
RETURN t, parent;
```
