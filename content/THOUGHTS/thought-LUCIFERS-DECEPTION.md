---
type: THOUGHT
name: "thought.LUCIFERS DECEPTION"
alias: "Thought: Lucifers Deception"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "God knew what Lucifer was doing...and allowed him to tempt, deceive and lead astray one third of Heaven."
tags: ["lucifer", "deception", "temptation", "evil", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LUCIFERS DECEPTION",
    alias: "Thought: Lucifers Deception",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['lucifer', 'deception', 'temptation', 'evil', 'sovereignty'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LUCIFERS DECEPTION",
    ctype: "THOUGHT",
    en_title: "Lucifers Deception",
    en_content: "God knew what Lucifer was doing...and allowed him to tempt, deceive and lead astray one third of Heaven.",
    es_title: "El Engaño de Lucifer",
    es_content: "Dios sabía lo que Lucifer estaba haciendo...y le permitió tentar, engañar y extraviar a un tercio del Cielo.",
    fr_title: "La Tromperie de Lucifer",
    fr_content: "Dieu savait ce que Lucifer faisait...et lui a permis de tenter, tromper et égarer un tiers du Ciel.",
    hi_title: "लूसिफर का छल",
    hi_content: "भगवान जानते थे कि लूसिफर क्या कर रहा था...और उन्होंने उसे स्वर्ग के एक तिहाई हिस्से को प्रलोभित करने, धोखा देने और भटकाने की अनुमति दी।",
    zh_title: "Lùxīfú de Qīpiàn",
    zh_content: "Shàngdì zhīdào Lùxīfú zài zuò shénme...bìng yǔnxǔ tā yòuhuò, qīpiàn hé mísī tiāntáng de sānfēnzhīyī."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LUCIFERS DECEPTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->LUCIFERS DECEPTION"
RETURN t, parent;
```
