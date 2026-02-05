---
name: "thought.FUTILE REBELLION"
alias: "Thought: Futile Rebellion"
type: THOUGHT
en_content: "Rebellion against God is futile!"
parent: "topic.HUMANITY"
tags:
- rebellion
- futility
- humanity
- god
- sovereignty
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.FUTILE REBELLION",
    alias: "Thought: Futile Rebellion",
    parent: "topic.HUMANITY",
    tags: ['rebellion', 'futility', 'humanity', 'god', 'sovereignty'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FUTILE REBELLION",
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

MATCH (t:THOUGHT {name: "thought.FUTILE REBELLION"})
MATCH (c:CONTENT {name: "content.FUTILE REBELLION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FUTILE REBELLION" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.FUTILE REBELLION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->FUTILE REBELLION" }]->(child);
```
