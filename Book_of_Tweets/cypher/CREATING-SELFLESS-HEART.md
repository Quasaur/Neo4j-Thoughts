---
name: "thought.CREATING SELFLESS HEART"
alias: "Thought: Creating Selfless Heart"
type: THOUGHT
en_content: "Only God can create a selfless heart from a pile of dust."
parent: "topic.THE GODHEAD"
tags:
- heart
- transformation
- creation
- selfless
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.CREATING SELFLESS HEART",
    alias: "Thought: Creating Selfless Heart",
    parent: "topic.THE GODHEAD",
    tags: ['heart', 'transformation', 'creation', 'selfless', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CREATING SELFLESS HEART",
    en_title: "Creating Selfless Heart",
    en_content: "Only God can create a selfless heart from a pile of dust.",
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
WHERE t.name = "thought.CREATING SELFLESS HEART" AND c.name = "content.CREATING SELFLESS HEART"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CREATING SELFLESS HEART" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CREATING SELFLESS HEART"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CREATING SELFLESS HEART" }]->(child);
```
