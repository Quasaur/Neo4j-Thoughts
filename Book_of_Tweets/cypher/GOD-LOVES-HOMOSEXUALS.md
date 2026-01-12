---
name: "thought.GOD LOVES HOMOSEXUALS"
alias: "Thought: God Loves Homosexuals"
type: THOUGHT
en_content: "God loves homosexuals."
parent: "topic.THE GODHEAD"
tags:
- love
- character
- god
- humanity
- inclusion
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD LOVES HOMOSEXUALS",
    alias: "Thought: God Loves Homosexuals",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'character', 'god', 'humanity', 'inclusion'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD LOVES HOMOSEXUALS",
    en_title: "God Loves Homosexuals",
    en_content: "God loves homosexuals.",
    es_title: "Dios Ama a los Homosexuales",
    es_content: "Dios ama a los homosexuales.",
    fr_title: "Dieu Aime les Homosexuels",
    fr_content: "Dieu aime les homosexuels.",
    hi_title: "ईश्वर समलैंगिकों से प्रेम करता है",
    hi_content: "ईश्वर समलैंगिकों से प्रेम करता है।",
    zh_title: "Shàngdì ài tóngxìngliàn zhě",
    zh_content: "Shàngdì ài tóngxìngliàn zhě."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD LOVES HOMOSEXUALS" AND c.name = "content.GOD LOVES HOMOSEXUALS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD LOVES HOMOSEXUALS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD LOVES HOMOSEXUALS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD LOVES HOMOSEXUALS" }]->(child);
```
