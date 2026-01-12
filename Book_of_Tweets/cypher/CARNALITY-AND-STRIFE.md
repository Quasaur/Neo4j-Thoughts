---
name: "thought.CARNALITY AND STRIFE"
alias: "Thought: Carnality And Strife"
type: THOUGHT
en_content: "1 Corinthians 3:3: \"...for whereas there is among you envying, and strife, and divisions, are ye not carnal, and walk as men?\""
parent: "topic.MORALITY"
tags:
- morality
- carnality
- strife
- church
- bible
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.CARNALITY AND STRIFE",
    alias: "Thought: Carnality And Strife",
    parent: "topic.MORALITY",
    tags: ['morality', 'carnality', 'strife', 'church', 'bible'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CARNALITY AND STRIFE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CARNALITY AND STRIFE" AND c.name = "content.CARNALITY AND STRIFE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CARNALITY AND STRIFE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CARNALITY AND STRIFE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CARNALITY AND STRIFE" }]->(child);
```
