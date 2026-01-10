---
name: "thought.POWER OF JESUS"
alias: "Thought: Power Of Jesus"
type: THOUGHT
en_content: "I have NEVER met anyone more powerful that Jesus...and I never will."
parent: "topic.THE GODHEAD"
tags:
- jesus
- power
- divinity
- majesty
- lordship
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2010a)
CREATE (t:THOUGHT {
    name: "thought.POWER OF JESUS",
    alias: "Thought: Power Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'power', 'divinity', 'majesty', 'lordship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.POWER OF JESUS",
    en_title: "Power Of Jesus",
    en_content: "I have NEVER met anyone more powerful that Jesus...and I never will.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.POWER OF JESUS" AND c.name = "content.POWER OF JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER OF JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.POWER OF JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >POWER OF JESUS" }]->(child);
```
