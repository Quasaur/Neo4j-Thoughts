---
name: "thought.SAUL WASTING LIFE"
alias: "Thought: Saul Wasting Life"
type: THOUGHT
en_content: "Saul wasted a large portion of his life trying to kill David while neglecting weightier matters...like his relationship with God."
parent: "topic.RELIGION"
tags:
- saul
- david
- relationship
- god
- waste
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.SAUL WASTING LIFE",
    alias: "Thought: Saul Wasting Life",
    parent: "topic.RELIGION",
    tags: ['saul', 'david', 'relationship', 'god', 'waste'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SAUL WASTING LIFE",
    en_title: "Saul Wasting Life",
    en_content: "Saul wasted a large portion of his life trying to kill David while neglecting weightier matters...like his relationship with God.",
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
WHERE t.name = "thought.SAUL WASTING LIFE" AND c.name = "content.SAUL WASTING LIFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SAUL WASTING LIFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.SAUL WASTING LIFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >SAUL WASTING LIFE" }]->(child);
```
