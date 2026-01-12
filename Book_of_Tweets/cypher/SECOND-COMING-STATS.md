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
insert: true
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
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
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
