---
name: "thought.UNEMPLOYMENT STATS"
alias: "Thought: Unemployment Stats"
type: THOUGHT
en_content: "White Unemployment : 9%...Black Unemployment : 16%."
parent: "topic.MORALITY"
tags:
- justice
- economy
- race
- society
- morality
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011c)
CREATE (t:THOUGHT {
    name: "thought.UNEMPLOYMENT STATS",
    alias: "Thought: Unemployment Stats",
    parent: "topic.MORALITY",
    tags: ['justice', 'economy', 'race', 'society', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNEMPLOYMENT STATS",
    en_title: "Unemployment Stats",
    en_content: "White Unemployment : 9%...Black Unemployment : 16%.",
    es_title: "Estadísticas de desempleo",
    es_content: "Desempleo de blancos: 9%... Desempleo de negros: 16%.",
    fr_title: "Statistiques du chômage",
    fr_content: "Chômage des Blancs : 9%...Chômage des Noirs : 16%.",
    hi_title: "बेरोज़गारी आँकड़े",
    hi_content: "श्वेत बेरोज़गारी: 9%...काली बेरोज़गारी: 16%।",
    zh_title: "失业统计",
    zh_content: "白人失业率：9%...黑人失业率：16%。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNEMPLOYMENT STATS" AND c.name = "content.UNEMPLOYMENT STATS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNEMPLOYMENT STATS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.UNEMPLOYMENT STATS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >UNEMPLOYMENT STATS" }]->(child);
```
