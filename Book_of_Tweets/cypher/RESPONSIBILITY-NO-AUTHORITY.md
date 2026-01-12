---
name: "thought.RESPONSIBILITY NO AUTHORITY"
alias: "Thought: Responsibility No Authority"
type: THOUGHT
en_content: "Responsibility without authority is like a boat without a motor."
parent: "topic.WISDOM"
tags:
- responsibility
- authority
- logic
- wisdom
- analogy
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.RESPONSIBILITY NO AUTHORITY",
    alias: "Thought: Responsibility No Authority",
    parent: "topic.WISDOM",
    tags: ['responsibility', 'authority', 'logic', 'wisdom', 'analogy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RESPONSIBILITY NO AUTHORITY",
    en_title: "Responsibility No Authority",
    en_content: "Responsibility without authority is like a boat without a motor.",
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
WHERE t.name = "thought.RESPONSIBILITY NO AUTHORITY" AND c.name = "content.RESPONSIBILITY NO AUTHORITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESPONSIBILITY NO AUTHORITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.RESPONSIBILITY NO AUTHORITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >RESPONSIBILITY NO AUTHORITY" }]->(child);
```
