---
name: "thought.SHOULD BE VS WILL BE"
alias: "Thought: Should Be Vs Will Be"
type: THOUGHT
en_content: "Everything is as it should be, but not as it will be."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- time
- prophecy
- destiny
- future
level: 2
neo4j: false
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013c)
CREATE (t:THOUGHT {
    name: "thought.SHOULD BE VS WILL BE",
    alias: "Thought: Should Be Vs Will Be",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'time', 'prophecy', 'destiny', 'future'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SHOULD BE VS WILL BE",
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

MATCH (t:THOUGHT {name: "thought.SHOULD BE VS WILL BE"})
MATCH (c:CONTENT {name: "content.SHOULD BE VS WILL BE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHOULD BE VS WILL BE" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.SHOULD BE VS WILL BE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "edge.DIVINE SOVEREIGNTY->SHOULD BE VS WILL BE" }]->(child);
```
