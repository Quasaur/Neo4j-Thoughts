---
type: THOUGHT
name: "thought.FUTILE REBELLION"
alias: "Thought: Futile Rebellion"
parent: "topic.HUMANITY"
en_content: "Rebellion against God is futile!"
tags: ["rebellion", "futility", "humanity", "god", "sovereignty"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jan-2012a)
CREATE (t:THOUGHT {    name: "thought.FUTILE REBELLION",
    alias: "Thought: Futile Rebellion",
    parent: "topic.HUMANITY",
    tags: ['rebellion', 'futility', 'humanity', 'god', 'sovereignty'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.FUTILE REBELLION",
    ctype: "THOUGHT",
    en_title: "Futile Rebellion",
    en_content: "Rebellion against God is futile!",
    es_title: "Rebelión Fútil",
    es_content: "¡La rebelión contra Dios es fútil!",
    fr_title: "Rébellion Futile",
    fr_content: "La rébellion contre Dieu est futile !",
    hi_title: "व्यर्थ विद्रोह",
    hi_content: "परमेश्वर के विरुद्ध विद्रोह व्यर्थ है!",
    zh_title: "Túláo de fǎnnù  tú láo de pàn nì",
    zh_content: "Fǎnnù Shàngdì shì túláo de!  pàn nì shàng dì shì tú láo de ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FUTILE REBELLION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->FUTILE REBELLION"
RETURN t, parent;
```
