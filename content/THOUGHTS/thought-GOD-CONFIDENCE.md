---
type: THOUGHT
name: "thought.GOD CONFIDENCE"
alias: "Thought: God Confidence"
parent: "topic.FAITH"
en_content: "God-confidence is better than self-confidence."
tags: ["faith", "confidence", "self", "god", "truth"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD CONFIDENCE",
    alias: "Thought: God Confidence",
    parent: "topic.FAITH",
    tags: ['faith', 'confidence', 'self', 'god', 'truth'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GOD CONFIDENCE",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD CONFIDENCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GOD CONFIDENCE"
RETURN t, parent;
```
