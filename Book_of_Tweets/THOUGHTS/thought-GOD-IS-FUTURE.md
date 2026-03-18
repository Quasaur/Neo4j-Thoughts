---
type: THOUGHT
name: "thought.GOD IS FUTURE"
alias: "Thought: God Is Future"
parent: "topic.SPIRITUALITY"
en_content: "God is your Future."
tags: ["future", "god", "spirituality", "eternity", "presence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Jun-2012)
CREATE (t:THOUGHT {    name: "thought.GOD IS FUTURE",
    alias: "Thought: God Is Future",
    parent: "topic.SPIRITUALITY",
    tags: ['future', 'god', 'spirituality', 'eternity', 'presence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.GOD IS FUTURE",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD IS FUTURE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->GOD IS FUTURE"
RETURN t, parent;
```
