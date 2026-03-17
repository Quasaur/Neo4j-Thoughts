---
type: THOUGHT
name: "thought.EMPATHY"
alias: "Thought: Empathy"
parent: "topic.LOVE"
tags: ["emptiness", "void", "hunger", "addiction", "spirituality"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.EMPATHY",
    alias: "Thought: Empathy",
    parent: "topic.LOVE",
    tags: ["emptiness", "void", "hunger", "addiction", "spirituality"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EMPATHY",
    ctype: "THOUGHT",
    en_title: "Empathy",
    en_content: "",
    es_title: "EMPATÍA",
    es_content: "Para AMARTE, debo ser tan tolerante con tus defectos como lo soy con los míos propios.",
    fr_title: "EMPATHIE",
    fr_content: "Pour t’aimer, je dois être aussi tolérante envers tes défauts que envers les miens.",
    hi_title: "समानुभूति",
    hi_content: "आपसे प्यार करने के लिए, मुझे आपकी कमियों के प्रति उतना ही सहनशील होना होगा जितना कि अपनी कमियों के प्रति।",
    zh_title: "gòng qíng",
    zh_content: "wèi le ài nǐ ， wǒ bì xū xiàng róng rěn wǒ zì jǐ de quē diǎn yī yàng róng rěn nǐ de quē diǎn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EMPATHY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->EMPATHY"
RETURN t, parent;
```
