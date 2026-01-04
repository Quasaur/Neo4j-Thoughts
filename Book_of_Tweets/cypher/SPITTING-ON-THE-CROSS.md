---
name: "thought.SPITTING ON THE CROSS"
alias: "Thought: Spitting On The Cross"
type: THOUGHT
parent: "topic.GRACE"
tags:
- forgiveness
- cross
- atonement
- grace
- pride
level: 3
neo4j: true
insert: true
---
# Spitting On The Cross

> [!Thought-en]
> Jesus has been punished for the sin you have committed against me; if I don't forgive you I have spit on The Cross of Christ.

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.SPITTING ON THE CROSS",
    alias: "Thought: Spitting On The Cross",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'cross', 'atonement', 'grace', 'pride'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SPITTING ON THE CROSS",
    en_title: "Spitting On The Cross",
    en_content: "Jesus has been punished for the sin you have committed against me; if I don't forgive you I have spit on The Cross of Christ.",
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
WHERE t.name = "thought.SPITTING ON THE CROSS" AND c.name = "content.SPITTING ON THE CROSS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPITTING ON THE CROSS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SPITTING ON THE CROSS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >SPITTING ON THE CROSS" }]->(child);
```