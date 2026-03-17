---
type: THOUGHT
name: "thought.LOVE2"
alias: "Thought: Love 2"
parent: "topic.LOVE"
tags: ["love", "sacrificial", "give", "selfless", "cause"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOVE2",
    alias: "Thought: Love 2",
    parent: "topic.LOVE",
    tags: ["love", "sacrificial", "give", "selfless", "cause"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE2",
    ctype: "THOUGHT",
    en_title: "Love 2",
    en_content: "",
    es_title: "AMOR 2",
    es_content: "¿Qué te impulsa a entregarte a una causa más grande que tú? AMAR.",
    fr_title: "AMOUR 2",
    fr_content: "Qu’est-ce qui vous pousse à vous consacrer à une cause plus grande que vous ? AMOUR.",
    hi_title: "प्यार 2",
    hi_content: "कौन सी चीज़ आपको अपने आप को अपने से बड़े उद्देश्य के लिए समर्पित करने के लिए प्रेरित करती है? प्यार।",
    zh_title: "ài 2",
    zh_content: "shì shén me qū shǐ nǐ quán shēn xīn tóu rù dào bǐ nǐ gèng wěi dà de shì yè zhōng ？ ài 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE2"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->LOVE2"
RETURN t, parent;
```
