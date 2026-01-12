---
name: "thought.LEAVING GOD OUT"
alias: "Thought: Leaving God Out"
type: THOUGHT
en_content: "We've left God out."
parent: "topic.RELIGION"
tags:
- secularism
- society
- religion
- exclusion
- faith
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.LEAVING GOD OUT",
    alias: "Thought: Leaving God Out",
    parent: "topic.RELIGION",
    tags: ['secularism', 'society', 'religion', 'exclusion', 'faith'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LEAVING GOD OUT",
    en_title: "Leaving God Out",
    en_content: "We've left God out.",
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
WHERE t.name = "thought.LEAVING GOD OUT" AND c.name = "content.LEAVING GOD OUT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LEAVING GOD OUT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.LEAVING GOD OUT"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >LEAVING GOD OUT" }]->(child);
```
