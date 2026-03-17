---
type: THOUGHT
name: "thought.HAPPY SABBATH"
alias: "Thought: Happy Sabbath"
parent: "topic.CREATION"
en_content: "Happy Sabbath, Earth!"
tags: ["happy", "sabbath", "earth", "creation", "rest"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HAPPY SABBATH",
    alias: "Thought: Happy Sabbath",
    parent: "topic.CREATION",
    tags: ["happy", "sabbath", "earth", "creation", "rest"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HAPPY SABBATH",
    ctype: "THOUGHT",
    en_title: "Happy Sabbath",
    en_content: "Happy Sabbath, Earth!",
    es_title: "FELIZ SÁBADO",
    es_content: "¡Feliz sábado, Tierra!",
    fr_title: "JOYEUX SABBAT",
    fr_content: "Joyeux sabbat, Terre !",
    hi_title: "शुभ सब्बाथ",
    hi_content: "शुभ सब्बाथ, पृथ्वी!",
    zh_title: "ān xī rì kuài lè",
    zh_content: "ān xī rì kuài lè ， dì qiú ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HAPPY SABBATH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->HAPPY SABBATH"
RETURN t, parent;
```
