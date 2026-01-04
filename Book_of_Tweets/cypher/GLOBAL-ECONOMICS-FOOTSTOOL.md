---
name: "thought.GLOBAL ECONOMICS FOOTSTOOL"
alias: "Thought: Global Economics Footstool"
type: THOUGHT
en_content: "Global economics: God is making Christ's enemies His Footstool."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- economics
- prophecy
- jesus
- victory
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL ECONOMICS FOOTSTOOL",
    alias: "Thought: Global Economics Footstool",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'economics', 'prophecy', 'jesus', 'victory'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLOBAL ECONOMICS FOOTSTOOL",
    en_title: "Global Economics Footstool",
    en_content: "Global economics: God is making Christ's enemies His Footstool.",
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
WHERE t.name = "thought.GLOBAL ECONOMICS FOOTSTOOL" AND c.name = "content.GLOBAL ECONOMICS FOOTSTOOL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLOBAL ECONOMICS FOOTSTOOL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.GLOBAL ECONOMICS FOOTSTOOL"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >GLOBAL ECONOMICS FOOTSTOOL" }]->(child);
```
