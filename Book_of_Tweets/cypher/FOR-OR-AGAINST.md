---
name: "thought.FOR OR AGAINST"
alias: "Thought: For Or Against"
type: THOUGHT
en_content: "\"Whoever is not for Me is against Me.\" -- Jesus Christ"
parent: "topic.THE GODHEAD"
tags:
- jesus
- choice
- allegiance
- christ
- judgment
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.FOR OR AGAINST",
    alias: "Thought: For Or Against",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'choice', 'allegiance', 'christ', 'judgment'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.FOR OR AGAINST",
    en_title: "For Or Against",
    en_content: "\"Whoever is not for Me is against Me.\" -- Jesus Christ",
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
WHERE t.name = "thought.FOR OR AGAINST" AND c.name = "content.FOR OR AGAINST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FOR OR AGAINST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.FOR OR AGAINST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >FOR OR AGAINST" }]->(child);
```
