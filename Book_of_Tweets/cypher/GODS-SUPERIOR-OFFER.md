---
name: "thought.GODS SUPERIOR OFFER"
alias: "Thought: Gods Superior Offer"
type: THOUGHT
en_content: "God has FAR MORE to offer me than I have to offer Him."
parent: "topic.THE GODHEAD"
tags:
- god
- offer
- value
- grace
- majesty
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.GODS SUPERIOR OFFER",
    alias: "Thought: Gods Superior Offer",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'offer', 'value', 'grace', 'majesty'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS SUPERIOR OFFER",
    en_title: "Gods Superior Offer",
    en_content: "God has FAR MORE to offer me than I have to offer Him.",
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
WHERE t.name = "thought.GODS SUPERIOR OFFER" AND c.name = "content.GODS SUPERIOR OFFER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS SUPERIOR OFFER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS SUPERIOR OFFER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS SUPERIOR OFFER" }]->(child);
```
