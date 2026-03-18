---
type: THOUGHT
name: "thought.CARNALITY AND STRIFE"
alias: "Thought: Carnality And Strife"
parent: "topic.MORALITY"
en_content: "1 Corinthians 3:3: \"...for whereas there is among you envying, and strife, and divisions, are ye not carnal, and walk as men?\""
tags: ["morality", "carnality", "strife", "church", "bible"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Sep-2011)
CREATE (t:THOUGHT {    name: "thought.CARNALITY AND STRIFE",
    alias: "Thought: Carnality And Strife",
    parent: "topic.MORALITY",
    tags: ['morality', 'carnality', 'strife', 'church', 'bible'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CARNALITY AND STRIFE",
    ctype: "THOUGHT",
    en_title: "Carnality And Strife",
    en_content: "1 Corinthians 3:3: \"...for whereas there is among you envying, and strife, and divisions, are ye not carnal, and walk as men?\"",
    es_title: "Carnalidad y Contienda",
    es_content: "1 Corintios 3:3: \"...porque habiendo entre vosotros celos, y contiendas, y disensiones, ¿no sois carnales, y andáis como hombres?\"",
    fr_title: "Carnalité et Querelle",
    fr_content: "1 Corinthiens 3:3 : \"...car, puisqu'il y a parmi vous de la jalousie et des disputes, n'êtes-vous pas charnels, et ne marchez-vous pas selon l'homme ?\"",
    hi_title: "शारीरिकता और कलह",
    hi_content: "1 कुरिन्थियों 3:3: \"...क्योंकि जब तुम में डाह और झगड़े हैं, तो क्या तुम शारीरिक नहीं हो, और मनुष्य के समान नहीं चलते?\"",
    zh_title: "Ròutǐ hé Zhēngzhí",
    zh_content: "Gēlínduō qiánshū 3:3: \"...nǐmen réng shì shǔ ròutǐ de, yīnwèi zài nǐmen zhōngjiān yǒu jí dù, fēnzhēng, zhè qǐbùshì shǔ hūròutǐ, zhào zhe shìrén de yàngzi xíng ma?\""
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CARNALITY AND STRIFE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CARNALITY AND STRIFE"
RETURN t, parent;
```
