---
name: "thought.GOD IS FUTURE"
alias: "Thought: God Is Future"
type: THOUGHT
en_content: "God is your Future."
parent: "topic.SPIRITUALITY"
tags:
- future
- god
- spirituality
- eternity
- presence
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD IS FUTURE",
    alias: "Thought: God Is Future",
    parent: "topic.SPIRITUALITY",
    tags: ['future', 'god', 'spirituality', 'eternity', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD IS FUTURE",
    en_title: "God Is Future",
    en_content: "God is your Future.",
    es_title: "Dios Es el Futuro",
    es_content: "Dios es tu Futuro.",
    fr_title: "Dieu Est l'Avenir",
    fr_content: "Dieu est votre Avenir.",
    hi_title: "परमेश्वर भविष्य है",
    hi_content: "परमेश्वर आपका भविष्य है।",
    zh_title: "Shàngdì Shì Wèilái",
    zh_content: "Shàngdì shì nǐ de Wèilái."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD IS FUTURE" AND c.name = "content.GOD IS FUTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS FUTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.GOD IS FUTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >GOD IS FUTURE" }]->(child);
```
