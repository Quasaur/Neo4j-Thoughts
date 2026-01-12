---
name: "thought.SIMPLE RELATIONSHIP CHRIST"
alias: "Thought: Simple Relationship Christ"
type: THOUGHT
en_content: "A relationship with Christ is simple...I make it complicated."
parent: "topic.SPIRITUALITY"
tags:
- relationship
- christ
- simplicity
- spirituality
- struggle
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.SIMPLE RELATIONSHIP CHRIST",
    alias: "Thought: Simple Relationship Christ",
    parent: "topic.SPIRITUALITY",
    tags: ['relationship', 'christ', 'simplicity', 'spirituality', 'struggle'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SIMPLE RELATIONSHIP CHRIST",
    en_title: "Simple Relationship Christ",
    en_content: "A relationship with Christ is simple...I make it complicated.",
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
WHERE t.name = "thought.SIMPLE RELATIONSHIP CHRIST" AND c.name = "content.SIMPLE RELATIONSHIP CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIMPLE RELATIONSHIP CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SIMPLE RELATIONSHIP CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SIMPLE RELATIONSHIP CHRIST" }]->(child);
```
