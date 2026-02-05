---
name: thought.DEFINE TRUST
alias: "Thought: Define Trust"
type: THOUGHT
en_content: "TRUST is born of confidence in the midst ignorance."
parent: topic.FAITH
tags:
  - trust
  - confidence
  - ignorance
  - faith
  - philosophy
level: 4
neo4j: false
ptopic: "[[topic-FAITH]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE TRUST",
    alias: "Thought: Define Trust",
    parent: "topic.FAITH",
    tags: ['trust', 'confidence', 'ignorance', 'faith', 'philosophy'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE TRUST",
    en_title: "Define Trust",
    en_content: "TRUST is born of confidence in the midst of ignorance.",
    es_title: "Definición de confianza",
    es_content: "a confianza nace de la seguridad en medio de la incertidumbre.",
    fr_title: "Définir la confiance",
    fr_content: "La confiance naît de la certitude au milieu de l'incertitude.",
    hi_title: "विश्वास को परिभाषित करें",
    hi_content: "विश्वास अज्ञानता के बीच भरोसे से पैदा होता है।",
    zh_title: "Dìngyì xìnrèn",
    zh_content: "xìnrèn yuán yú zài wèizhī zhōng chǎnshēng de xìnxīn."
});

MATCH (t:THOUGHT {name: "thought.DEFINE TRUST"})
MATCH (c:CONTENT {name: "content.DEFINE TRUST"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.DEFINE TRUST" }]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.DEFINE TRUST"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.FAITH->DEFINE TRUST" }]->(child);
```
