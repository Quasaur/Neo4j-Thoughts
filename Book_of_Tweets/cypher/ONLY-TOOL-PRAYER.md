---
name: "thought.ONLY TOOL PRAYER"
alias: "Thought: Only Tool Prayer"
type: THOUGHT
en_content: "Prayer is not our best tool; it's our ONLY tool."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- spirituality
- dependence
- faith
- connection
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-May-2011a)
CREATE (t:THOUGHT {
    name: "thought.ONLY TOOL PRAYER",
    alias: "Thought: Only Tool Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'spirituality', 'dependence', 'faith', 'connection'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ONLY TOOL PRAYER",
    en_title: "Only Tool Prayer",
    en_content: "Prayer is not our best tool; it's our ONLY tool.",
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
WHERE t.name = "thought.ONLY TOOL PRAYER" AND c.name = "content.ONLY TOOL PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ONLY TOOL PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.ONLY TOOL PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >ONLY TOOL PRAYER" }]->(child);
```
