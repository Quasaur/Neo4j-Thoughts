---
type: THOUGHT
name: "thought.SHOULD BE VS WILL BE"
alias: "Thought: Should Be Vs Will Be"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "Everything is as it should be, but not as it will be."
tags: ["sovereignty", "time", "prophecy", "destiny", "future"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SHOULD BE VS WILL BE",
    alias: "Thought: Should Be Vs Will Be",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'time', 'prophecy', 'destiny', 'future'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SHOULD BE VS WILL BE",
    ctype: "THOUGHT",
    en_title: "Should Be Vs Will Be",
    en_content: "Everything is as it should be, but not as it will be.",
    es_title: "Debería Ser Vs Será",
    es_content: "Todo es como debería ser, pero no como será.",
    fr_title: "Devrait Être Vs Sera",
    fr_content: "Tout est comme cela devrait être, mais pas comme cela sera.",
    hi_title: "होना चाहिए बनाम होगा",
    hi_content: "सब कुछ वैसा है जैसा होना चाहिए, लेकिन वैसा नहीं जैसा होगा।",
    zh_title: "Ying Gai Shi Vs Jiang Hui Shi",
    zh_content: "Yi qie dou ru qi suo ying, dan fei ru qi suo jiang."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SHOULD BE VS WILL BE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->SHOULD BE VS WILL BE"
RETURN t, parent;
```
