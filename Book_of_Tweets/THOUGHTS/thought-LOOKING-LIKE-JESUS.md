---
type: THOUGHT
name: "thought.LOOKING LIKE JESUS"
alias: "Thought: Looking Like Jesus"
parent: "topic.THE GODHEAD"
en_content: "Jesus is what you look like to God!"
tags: ["jesus", "identity", "god", "appearance", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jul-2012a)
CREATE (t:THOUGHT {    name: "thought.LOOKING LIKE JESUS",
    alias: "Thought: Looking Like Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'identity', 'god', 'appearance', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.LOOKING LIKE JESUS",
    ctype: "THOUGHT",
    en_title: "Looking Like Jesus",
    en_content: "Jesus is what you look like to God!",
    es_title: "Pareciéndose a Jesús",
    es_content: "¡Jesús es como tú te ves ante Dios!",
    fr_title: "Ressembler à Jésus",
    fr_content: "Jésus est ce à quoi tu ressembles aux yeux de Dieu !",
    hi_title: "यीशु के समान दिखना",
    hi_content: "यीशु ही वह है जैसा तुम परमेश्वर को दिखते हो!",
    zh_title: "Kàn Qǐlái Xiàng Yēsū",
    zh_content: "Yēsū jiù shì nǐ zài Shàngdì miànqián de yàngzi!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOOKING LIKE JESUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->LOOKING LIKE JESUS"
RETURN t, parent;
```
