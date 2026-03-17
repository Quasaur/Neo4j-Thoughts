---
type: THOUGHT
name: "thought.SELF DENIAL"
alias: "Thought: Self-denial"
parent: "topic.ATTITUDE"
en_content: "If you can't say \"No\" to Self, you can't say \"Yes\" to God."
tags: ["self", "denial", "humility", "deprecation", "worship"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SELF DENIAL",
    alias: "Thought: Self-denial",
    parent: "topic.ATTITUDE",
    tags: ["self", "denial", "humility", "deprecation", "worship"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF DENIAL",
    ctype: "THOUGHT",
    en_title: "Self-denial",
    en_content: "If you can't say \\\"No\\\" to Self, you can't say \\\"Yes\\\" to God.",
    es_title: "ABNEGACIÓN",
    es_content: "Si no puedes decir \\\"No\\\" a ti mismo, no puedes decir \\\"Sí\\\" a Dios.",
    fr_title: "ABNÉGATION",
    fr_content: "Si vous ne pouvez pas dire « Non » à vous-même, vous ne pouvez pas dire « Oui » à Dieu.",
    hi_title: "आत्मोत्सर्ग",
    hi_content: "यदि आप स्वयं को \\\"नहीं\\\" नहीं कह सकते, तो आप भगवान को \\\"हाँ\\\" नहीं कह सकते।",
    zh_title: "zì wǒ fǒu dìng",
    zh_content: "Rúguǒ nǐ bùnéng duì zìjǐ shuō “bù”, nǐ jiù wúfǎ duì shàngdì shuō “shì”."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SELF DENIAL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->SELF DENIAL"
RETURN t, parent;
```
