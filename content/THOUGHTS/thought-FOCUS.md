---
type: THOUGHT
name: "thought.FOCUS"
alias: "Thought: Focus"
parent: "topic.PSYCHOLOGY"
tags: ["focus", "crisis", "forward", "criticalthinking", "faith"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FOCUS",
    alias: "Thought: Focus",
    parent: "topic.PSYCHOLOGY",
    tags: ["focus", "crisis", "forward", "criticalthinking", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOCUS",
    ctype: "THOUGHT",
    en_title: "Focus",
    en_content: "",
    es_title: "ENFOCAR",
    es_content: "Cuando tu espalda está contra la pared, no tienes que mirar hacia atrás.",
    fr_title: "SE CONCENTRER",
    fr_content: "Lorsque vous êtes dos au mur, vous n’avez pas besoin de regarder derrière vous.",
    hi_title: "केंद्र",
    hi_content: "जब आपकी पीठ दीवार से सटी हो तो आपको पीछे देखने की जरूरत नहीं है।",
    zh_title: "zhòng diǎn",
    zh_content: "dāng nǐ bèi kào qiáng shí ， nǐ bù bì xiàng hòu kàn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FOCUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->FOCUS"
RETURN t, parent;
```
