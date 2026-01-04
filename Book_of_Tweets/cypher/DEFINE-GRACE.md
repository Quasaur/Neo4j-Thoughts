---
name: "thought.DEFINE GRACE"
alias: "Thought: Define Grace"
type: THOUGHT
en_content: "GRACE is God saying \"I like you! I'm gonna cut you a break!\""
parent: "topic.GRACE"
tags:
- grace
- mercy
- love
- salvation
- favor
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE GRACE",
    alias: "Thought: Define Grace",
    parent: "topic.GRACE",
    tags: ['grace', 'mercy', 'love', 'salvation', 'favor'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE GRACE",
    en_title: "Define Grace",
    en_content: "GRACE is God saying \"I like you! I'm gonna cut you a break!\"",
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
WHERE t.name = "thought.DEFINE GRACE" AND c.name = "content.DEFINE GRACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE GRACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DEFINE GRACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >DEFINE GRACE" }]->(child);
```
