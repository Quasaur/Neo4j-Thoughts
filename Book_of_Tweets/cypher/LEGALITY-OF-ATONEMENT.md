---
name: "thought.LEGALITY OF ATONEMENT"
alias: "Thought: Legality Of Atonement"
type: THOUGHT
en_content: "IT'S NOT LEGAL for you AND Jesus to suffer for the same sin!"
parent: "topic.GRACE"
tags:
- atonement
- sin
- suffering
- legality
- jesus
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jul-2012b)
CREATE (t:THOUGHT {
    name: "thought.LEGALITY OF ATONEMENT",
    alias: "Thought: Legality Of Atonement",
    parent: "topic.GRACE",
    tags: ['atonement', 'sin', 'suffering', 'legality', 'jesus'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LEGALITY OF ATONEMENT",
    en_title: "Legality Of Atonement",
    en_content: "IT'S NOT LEGAL for you AND Jesus to suffer for the same sin!",
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
WHERE t.name = "thought.LEGALITY OF ATONEMENT" AND c.name = "content.LEGALITY OF ATONEMENT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LEGALITY OF ATONEMENT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LEGALITY OF ATONEMENT"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LEGALITY OF ATONEMENT" }]->(child);
```
