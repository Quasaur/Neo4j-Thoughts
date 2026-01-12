---
name: "thought.WISDOM OF GOD"
alias: "Thought: Wisdom Of God"
type: THOUGHT
en_content: "God is older, wiser, smarter, more intelligent and more powerful than you."
parent: "topic.THE GODHEAD"
tags:
- god
- wisdom
- power
- majesty
- intelligence
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.WISDOM OF GOD",
    alias: "Thought: Wisdom Of God",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'wisdom', 'power', 'majesty', 'intelligence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.WISDOM OF GOD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WISDOM OF GOD" AND c.name = "content.WISDOM OF GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WISDOM OF GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.WISDOM OF GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >WISDOM OF GOD" }]->(child);
```
