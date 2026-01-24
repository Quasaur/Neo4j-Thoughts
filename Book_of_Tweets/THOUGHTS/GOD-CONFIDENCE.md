---
name: "thought.GOD CONFIDENCE"
alias: "Thought: God Confidence"
type: THOUGHT
en_content: "God-confidence is better than self-confidence."
parent: "topic.FAITH"
tags:
- faith
- confidence
- self
- god
- truth
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.GOD CONFIDENCE",
    alias: "Thought: God Confidence",
    parent: "topic.FAITH",
    tags: ['faith', 'confidence', 'self', 'god', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GOD CONFIDENCE",
    en_title: "God Confidence",
    en_content: "God-confidence is better than self-confidence.",
    es_title: "Confianza en Dios",
    es_content: "La confianza en Dios es mejor que la confianza en uno mismo.",
    fr_title: "Confiance en Dieu",
    fr_content: "La confiance en Dieu est meilleure que la confiance en soi.",
    hi_title: "ईश्वर में विश्वास",
    hi_content: "ईश्वर में विश्वास आत्मविश्वास से बेहतर है।",
    zh_title: "Duì Shàngdì de xìnxīn",
    zh_content: "Duì Shàngdì de xìnxīn bǐ zìxìn gèng hǎo."
});

MATCH (t:THOUGHT {name: "thought.GOD CONFIDENCE"})
MATCH (c:CONTENT {name: "content.GOD CONFIDENCE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD CONFIDENCE" }]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.GOD CONFIDENCE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH->GOD CONFIDENCE" }]->(child);
```
