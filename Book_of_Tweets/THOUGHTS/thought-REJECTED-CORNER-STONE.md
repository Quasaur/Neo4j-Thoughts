---
type: THOUGHT
name: "thought.REJECTED CORNER STONE"
alias: "Thought: Rejected Corner Stone"
parent: "topic.RELIGION"
en_content: "The Stone that the builders rejected...(smile)!"
tags: ["stone", "builders", "rejection", "jesus"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Dec-2013)
CREATE (t:THOUGHT {    name: "thought.REJECTED CORNER STONE",
    alias: "Thought: Rejected Corner Stone",
    parent: "topic.RELIGION",
    tags: ['stone', 'builders', 'rejection', 'jesus'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.REJECTED CORNER STONE",
    ctype: "THOUGHT",
    en_title: "Rejected Corner Stone",
    en_content: "The Stone that the builders rejected...(smile)!",
    es_title: "La Piedra Angular Rechazada",
    es_content: "La Piedra que desecharon los edificadores...(¡sonrisa)!",
    fr_title: "La Pierre Angulaire Rejetée",
    fr_content: "La Pierre que les bâtisseurs ont rejetée...(sourire)!",
    hi_title: "अस्वीकृत आधारशिला",
    hi_content: "जिस पत्थर को राजमिस्त्रियों ने निकम्मा ठहराया था...(मुस्कान)!",
    zh_title: "Bei Qi Jue De Fang Jiao Shi",
    zh_content: "Jiang Gong Ren Suo Qi De Shi Tou...(wei xiao)!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.REJECTED CORNER STONE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->REJECTED CORNER STONE"
RETURN t, parent;
```
