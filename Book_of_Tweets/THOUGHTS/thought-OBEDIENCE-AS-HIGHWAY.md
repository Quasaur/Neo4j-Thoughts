---
type: THOUGHT
name: "thought.OBEDIENCE AS HIGHWAY"
alias: "Thought: Obedience As Highway"
parent: "topic.SPIRITUALITY"
en_content: "Obedience is like the lines on a highway: though restrictive, they will take you where you need to go."
tags: ["obedience", "guidance", "restriction", "spirituality", "direction"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2011a)
CREATE (t:THOUGHT {    name: "thought.OBEDIENCE AS HIGHWAY",
    alias: "Thought: Obedience As Highway",
    parent: "topic.SPIRITUALITY",
    tags: ['obedience', 'guidance', 'restriction', 'spirituality', 'direction'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.OBEDIENCE AS HIGHWAY",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OBEDIENCE AS HIGHWAY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->OBEDIENCE AS HIGHWAY"
RETURN t, parent;
```
