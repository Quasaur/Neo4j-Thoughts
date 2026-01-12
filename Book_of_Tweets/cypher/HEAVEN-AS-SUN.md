---
name: "thought.HEAVEN AS SUN"
alias: "Thought: Heaven As Sun"
type: THOUGHT
en_content: "What is Heaven like? The center of the Sun!"
parent: "topic.SPIRITUALITY"
tags:
- heaven
- sun
- metaphor
- eternity
- light
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN AS SUN",
    alias: "Thought: Heaven As Sun",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'sun', 'metaphor', 'eternity', 'light'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN AS SUN",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HEAVEN AS SUN" AND c.name = "content.HEAVEN AS SUN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN AS SUN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEAVEN AS SUN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN AS SUN" }]->(child);
```
