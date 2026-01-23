---
name: "thought.ABORTION AND GOLDEN RULE"
alias: "Thought: Abortion And Golden Rule"
type: THOUGHT
en_content: "Abortion is a violation of the Golden Rule: \"Do unto others as you would have them do into you.\""
parent: "topic.MORALITY"
tags:
- morality
- abortion
- golden_rule
- justice
- ethics
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.ABORTION AND GOLDEN RULE",
    alias: "Thought: Abortion And Golden Rule",
    parent: "topic.MORALITY",
    tags: ['morality', 'abortion', 'golden_rule', 'justice', 'ethics'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ABORTION AND GOLDEN RULE",
    en_title: "Abortion And Golden Rule",
    en_content: "Abortion is a violation of the Golden Rule: \"Do unto others as you would have them do into you.\"",
    es_title: "El Aborto y la Regla de Oro",
    es_content: "El aborto es una violación de la Regla de Oro: \"Haz a los demás lo que quieras que te hagan a ti.\"",
    fr_title: "L'avortement et la Règle d'Or",
    fr_content: "L'avortement est une violation de la Règle d'Or : \"Fais aux autres ce que tu voudrais qu'ils te fassent.\"",
    hi_title: "गर्भपात और स्वर्णिम नियम",
    hi_content: "गर्भपात स्वर्णिम नियम का उल्लंघन है: \"दूसरों के साथ वैसा ही करो जैसा तुम चाहते हो कि तुम्हारे साथ किया जाए।\"",
    zh_title: "Duòtāi yǔ huángjīn fǎzé",
    zh_content: "Duòtāi wéifǎnle huángjīn fǎzé."己所不欲，勿施于人。\""
});

MATCH (t:THOUGHT {name: "thought.ABORTION AND GOLDEN RULE"})
MATCH (c:CONTENT {name: "content.ABORTION AND GOLDEN RULE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ABORTION AND GOLDEN RULE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.ABORTION AND GOLDEN RULE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ABORTION AND GOLDEN RULE" }]->(child);
```
