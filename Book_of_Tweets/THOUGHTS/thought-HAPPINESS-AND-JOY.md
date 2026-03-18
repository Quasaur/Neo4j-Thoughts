---
type: THOUGHT
name: "thought.HAPPINESS AND JOY"
alias: "Thought: Happiness And Joy"
parent: "topic.SPIRITUALITY"
en_content: "Happiness: pleasing God. Joy: being pleased by God."
tags: ["happiness", "joy", "spirituality", "obedience", "blessing"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2010a)
CREATE (t:THOUGHT {    name: "thought.HAPPINESS AND JOY",
    alias: "Thought: Happiness And Joy",
    parent: "topic.SPIRITUALITY",
    tags: ['happiness', 'joy', 'spirituality', 'obedience', 'blessing'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.HAPPINESS AND JOY",
    ctype: "THOUGHT",
    en_title: "Happiness And Joy",
    en_content: "Happiness: pleasing God. Joy: being pleased by God.",
    es_title: "Felicidad y alegría",
    es_content: "Felicidad: agradar a Dios.Alegría: agradarse a Dios.",
    fr_title: "Bonheur et joie",
    fr_content: "Bonheur : plaire à Dieu.Joie : être satisfait de Dieu.",
    hi_title: "खुशी और मस्ती",
    hi_content: "ख़ुशी: भगवान को प्रसन्न करना.ख़ुशी: भगवान से प्रसन्न होना।",
    zh_title: "xìng fú yǔ kuài lè",
    zh_content: "xìng fú ： tǎo shén xǐ yuè 。 xǐ lè ： méng shén xǐ yuè 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HAPPINESS AND JOY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->HAPPINESS AND JOY"
RETURN t, parent;
```
