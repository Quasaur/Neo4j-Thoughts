---
name: "thought.LUCIFERS DECEPTION"
alias: "Thought: Lucifers Deception"
type: THOUGHT
en_content: "God knew what Lucifer was doing...and allowed him to tempt, deceive and lead astray one third of Heaven."
parent: "topic.EVIL"
tags:
- lucifer
- deception
- temptation
- evil
- sovereignty
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.LUCIFERS DECEPTION",
    alias: "Thought: Lucifers Deception",
    parent: "topic.EVIL",
    tags: ['lucifer', 'deception', 'temptation', 'evil', 'sovereignty'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LUCIFERS DECEPTION",
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

MATCH (t:THOUGHT {name: "thought.LUCIFERS DECEPTION"})
MATCH (c:CONTENT {name: "content.LUCIFERS DECEPTION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LUCIFERS DECEPTION" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.LUCIFERS DECEPTION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL->LUCIFERS DECEPTION" }]->(child);
```
