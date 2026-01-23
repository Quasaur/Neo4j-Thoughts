---
name: "thought.DEFINE TRUST"
alias: "Thought: Define Trust"
type: THOUGHT
en_content: "TRUST is born of both confidence and ignorance."
parent: "topic.FAITH"
tags:
- trust
- confidence
- ignorance
- faith
- philosophy
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE TRUST",
    alias: "Thought: Define Trust",
    parent: "topic.FAITH",
    tags: ['trust', 'confidence', 'ignorance', 'faith', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE TRUST",
    en_title: "Define Trust",
    en_content: "TRUST is born of both confidence and ignorance.",
    es_title: "Definir la Confianza",
    es_content: "La CONFIANZA nace tanto de la certeza como de la ignorancia.",
    fr_title: "Définir la Confiance",
    fr_content: "La CONFIANCE naît à la fois de la certitude et de l'ignorance.",
    hi_title: "भरोसे की परिभाषा",
    hi_content: "भरोसा विश्वास और अज्ञानता दोनों से जन्म लेता है।",
    zh_title: "Dìng Yì Xìn Rèn",
    zh_content: "Xìn Rèn jì shēng yú xìn xīn, yě shēng yú wú zhī."
});

MATCH (t:THOUGHT {name: "thought.DEFINE TRUST"})
MATCH (c:CONTENT {name: "content.DEFINE TRUST"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE TRUST" }]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.DEFINE TRUST"})
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >DEFINE TRUST" }]->(child);
```
