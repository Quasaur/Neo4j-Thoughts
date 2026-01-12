---
name: "thought.NATIONAL DEBT STATS"
alias: "Thought: National Debt Stats"
type: THOUGHT
en_content: "The National Debt: $16 TRILLION...that's $30 million every second for a year!!!"
parent: "topic.MORALITY"
tags:
- debt
- economics
- morality
- society
- judgment
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.NATIONAL DEBT STATS",
    alias: "Thought: National Debt Stats",
    parent: "topic.MORALITY",
    tags: ['debt', 'economics', 'morality', 'society', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NATIONAL DEBT STATS",
    en_title: "National Debt Stats",
    en_content: "The National Debt: $16 TRILLION...that's $30 million every second for a year!!!",
    es_title: "Estadísticas de deuda nacional",
    es_content: "La Deuda Nacional: $16 TRILLONES... ¡¡¡Eso es $30 millones cada segundo durante un año!!!",
    fr_title: "Statistiques de la dette nationale",
    fr_content: "La dette nationale : 16 000 milliards de dollars... soit 30 millions de dollars par seconde pendant un an !!!",
    hi_title: "राष्ट्रीय ऋण आँकड़े",
    hi_content: "राष्ट्रीय ऋण: $16 ट्रिलियन...अर्थात् एक वर्ष के लिए प्रति सेकंड $30 मिलियन!!!",
    zh_title: "国债统计",
    zh_content: "国债：16万亿美元……相当于一年每秒3000万美元！！！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NATIONAL DEBT STATS" AND c.name = "content.NATIONAL DEBT STATS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATIONAL DEBT STATS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.NATIONAL DEBT STATS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >NATIONAL DEBT STATS" }]->(child);
```
