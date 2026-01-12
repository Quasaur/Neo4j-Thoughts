---
name: "thought.RECONCILING IN CHRIST"
alias: "Thought: Reconciling In Christ"
type: THOUGHT
en_content: "1st Corinthians 15:24-28: God is reconciling and consolidating all things into Christ."
parent: "topic.THE GODHEAD"
tags:
- reconciliation
- christ
- consolidation
- bible
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.RECONCILING IN CHRIST",
    alias: "Thought: Reconciling In Christ",
    parent: "topic.THE GODHEAD",
    tags: ['reconciliation', 'christ', 'consolidation', 'bible', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RECONCILING IN CHRIST",
    en_title: "Reconciling In Christ",
    en_content: "1st Corinthians 15:24-28: God is reconciling and consolidating all things into Christ.",
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
WHERE t.name = "thought.RECONCILING IN CHRIST" AND c.name = "content.RECONCILING IN CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RECONCILING IN CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.RECONCILING IN CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >RECONCILING IN CHRIST" }]->(child);
```
