---
name: "thought.LEAVING GOD OUT"
alias: "Thought: Leaving God Out"
type: THOUGHT
en_content: "We've left God out."
parent: "topic.RELIGION"
tags:
- secularism
- society
- religion
- exclusion
- faith
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.LEAVING GOD OUT",
    alias: "Thought: Leaving God Out",
    parent: "topic.RELIGION",
    tags: ['secularism', 'society', 'religion', 'exclusion', 'faith'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LEAVING GOD OUT",
    en_title: "Leaving God Out",
    en_content: "We've left God out.",
    es_title: "Dejando a Dios Fuera",
    es_content: "Hemos dejado a Dios fuera.",
    fr_title: "Laisser Dieu de Côté",
    fr_content: "Nous avons laissé Dieu de côté.",
    hi_title: "परमेश्वर को छोड़ना",
    hi_content: "हमने परमेश्वर को छोड़ दिया है।",
    zh_title: "Ba Shen Paichu Zaiwei",
    zh_content: "Women ba Shen paichu zaiwai le."
});

MATCH (t:THOUGHT {name: "thought.LEAVING GOD OUT"})
MATCH (c:CONTENT {name: "content.LEAVING GOD OUT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LEAVING GOD OUT" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.LEAVING GOD OUT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION->LEAVING GOD OUT" }]->(child);
```
