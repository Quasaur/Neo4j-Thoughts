---
type: THOUGHT
name: "thought.CONSPIRACY THEORIES"
alias: "Thought: Conspiracy Theories"
parent: "topic.UNDERSTANDING"
en_content: "I LOVE conspiracy theories...they allow me to pass responsibility for my failures to someone else!"
tags: ["responsibility", "failure", "wisdom", "truth", "deception"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2010b)
CREATE (t:THOUGHT {    name: "thought.CONSPIRACY THEORIES",
    alias: "Thought: Conspiracy Theories",
    parent: "topic.UNDERSTANDING",
    tags: ['responsibility', 'failure', 'wisdom', 'truth', 'deception'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CONSPIRACY THEORIES",
    ctype: "THOUGHT",
    en_title: "Conspiracy Theories",
    en_content: "I LOVE conspiracy theories...they allow me to pass responsibility for my failures to someone else!",
    es_title: "Teorías de Conspiración",
    es_content: "¡AMO las teorías de conspiración... me permiten pasar la responsabilidad de mis fracasos a alguien más!",
    fr_title: "Théories du Complot",
    fr_content: "J'AIME les théories du complot... elles me permettent de passer la responsabilité de mes échecs à quelqu'un d'autre !",
    hi_title: "षड्यंत्र सिद्धांत",
    hi_content: "मैं षड्यंत्र सिद्धांतों को प्यार करता हूं... वे मुझे अपनी विफलताओं की जिम्मेदारी किसी और पर डालने की अनुमति देते हैं!",
    zh_title: "Yīn Móu Lùn",
    zh_content: "Wǒ ài yīn móu lùn... Tāmen ràng wǒ nénggòu bǎ wǒ shībài de zérèn tuī gěi biérén!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CONSPIRACY THEORIES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.UNDERSTANDING->CONSPIRACY THEORIES"
RETURN t, parent;
```
