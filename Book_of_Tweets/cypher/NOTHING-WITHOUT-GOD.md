---
name: "thought.NOTHING WITHOUT GOD"
alias: "Thought: Nothing Without God"
type: THOUGHT
en_content: "You are NOTHING without God; You are EVERYTHING to God."
parent: "topic.HUMANITY"
tags:
- humanity
- god
- value
- identity
- dependence
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.NOTHING WITHOUT GOD",
    alias: "Thought: Nothing Without God",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'god', 'value', 'identity', 'dependence'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOTHING WITHOUT GOD",
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

MATCH (t:THOUGHT {name: "thought.NOTHING WITHOUT GOD"})
MATCH (c:CONTENT {name: "content.NOTHING WITHOUT GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING WITHOUT GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.NOTHING WITHOUT GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NOTHING WITHOUT GOD" }]->(child);
```
