---
name: "thought.ULTIMATE REALITY GOD"
alias: "Thought: Ultimate Reality God"
type: THOUGHT
en_content: "God is the Ultimate Reality. So if you're not interested in God, how real are you?"
parent: "topic.THE GODHEAD"
tags:
- god
- reality
- existence
- philosophy
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Mar-2013)
CREATE (t:THOUGHT {
    name: "thought.ULTIMATE REALITY GOD",
    alias: "Thought: Ultimate Reality God",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'reality', 'existence', 'philosophy', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ULTIMATE REALITY GOD",
    en_title: "Ultimate Reality God",
    en_content: "God is the Ultimate Reality. So if you're not interested in God, how real are you?",
    es_title: "Dios la Realidad Última",
    es_content: "Dios es la Realidad Última. Entonces, si no estás interesado en Dios, ¿qué tan real eres?",
    fr_title: "Dieu la Réalité Ultime",
    fr_content: "Dieu est la Réalité Ultime. Alors si vous ne vous intéressez pas à Dieu, à quel point êtes-vous réel ?",
    hi_title: "परम सत्ता परमेश्वर",
    hi_content: "परमेश्वर ही परम सत्ता है। तो यदि आप परमेश्वर में रुचि नहीं रखते, तो आप कितने वास्तविक हैं?",
    zh_title: "Zhìgāo Shíxiàng Shàngdì",
    zh_content: "Shàngdì shì Zhìgāo Shíxiàng. Suǒyǐ rúguǒ nǐ duì Shàngdì méiyǒu xìngqù, nǐ yǒu duō zhēnshí?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ULTIMATE REALITY GOD" AND c.name = "content.ULTIMATE REALITY GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ULTIMATE REALITY GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ULTIMATE REALITY GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ULTIMATE REALITY GOD" }]->(child);
```
