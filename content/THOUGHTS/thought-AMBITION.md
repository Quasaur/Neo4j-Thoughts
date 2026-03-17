---
type: THOUGHT
name: "thought.AMBITION"
alias: "Thought: Ambition"
parent: "topic.THE-GOSPEL"
tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.AMBITION",
    alias: "Thought: Ambition",
    parent: "topic.THE-GOSPEL",
    tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.AMBITION",
    ctype: "THOUGHT",
    en_title: "Ambition",
    en_content: "",
    es_title: "AMBICIÓN",
    es_content: "¡Dios es todo lo que quieres ser!",
    fr_title: "AMBITION",
    fr_content: "Dieu est tout ce que vous voulez être !",
    hi_title: "महत्वाकांक्षा",
    hi_content: "ईश्वर वह सब कुछ है जो आप बनना चाहते हैं!",
    zh_title: "zhì xiàng",
    zh_content: "shén jiù shì nǐ xiǎng chéng wéi de yī qiè ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AMBITION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->AMBITION"
RETURN t, parent;
```
