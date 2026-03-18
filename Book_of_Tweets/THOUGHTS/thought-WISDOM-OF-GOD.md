---
type: THOUGHT
name: "thought.WISDOM OF GOD"
alias: "Thought: Wisdom Of God"
parent: "topic.THE GODHEAD"
en_content: "God is older, wiser, smarter, more intelligent and more powerful than you."
tags: ["god", "wisdom", "power", "majesty", "intelligence"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2011b)
CREATE (t:THOUGHT {    name: "thought.WISDOM OF GOD",
    alias: "Thought: Wisdom Of God",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'wisdom', 'power', 'majesty', 'intelligence'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.WISDOM OF GOD",
    ctype: "THOUGHT",
    en_title: "Wisdom Of God",
    en_content: "God is older, wiser, smarter, more intelligent and more powerful than you.",
    es_title: "Sabiduría de Dios",
    es_content: "Dios es más antiguo, más sabio, más inteligente y más poderoso que tú.",
    fr_title: "Sagesse de Dieu",
    fr_content: "Dieu est plus âgé, plus sage, plus intelligent et plus puissant que vous.",
    hi_title: "ईश्वर की बुद्धि",
    hi_content: "ईश्वर आपसे अधिक प्राचीन, अधिक बुद्धिमान, अधिक चतुर और अधिक शक्तिशाली है।",
    zh_title: "Shàngdì de Zhìhuì",
    zh_content: "Shàngdì bǐ nǐ gèng gǔlǎo, gèng míngzhì, gèng cōngmíng, gèng yǒu zhìhuì, gèng qiángdà."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WISDOM OF GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->WISDOM OF GOD"
RETURN t, parent;
```
