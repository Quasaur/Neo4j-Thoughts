---
type: THOUGHT
name: "thought.SCENT OF GOD"
alias: "Thought: Scent Of God"
parent: "topic.SPIRITUALITY"
en_content: "It is Prayer, and Prayer alone, that places the Scent of God on us."
tags: ["prayer", "spirituality", "presence", "scent", "character"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2012a)
CREATE (t:THOUGHT {    name: "thought.SCENT OF GOD",
    alias: "Thought: Scent Of God",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'spirituality', 'presence', 'scent', 'character'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.SCENT OF GOD",
    ctype: "THOUGHT",
    en_title: "Scent Of God",
    en_content: "It is Prayer, and Prayer alone, that places the Scent of God on us.",
    es_title: "Aroma de Dios",
    es_content: "Es la Oración, y sólo la Oración, la que pone el Aroma de Dios sobre nosotros.",
    fr_title: "Parfum de Dieu",
    fr_content: "C'est la Prière, et la Prière seule, qui dépose le Parfum de Dieu sur nous.",
    hi_title: "परमेश्वर की सुगंध",
    hi_content: "यह प्रार्थना है, और केवल प्रार्थना ही है, जो हम पर परमेश्वर की सुगंध रखती है।",
    zh_title: "Shén de Xiāngqì",
    zh_content: "Zhǐ yǒu qídǎo, jǐnjǐn shì qídǎo, cáinéng shǐ wǒmen shēnshàng dàiyǒu Shén de xiāngqì."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SCENT OF GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->SCENT OF GOD"
RETURN t, parent;
```
