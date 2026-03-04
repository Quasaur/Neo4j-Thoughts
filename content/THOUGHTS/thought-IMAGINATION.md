---
type: THOUGHT
name: "thought.IMAGINATION"
alias: "Thought: Imagination"
parent: "topic.UNDERSTANDING"
tags: ["imagination", "imagery", "vision", "mind", "realization"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
---

```Cypher
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
 es_title: "IMAGINACIÓN",
 fr_title: "IMAGINATION",
 hi_title: "कल्पना",
 zh_title: "xiǎng xiàng lì",
    en_content: "",
 es_content: "La imaginación fue diseñada para ser el vehículo mediante el cual podamos captar, apreciar y someternos a la Verdad Divina; no el motor de fantasías y delirios de grandeza.",
 fr_content: "L'imagination a été conçue pour être le véhicule par lequel nous sommes capables de saisir, d'apprécier et de nous soumettre à la Vérité Divine ; pas le moteur des fantasmes et de la folie des grandeurs.",
 hi_content: "कल्पना को वह माध्यम बनाने के लिए डिज़ाइन किया गया था जिसके द्वारा हम दिव्य सत्य को समझने, सराहने और उसके प्रति समर्पण करने में सक्षम होते हैं; कल्पनाओं और भव्यता के भ्रम का इंजन नहीं।",
 zh_content: "xiǎng xiàng lì bèi shè jì wèi wǒ men néng gòu zhǎng wò 、 xīn shǎng hé fú cóng shén shèng zhēn lǐ de gōng jù ； bú shì huàn xiǎng hé wěi dà wàng xiǎng de yǐn qíng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMAGINATION" AND c.name = "content.IMAGINATION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.IMAGINATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.IMAGINATION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.UNDERSTANDING->IMAGINATION"}]->(child);
```