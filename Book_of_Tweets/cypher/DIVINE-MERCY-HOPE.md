---
name: "thought.DIVINE MERCY HOPE"
alias: "Thought: Divine Mercy Hope"
type: THOUGHT
en_content: "Apart from Divine Mercy there is no hope for the human race."
parent: "topic.GRACE"
tags:
- mercy
- hope
- grace
- humanity
- salvation
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Dec-2010)
CREATE (t:THOUGHT {
    name: "thought.DIVINE MERCY HOPE",
    alias: "Thought: Divine Mercy Hope",
    parent: "topic.GRACE",
    tags: ['mercy', 'hope', 'grace', 'humanity', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIVINE MERCY HOPE",
    en_title: "Divine Mercy Hope",
    en_content: "Apart from Divine Mercy there is no hope for the human race.",
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
WHERE t.name = "thought.DIVINE MERCY HOPE" AND c.name = "content.DIVINE MERCY HOPE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DIVINE MERCY HOPE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DIVINE MERCY HOPE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >DIVINE MERCY HOPE" }]->(child);
```
