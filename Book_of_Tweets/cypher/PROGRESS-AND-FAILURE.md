---
name: "thought.PROGRESS AND FAILURE"
alias: "Thought: Progress And Failure"
type: THOUGHT
en_content: "There's no progress without failure."
parent: "topic.WISDOM"
tags:
- wisdom
- progress
- failure
- growth
- truth
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.PROGRESS AND FAILURE",
    alias: "Thought: Progress And Failure",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'progress', 'failure', 'growth', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PROGRESS AND FAILURE",
    en_title: "Progress And Failure",
    en_content: "There's no progress without failure.",
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
WHERE t.name = "thought.PROGRESS AND FAILURE" AND c.name = "content.PROGRESS AND FAILURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PROGRESS AND FAILURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.PROGRESS AND FAILURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >PROGRESS AND FAILURE" }]->(child);
```
