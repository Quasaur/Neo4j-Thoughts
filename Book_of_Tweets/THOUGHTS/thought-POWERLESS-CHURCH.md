---
type: THOUGHT
name: "thought.POWERLESS CHURCH"
alias: "Thought: Powerless Church"
parent: "topic.RELIGION"
en_content: "The church that is without power doesn't understand The Gospel (Romans 1:16)."
tags: ["church", "gospel", "power", "understanding", "religion"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jan-2012)
CREATE (t:THOUGHT {    name: "thought.POWERLESS CHURCH",
    alias: "Thought: Powerless Church",
    parent: "topic.RELIGION",
    tags: ['church', 'gospel', 'power', 'understanding', 'religion'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.POWERLESS CHURCH",
    ctype: "THOUGHT",
    en_title: "Powerless Church",
    en_content: "The church that is without power doesn't understand The Gospel (Romans 1:16).",
    es_title: "Iglesia Sin Poder",
    es_content: "La iglesia que está sin poder no entiende El Evangelio (Romanos 1:16).",
    fr_title: "Église Sans Pouvoir",
    fr_content: "L'église qui est sans pouvoir ne comprend pas L'Évangile (Romains 1:16).",
    hi_title: "शक्तिहीन कलीसिया",
    hi_content: "जो कलीसिया शक्ति के बिना है वह सुसमाचार को नहीं समझती (रोमियों 1:16)।",
    zh_title: "Wu Li De Jiao Hui",
    zh_content: "Mei You Neng Li De Jiao Hui Bu Ming Bai Fu Yin (Luo Ma Shu 1:16)."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.POWERLESS CHURCH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->POWERLESS CHURCH"
RETURN t, parent;
```
