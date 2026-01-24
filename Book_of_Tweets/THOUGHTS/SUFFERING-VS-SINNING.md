---
name: "thought.SUFFERING VS SINNING"
alias: "Thought: Suffering Vs Sinning"
type: THOUGHT
en_content: "We are tired of suffering, yet we are not tired of sinning."
parent: "topic.HUMANITY"
tags:
- suffering
- sin
- humanity
- paradox
- attitude
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011d)
CREATE (t:THOUGHT {
    name: "thought.SUFFERING VS SINNING",
    alias: "Thought: Suffering Vs Sinning",
    parent: "topic.HUMANITY",
    tags: ['suffering', 'sin', 'humanity', 'paradox', 'attitude'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SUFFERING VS SINNING",
    en_title: "Suffering Vs Sinning",
    en_content: "We are tired of suffering, yet we are not tired of sinning.",
    es_title: "Sufrir versus Pecar",
    es_content: "Estamos cansados de sufrir, pero no estamos cansados de pecar.",
    fr_title: "Souffrir contre Pécher",
    fr_content: "Nous sommes fatigués de souffrir, mais nous ne sommes pas fatigués de pécher.",
    hi_title: "दुःख बनाम पाप",
    hi_content: "हम दुःख से थक गए हैं, फिर भी हम पाप करने से नहीं थके।",
    zh_title: "Shòukǔ yǔ fànzuì 受苦与犯罪",
    zh_content: "Wǒmen yànjàn le shòukǔ, dàn wǒmen què méiyǒu yànjàn fànzuì. 我们厌倦了受苦，但我们却没有厌倦犯罪。"
});

MATCH (t:THOUGHT {name: "thought.SUFFERING VS SINNING"})
MATCH (c:CONTENT {name: "content.SUFFERING VS SINNING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUFFERING VS SINNING" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.SUFFERING VS SINNING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->SUFFERING VS SINNING" }]->(child);
```
