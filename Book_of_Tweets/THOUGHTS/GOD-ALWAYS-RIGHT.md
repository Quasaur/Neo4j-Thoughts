---
name: "thought.GOD ALWAYS RIGHT"
alias: "Thought: God Always Right"
type: THOUGHT
en_content: "Only God is right about everything."
parent: "topic.THE GODHEAD"
tags:
- truth
- perfection
- god
- divinity
- wisdom
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Mar-2013a)
CREATE (t:THOUGHT {
    name: "thought.GOD ALWAYS RIGHT",
    alias: "Thought: God Always Right",
    parent: "topic.THE GODHEAD",
    tags: ['truth', 'perfection', 'god', 'divinity', 'wisdom'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD ALWAYS RIGHT",
    en_title: "God Always Right",
    en_content: "Only God is right about everything.",
    es_title: "Dios Siempre Tiene Razón",
    es_content: "Solo Dios tiene razón en todo.",
    fr_title: "Dieu a Toujours Raison",
    fr_content: "Seul Dieu a raison en tout.",
    hi_title: "ईश्वर हमेशा सही है",
    hi_content: "केवल ईश्वर ही हर बात में सही है।",
    zh_title: "Shàngdì Yǒngyuǎn Zhèngquè",
    zh_content: "Zhǐyǒu Shàngdì duì yīqiè dōu shì zhèngquè de."
});

MATCH (t:THOUGHT {name: "thought.GOD ALWAYS RIGHT"})
MATCH (c:CONTENT {name: "content.GOD ALWAYS RIGHT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD ALWAYS RIGHT" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD ALWAYS RIGHT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD ALWAYS RIGHT" }]->(child);
```
