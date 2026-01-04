---
name: "thought.DEFINE TRUST"
alias: "Thought: Define Trust"
type: THOUGHT
en_content: "TRUST is born of both confidence and ignorance."
parent: "topic.FAITH"
tags:
- trust
- confidence
- ignorance
- faith
- philosophy
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE TRUST",
    alias: "Thought: Define Trust",
    parent: "topic.FAITH",
    tags: ['trust', 'confidence', 'ignorance', 'faith', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE TRUST",
    en_title: "Define Trust",
    en_content: "TRUST is born of both confidence and ignorance.",
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
WHERE t.name = "thought.DEFINE TRUST" AND c.name = "content.DEFINE TRUST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE TRUST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DEFINE TRUST"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >DEFINE TRUST" }]->(child);
```
