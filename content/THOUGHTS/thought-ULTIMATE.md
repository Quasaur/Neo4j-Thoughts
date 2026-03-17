---
type: THOUGHT
name: "thought.ULTIMATE"
alias: "Thought: The Ultimate"
parent: "topic.THE GODHEAD"
en_content: "That which is Ultimate cannot be Ultimate unless \"it\" (He) is also PERSONAL."
tags: ["humanity", "self_worship", "god", "judgement", "accountable"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ULTIMATE",
    alias: "Thought: The Ultimate",
    parent: "topic.THE GODHEAD",
    tags: ["humanity", "self_worship", "god", "judgement", "accountable"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ULTIMATE",
    ctype: "THOUGHT",
    en_title: "Ultimate",
    en_content: "That which is Ultimate cannot be Ultimate unless \\\"it\\\" (He) is also PERSONAL.",
    es_title: "LO ÚLTIMO",
    es_content: "Aquello que es Último no puede ser Último a menos que \\\"eso\\\" (Él) sea también PERSONAL.",
    fr_title: "L'ULTIME",
    fr_content: "Ce qui est Ultime ne peut pas être Ultime à moins que « cela » (Il) ne soit également PERSONNEL.",
    hi_title: "अंतिम",
    hi_content: "जो परम है वह परम नहीं हो सकता जब तक कि \\\"वह\\\" भी व्यक्तिगत न हो।",
    zh_title: "zhōng jí",
    zh_content: "chú fēi “ tā ”（ tā ） yě shì gè rén de ， fǒu zé zhōng jí bù kě néng shì zhōng jí de 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ULTIMATE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->ULTIMATE"
RETURN t, parent;
```
