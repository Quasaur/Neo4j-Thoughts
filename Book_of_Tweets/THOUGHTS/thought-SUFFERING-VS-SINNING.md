---
type: THOUGHT
name: "thought.SUFFERING VS SINNING"
alias: "Thought: Suffering Vs Sinning"
parent: "topic.HUMANITY"
en_content: "We are tired of suffering, yet we are not tired of sinning."
tags: ["suffering", "sin", "humanity", "paradox", "attitude"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011d)
CREATE (t:THOUGHT {    name: "thought.SUFFERING VS SINNING",
    alias: "Thought: Suffering Vs Sinning",
    parent: "topic.HUMANITY",
    tags: ['suffering', 'sin', 'humanity', 'paradox', 'attitude'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SUFFERING VS SINNING",
    ctype: "THOUGHT",
    en_title: "Suffering Vs Sinning",
    en_content: "We are tired of suffering, yet we are not tired of sinning.",
    es_title: "Sufrir versus Pecar",
    es_content: "Estamos cansados de sufrir, pero no estamos cansados de pecar.",
    fr_title: "Souffrir contre Pécher",
    fr_content: "Nous sommes fatigués de souffrir, mais nous ne sommes pas fatigués de pécher.",
    hi_title: "दुःख बनाम पाप",
    hi_content: "हम दुःख से थक गए हैं, फिर भी हम पाप करने से नहीं थके।",
    zh_title: "Shòukǔ yǔ fànzuì  shòu kǔ yǔ fàn zuì",
    zh_content: "Wǒmen yànjàn le shòukǔ, dàn wǒmen què méiyǒu yànjàn fànzuì.  wǒ men yàn juàn le shòu kǔ ， dàn wǒ men què méi yǒu yàn juàn fàn zuì 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SUFFERING VS SINNING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->SUFFERING VS SINNING"
RETURN t, parent;
```
