---
type: THOUGHT
name: "thought.NOTHING WITHOUT GOD"
alias: "Thought: Nothing Without God"
parent: "topic.HUMANITY"
en_content: "You are NOTHING without God; You are EVERYTHING to God."
tags: ["humanity", "god", "value", "identity", "dependence"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Dec-2011)
CREATE (t:THOUGHT {    name: "thought.NOTHING WITHOUT GOD",
    alias: "Thought: Nothing Without God",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'god', 'value', 'identity', 'dependence'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.NOTHING WITHOUT GOD",
    ctype: "THOUGHT",
    en_title: "Nothing Without God",
    en_content: "You are NOTHING without God; You are EVERYTHING to God.",
    es_title: "Nada Sin Dios",
    es_content: "No eres NADA sin Dios; Eres TODO para Dios.",
    fr_title: "Rien Sans Dieu",
    fr_content: "Tu n'es RIEN sans Dieu ; Tu es TOUT pour Dieu.",
    hi_title: "परमेश्वर के बिना कुछ नहीं",
    hi_content: "आप परमेश्वर के बिना कुछ भी नहीं हैं; आप परमेश्वर के लिए सब कुछ हैं।",
    zh_title: "Méi yǒu Shàngdì jiù shì wú",
    zh_content: "Méi yǒu Shàngdì, nǐ shénme dōu bù shì; duì Shàngdì lái shuō, nǐ jiùshì yīqiè."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOTHING WITHOUT GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->NOTHING WITHOUT GOD"
RETURN t, parent;
```
