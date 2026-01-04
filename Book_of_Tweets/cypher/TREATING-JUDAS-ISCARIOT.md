---
name: "thought.TREATING JUDAS ISCARIOT"
alias: "Thought: Treating Judas Iscariot"
type: THOUGHT
en_content: "Do you think Jesus treated Judas Iscariot differently from the rest of the disciples?"
parent: "topic.THE GODHEAD"
tags:
- judas
- jesus
- treatment
- disciples
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TREATING JUDAS ISCARIOT",
    alias: "Thought: Treating Judas Iscariot",
    parent: "topic.THE GODHEAD",
    tags: ['judas', 'jesus', 'treatment', 'disciples'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.TREATING JUDAS ISCARIOT",
    en_title: "Treating Judas Iscariot",
    en_content: "Do you think Jesus treated Judas Iscariot differently from the rest of the disciples?",
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
WHERE t.name = "thought.TREATING JUDAS ISCARIOT" AND c.name = "content.TREATING JUDAS ISCARIOT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TREATING JUDAS ISCARIOT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.TREATING JUDAS ISCARIOT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >TREATING JUDAS ISCARIOT" }]->(child);
```
