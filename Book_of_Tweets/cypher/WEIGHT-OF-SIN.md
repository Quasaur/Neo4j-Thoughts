---
name: "thought.WEIGHT OF SIN"
alias: "Thought: Weight Of Sin"
type: THOUGHT
en_content: "Christ bore in His Body the sins of the 12 billion sinners who have lived since Adam."
parent: "topic.THE GODHEAD"
tags:
- atonement
- sin
- cross
- redemption
- jesus
level: 1
neo4j: true
insert: true
---
# Weight Of Sin

> [!Thought-en]
> Christ bore in His Body the sins of the 12 billion sinners who have lived since Adam.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011f)
CREATE (t:THOUGHT {
    name: "thought.WEIGHT OF SIN",
    alias: "Thought: Weight Of Sin",
    parent: "topic.THE GODHEAD",
    tags: ['atonement', 'sin', 'cross', 'redemption', 'jesus'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.WEIGHT OF SIN",
    en_title: "Weight Of Sin",
    en_content: "Christ bore in His Body the sins of the 12 billion sinners who have lived since Adam.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WEIGHT OF SIN" AND c.name = "content.WEIGHT OF SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WEIGHT OF SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.WEIGHT OF SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >WEIGHT OF SIN" }]->(child);
```