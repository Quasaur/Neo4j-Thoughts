---
type: THOUGHT
name: "thought.HEAVEN WITHIN"
alias: "Thought: Heaven Within"
parent: "topic.SPIRITUALITY"
en_content: "If Heaven isn't in us, then we can't go to Heaven."
tags: ["heaven", "spirituality", "eternity", "transformation", "presence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2010b)
CREATE (t:THOUGHT {    name: "thought.HEAVEN WITHIN",
    alias: "Thought: Heaven Within",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'spirituality', 'eternity', 'transformation', 'presence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.HEAVEN WITHIN",
    ctype: "THOUGHT",
    en_title: "Heaven Within",
    en_content: "If Heaven isn't in us, then we can't go to Heaven.",
    es_title: "El cielo interior",
    es_content: "Si el Cielo no está en nosotros, entonces no podemos ir al Cielo.",
    fr_title: "Le paradis intérieur",
    fr_content: "Si le Ciel n’est pas en nous, alors nous ne pouvons pas aller au Ciel.",
    hi_title: "भीतर स्वर्ग",
    hi_content: "यदि स्वर्ग हमारे अंदर नहीं है तो हम स्वर्ग में नहीं जा सकते।",
    zh_title: "tiān táng zhī nèi",
    zh_content: "rú guǒ tiān táng bù zài wǒ men lǐ miàn ， nà me wǒ men jiù bù néng qù tiān táng 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEAVEN WITHIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->HEAVEN WITHIN"
RETURN t, parent;
```
