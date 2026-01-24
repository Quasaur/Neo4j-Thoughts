---
name: "thought.DEFINE HOPE"
alias: "Thought: Define Hope"
type: THOUGHT
en_content: HOPE = DESIRE + EXPECTATION
parent: topic.ATTITUDE
tags:
  - hope
  - desire
  - expectation
  - attitude
  - philosophy
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.DEFINE HOPE",
    alias: "Thought: Define Hope",
    parent: "topic.ATTITUDE",
    tags: ['hope', 'desire', 'expectation', 'attitude', 'philosophy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE HOPE",
    en_title: "Define Hope",
    en_content: "HOPE = DESIRE + EXPECTATION",
    es_title: "Definir Esperanza",
    es_content: "ESPERANZA = DESEO + EXPECTATIVA",
    fr_title: "Définir l'Espoir",
    fr_content: "ESPOIR = DÉSIR + ATTENTE",
    hi_title: "आशा को परिभाषित करें",
    hi_content: "आशा = इच्छा + अपेक्षा",
    zh_title: "Dìngyì xīwàng",
    zh_content: "Xīwàng = Kěwàng + Qīwàng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE HOPE" AND c.name = "content.DEFINE HOPE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE HOPE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.DEFINE HOPE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->DEFINE HOPE" }]->(child);
```
