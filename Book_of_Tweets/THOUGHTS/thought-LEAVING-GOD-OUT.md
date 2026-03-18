---
type: THOUGHT
name: "thought.LEAVING GOD OUT"
alias: "Thought: Leaving God Out"
parent: "topic.RELIGION"
en_content: "We've left God out."
tags: ["secularism", "society", "religion", "exclusion", "faith"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2011)
CREATE (t:THOUGHT {    name: "thought.LEAVING GOD OUT",
    alias: "Thought: Leaving God Out",
    parent: "topic.RELIGION",
    tags: ['secularism', 'society', 'religion', 'exclusion', 'faith'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.LEAVING GOD OUT",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LEAVING GOD OUT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->LEAVING GOD OUT"
RETURN t, parent;
```
