---
type: THOUGHT
name: "thought.HEAVEN AS SUN"
alias: "Thought: Heaven As Sun"
parent: "topic.SPIRITUALITY"
en_content: "What is Heaven like? The center of the Sun!"
tags: ["heaven", "sun", "metaphor", "eternity", "light"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Dec-2012)
CREATE (t:THOUGHT {    name: "thought.HEAVEN AS SUN",
    alias: "Thought: Heaven As Sun",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'sun', 'metaphor', 'eternity', 'light'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.HEAVEN AS SUN",
    ctype: "THOUGHT",
    en_title: "Heaven As Sun",
    en_content: "What is Heaven like? The center of the Sun!",
    es_title: "El Cielo Como Sol",
    es_content: "¿Cómo es el Cielo? ¡El centro del Sol!",
    fr_title: "Le Ciel Comme Soleil",
    fr_content: "À quoi ressemble le Ciel ? Le centre du Soleil !",
    hi_title: "स्वर्ग सूर्य के समान",
    hi_content: "स्वर्ग कैसा है? सूर्य का केंद्र!",
    zh_title: "Tiān táng rú tài yáng",
    zh_content: "Tiān táng shì shén me yàng de? Tài yáng de zhōng xīn!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEAVEN AS SUN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->HEAVEN AS SUN"
RETURN t, parent;
```
