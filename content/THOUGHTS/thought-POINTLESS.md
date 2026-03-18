---
type: THOUGHT
name: "thought.POINTLESS"
alias: "Thought: Pointless"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["pointless", "purpose", "meaning", "god", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.POINTLESS",
    alias: "Thought: Pointless",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["pointless", "purpose", "meaning", "god", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.POINTLESS",
    ctype: "THOUGHT",
    en_title: "Pointless",
    en_content: "",
    es_title: "INÚTIL",
    es_content: "Una vida sin Dios es verdaderamente inútil.",
    fr_title: "INUTILE",
    fr_content: "Une vie sans Dieu est vraiment inutile.",
    hi_title: "व्यर्थ",
    hi_content: "ईश्वर-विहीन जीवन वास्तव में व्यर्थ है।",
    zh_title: "wú yì yì",
    zh_content: "méi yǒu shén de shēng huó què shí háo wú yì yì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.POINTLESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->POINTLESS"
RETURN t, parent;
```
