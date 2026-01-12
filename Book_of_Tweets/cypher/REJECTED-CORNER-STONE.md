---
name: "thought.REJECTED CORNER STONE"
alias: "Thought: Rejected Corner Stone"
type: THOUGHT
en_content: "The Stone that the builders rejected...(smile)!"
parent: "topic.RELIGION"
tags:
- stone
- builders
- rejection
- jesus
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.REJECTED CORNER STONE",
    alias: "Thought: Rejected Corner Stone",
    parent: "topic.RELIGION",
    tags: ['stone', 'builders', 'rejection', 'jesus'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.REJECTED CORNER STONE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REJECTED CORNER STONE" AND c.name = "content.REJECTED CORNER STONE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REJECTED CORNER STONE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.REJECTED CORNER STONE"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >REJECTED CORNER STONE" }]->(child);
```
