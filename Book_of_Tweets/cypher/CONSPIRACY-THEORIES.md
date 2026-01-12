---
name: "thought.CONSPIRACY THEORIES"
alias: "Thought: Conspiracy Theories"
type: THOUGHT
en_content: "I LOVE conspiracy theories...they allow me to pass responsibility for my failures to someone else!"
parent: "topic.UNDERSTANDING"
tags:
- responsibility
- failure
- wisdom
- truth
- deception
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2010b)
CREATE (t:THOUGHT {
    name: "thought.CONSPIRACY THEORIES",
    alias: "Thought: Conspiracy Theories",
    parent: "topic.UNDERSTANDING",
    tags: ['responsibility', 'failure', 'wisdom', 'truth', 'deception'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONSPIRACY THEORIES",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONSPIRACY THEORIES" AND c.name = "content.CONSPIRACY THEORIES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONSPIRACY THEORIES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.CONSPIRACY THEORIES"
MERGE (parent)-[:HAS_THOUGHT { "name": "UNDERSTANDING >CONSPIRACY THEORIES" }]->(child);
```
