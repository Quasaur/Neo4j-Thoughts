---
name: "thought.LOOKING LIKE JESUS"
alias: "Thought: Looking Like Jesus"
type: THOUGHT
en_content: "Jesus is what you look like to God!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- identity
- god
- appearance
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jul-2012a)
CREATE (t:THOUGHT {
    name: "thought.LOOKING LIKE JESUS",
    alias: "Thought: Looking Like Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'identity', 'god', 'appearance', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.LOOKING LIKE JESUS",
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

MATCH (t:THOUGHT {name: "thought.LOOKING LIKE JESUS"})
MATCH (c:CONTENT {name: "content.LOOKING LIKE JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOOKING LIKE JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.LOOKING LIKE JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >LOOKING LIKE JESUS" }]->(child);
```
