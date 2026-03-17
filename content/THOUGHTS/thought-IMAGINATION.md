---
type: THOUGHT
name: "thought.IMAGINATION"
alias: "Thought: Imagination"
parent: "topic.UNDERSTANDING"
tags: ["imagination", "imagery", "vision", "mind", "realization"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.IMAGINATION",
    alias: "Thought: Imagination",
    parent: "topic.UNDERSTANDING",
    tags: ["imagination", "imagery", "vision", "mind", "realization"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.IMAGINATION",
    ctype: "THOUGHT",
    en_title: "Imagination",
    en_content: "",
    es_title: "IMAGINACIÓN",
    es_content: "La imaginación fue diseñada para ser el vehículo mediante el cual podamos captar, apreciar y someternos a la Verdad Divina; no el motor de fantasías y delirios de grandeza.",
    fr_title: "IMAGINATION",
    fr_content: "L'imagination a été conçue pour être le véhicule par lequel nous sommes capables de saisir, d'apprécier et de nous soumettre à la Vérité Divine ; pas le moteur des fantasmes et de la folie des grandeurs.",
    hi_title: "कल्पना",
    hi_content: "कल्पना को वह माध्यम बनाने के लिए डिज़ाइन किया गया था जिसके द्वारा हम दिव्य सत्य को समझने, सराहने और उसके प्रति समर्पण करने में सक्षम होते हैं; कल्पनाओं और भव्यता के भ्रम का इंजन नहीं।",
    zh_title: "xiǎng xiàng lì",
    zh_content: "xiǎng xiàng lì bèi shè jì wèi wǒ men néng gòu zhǎng wò 、 xīn shǎng hé fú cóng shén shèng zhēn lǐ de gōng jù ； bú shì huàn xiǎng hé wěi dà wàng xiǎng de yǐn qíng 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IMAGINATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.UNDERSTANDING->IMAGINATION"
RETURN t, parent;
```
