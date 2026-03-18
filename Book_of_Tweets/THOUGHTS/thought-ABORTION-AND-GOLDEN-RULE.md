---
type: THOUGHT
name: "thought.ABORTION AND GOLDEN RULE"
alias: "Thought: Abortion And Golden Rule"
parent: "topic.MORALITY"
en_content: "Abortion is a violation of the Golden Rule: \"Do unto others as you would have them do into you.\""
tags: ["morality", "abortion", "golden_rule", "justice", "ethics"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011b)
CREATE (t:THOUGHT {    name: "thought.ABORTION AND GOLDEN RULE",
    alias: "Thought: Abortion And Golden Rule",
    parent: "topic.MORALITY",
    tags: ['morality', 'abortion', 'golden_rule', 'justice', 'ethics'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.ABORTION AND GOLDEN RULE",
    ctype: "THOUGHT",
    en_title: "Abortion And Golden Rule",
    en_content: "Abortion is a violation of the Golden Rule: \"Do unto others as you would have them do into you.\"",
    es_title: "El Aborto y la Regla de Oro",
    es_content: "El aborto es una violación de la Regla de Oro: \"Haz a los demás lo que quieras que te hagan a ti.\"",
    fr_title: "L'avortement et la Règle d'Or",
    fr_content: "L'avortement est une violation de la Règle d'Or : \"Fais aux autres ce que tu voudrais qu'ils te fassent.\"",
    hi_title: "गर्भपात और स्वर्णिम नियम",
    hi_content: "गर्भपात स्वर्णिम नियम का उल्लंघन है: \"दूसरों के साथ वैसा ही करो जैसा तुम चाहते हो कि तुम्हारे साथ किया जाए।\"",
    zh_title: "Duòtāi yǔ huángjīn fǎzé",
    zh_content: "Duòtāi wéifǎnle huángjīn fǎzé."jǐ suǒ bù yù ， wù shī yú rén 。\""
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ABORTION AND GOLDEN RULE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->ABORTION AND GOLDEN RULE"
RETURN t, parent;
```
