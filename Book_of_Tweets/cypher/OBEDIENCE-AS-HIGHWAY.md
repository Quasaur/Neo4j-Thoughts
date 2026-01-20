---
name: "thought.OBEDIENCE AS HIGHWAY"
alias: "Thought: Obedience As Highway"
type: THOUGHT
en_content: "Obedience is like the lines on a highway: though restrictive, they will take you where you need to go."
parent: "topic.SPIRITUALITY"
tags:
- obedience
- guidance
- restriction
- spirituality
- direction
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.OBEDIENCE AS HIGHWAY",
    alias: "Thought: Obedience As Highway",
    parent: "topic.SPIRITUALITY",
    tags: ['obedience', 'guidance', 'restriction', 'spirituality', 'direction'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OBEDIENCE AS HIGHWAY",
    en_title: "Obedience As Highway",
    en_content: "Obedience is like the lines on a highway: though restrictive, they will take you where you need to go.",
    es_title: "La Obediencia Como Autopista",
    es_content: "La obediencia es como las líneas de una autopista: aunque restrictivas, te llevarán a donde necesitas ir.",
    fr_title: "L'Obéissance Comme Autoroute",
    fr_content: "L'obéissance est comme les lignes sur une autoroute : bien que restrictives, elles vous mèneront là où vous devez aller.",
    hi_title: "आज्ञाकारिता राजमार्ग के समान",
    hi_content: "आज्ञाकारिता राजमार्ग की लकीरों के समान है: यद्यपि प्रतिबंधक हैं, वे आपको वहाँ ले जाएंगी जहाँ आपको जाना चाहिए।",
    zh_title: "Shùncóng Rú Gāosù Gōnglù",
    zh_content: "Shùncóng jiù xiàng gāosù gōnglù shàng de xiàn: suīrán yǒu xiànzhì, dàn tāmen huì dài nǐ dào nǐ xūyào qù de dìfāng."
});

MATCH (t:THOUGHT {name: "thought.OBEDIENCE AS HIGHWAY"})
MATCH (c:CONTENT {name: "content.OBEDIENCE AS HIGHWAY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.OBEDIENCE AS HIGHWAY" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.OBEDIENCE AS HIGHWAY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >OBEDIENCE AS HIGHWAY" }]->(child);
```
