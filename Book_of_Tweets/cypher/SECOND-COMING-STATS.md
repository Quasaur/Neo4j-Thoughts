---
name: "thought.SECOND COMING STATS"
alias: "Thought: Second Coming Stats"
type: THOUGHT
en_content: "One out of every 24 verses in the New Testament refers to the Second Coming of Christ."
parent: "topic.RELIGION"
tags:
- prophecy
- jesus
- return
- bible
- statistics
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Dec-2011c)
CREATE (t:THOUGHT {
    name: "thought.SECOND COMING STATS",
    alias: "Thought: Second Coming Stats",
    parent: "topic.RELIGION",
    tags: ['prophecy', 'jesus', 'return', 'bible', 'statistics'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SECOND COMING STATS",
    en_title: "Second Coming Stats",
    en_content: "One out of every 24 verses in the New Testament refers to the Second Coming of Christ.",
    es_title: "Estadísticas de la Segunda Venida",
    es_content: "Uno de cada 24 versículos en el Nuevo Testamento se refiere a la Segunda Venida de Cristo.",
    fr_title: "Statistiques du Second Avènement",
    fr_content: "Un verset sur 24 dans le Nouveau Testament fait référence au Second Avènement du Christ.",
    hi_title: "द्वितीय आगमन के आंकड़े",
    hi_content: "नए नियम की हर 24 आयतों में से एक आयत मसीह के द्वितीय आगमन का संदर्भ देती है।",
    zh_title: "Di Er Ci Jiang Lin Tong Ji",
    zh_content: "Xin Yue Quan Shu Zhong Mei 24 Jie Jing Wen Jiu You Yi Jie Ti Dao Ji Du De Di Er Ci Jiang Lin."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SECOND COMING STATS" AND c.name = "content.SECOND COMING STATS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SECOND COMING STATS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.SECOND COMING STATS"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >SECOND COMING STATS" }]->(child);
```
