---
type: THOUGHT
name: "thought.UNCONDITIONAL LOVE PRAYER"
alias: "Thought: Unconditional Love Prayer"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is where I am loved unconditionally."
tags: ["prayer", "love", "acceptance", "spirituality", "presence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013f)
CREATE (t:THOUGHT {    name: "thought.UNCONDITIONAL LOVE PRAYER",
    alias: "Thought: Unconditional Love Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'love', 'acceptance', 'spirituality', 'presence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL LOVE PRAYER",
    ctype: "THOUGHT",
    en_title: "Unconditional Love Prayer",
    en_content: "Prayer is where I am loved unconditionally.",
    es_title: "Oración de Amor Incondicional",
    es_content: "La oración es donde soy amado incondicionalmente.",
    fr_title: "Prière d'Amour Inconditionnel",
    fr_content: "La prière est où je suis aimé inconditionnellement.",
    hi_title: "निःशर्त प्रेम की प्रार्थना",
    hi_content: "प्रार्थना वह स्थान है जहाँ मुझे निःशर्त प्रेम मिलता है।",
    zh_title: "Wú tiáo jiàn ài de qí dǎo",
    zh_content: "Qí dǎo shì wǒ dé dào wú tiáo jiàn zhī ài de dì fāng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNCONDITIONAL LOVE PRAYER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->UNCONDITIONAL LOVE PRAYER"
RETURN t, parent;
```
