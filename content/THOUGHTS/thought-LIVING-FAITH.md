---
type: THOUGHT
name: "thought.LIVING FAITH"
alias: "Thought: Active Belief"
parent: "topic.FAITH"
en_content: "Faith is when Divine Truth is caught by your imagination and you begin to live it."
tags: ["faith", "truth", "imagination", "lifestyle", "action"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LIVING FAITH",
    alias: "Thought: Active Belief",
    parent: "topic.FAITH",
    tags: ["faith", "truth", "imagination", "lifestyle", "action"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIVING FAITH",
    ctype: "THOUGHT",
    en_title: "Living Faith",
    en_content: "Faith is when Divine Truth is caught by your imagination and you begin to live it.",
    es_title: "Fe viva",
    es_content: "La fe es cuando la Verdad Divina es captada por tu imaginación y comienzas a vivirla.",
    fr_title: "Foi vivante",
    fr_content: "La foi, c'est quand la Vérité Divine est saisie par votre imagination et que vous commencez à la vivre.",
    hi_title: "jeevant vishvaas",
    hi_content: "विश्वास तब होता है जब दिव्य सत्य आपकी कल्पना में पकड़ लिया जाता है और आप उसे जीना शुरू कर देते हैं।",
    zh_title: "huó de xìn xīn",
    zh_content: "xìn xīn shì dāng shén shèng de zhēn lǐ bèi nǐ de xiǎng xiàng lì bǎo zhuō bìng qiě nǐ kāi shǐ shí jiàn tā dì shí hòu."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIVING FAITH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->LIVING FAITH"
RETURN t, parent;
```
