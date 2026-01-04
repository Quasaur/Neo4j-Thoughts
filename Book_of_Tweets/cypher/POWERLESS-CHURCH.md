---
name: "thought.POWERLESS CHURCH"
alias: "Thought: Powerless Church"
type: THOUGHT
en_content: "The church that is without power doesn't understand The Gospel (Romans 1:16)."
parent: "topic.RELIGION"
tags:
- church
- gospel
- power
- understanding
- religion
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.POWERLESS CHURCH",
    alias: "Thought: Powerless Church",
    parent: "topic.RELIGION",
    tags: ['church', 'gospel', 'power', 'understanding', 'religion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.POWERLESS CHURCH",
    en_title: "Powerless Church",
    en_content: "The church that is without power doesn't understand The Gospel (Romans 1:16).",
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
WHERE t.name = "thought.POWERLESS CHURCH" AND c.name = "content.POWERLESS CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWERLESS CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.POWERLESS CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >POWERLESS CHURCH" }]->(child);
```
