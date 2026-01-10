---
name: "thought.TRANSFORMING POWER LOVE"
alias: "Thought: Transforming Power Love"
type: THOUGHT
en_content: "God's Love is frighteningly powerful: turning dirt into flesh, flesh into spirit, sin into righteousness and death into life."
parent: "topic.THE GODHEAD"
tags:
- love
- transformation
- power
- god
- life
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.TRANSFORMING POWER LOVE",
    alias: "Thought: Transforming Power Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'transformation', 'power', 'god', 'life'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.TRANSFORMING POWER LOVE",
    en_title: "Transforming Power Love",
    en_content: "God's Love is frighteningly powerful: turning dirt into flesh, flesh into spirit, sin into righteousness and death into life.",
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
WHERE t.name = "thought.TRANSFORMING POWER LOVE" AND c.name = "content.TRANSFORMING POWER LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRANSFORMING POWER LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.TRANSFORMING POWER LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >TRANSFORMING POWER LOVE" }]->(child);
```
