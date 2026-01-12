---
name: "thought.OMNIPOTENCE VS FREEWILL"
alias: "Thought: Omnipotence Vs Freewill"
type: THOUGHT
en_content: "Free Will exists only due to human ignorance of The Divine Omnipotence."
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- freewill
- omnipotence
- ignorance
- divinity
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012a)
CREATE (t:THOUGHT {
    name: "thought.OMNIPOTENCE VS FREEWILL",
    alias: "Thought: Omnipotence Vs Freewill",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'freewill', 'omnipotence', 'ignorance', 'divinity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OMNIPOTENCE VS FREEWILL",
    en_title: "Omnipotence Vs Freewill",
    en_content: "Free Will exists only due to human ignorance of The Divine Omnipotence.",
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
WHERE t.name = "thought.OMNIPOTENCE VS FREEWILL" AND c.name = "content.OMNIPOTENCE VS FREEWILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OMNIPOTENCE VS FREEWILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.OMNIPOTENCE VS FREEWILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >OMNIPOTENCE VS FREEWILL" }]->(child);
```
