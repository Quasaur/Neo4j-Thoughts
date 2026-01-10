---
name: "thought.NEAR COLLISION"
alias: "Thought: Near Collision"
type: THOUGHT
en_content: "An AA jet had a near collision with a United over AL...my sister was on the AA plane and could read the writing on the other plane."
parent: "topic.SPIRITUALITY"
tags:
- providence
- protection
- safety
- miracle
- spirituality
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.NEAR COLLISION",
    alias: "Thought: Near Collision",
    parent: "topic.SPIRITUALITY",
    tags: ['providence', 'protection', 'safety', 'miracle', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NEAR COLLISION",
    en_title: "Near Collision",
    en_content: "An AA jet had a near collision with a United over AL...my sister was on the AA plane and could read the writing on the other plane.",
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
WHERE t.name = "thought.NEAR COLLISION" AND c.name = "content.NEAR COLLISION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NEAR COLLISION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.NEAR COLLISION"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NEAR COLLISION" }]->(child);
```
