---
type: THOUGHT
name: "thought.JESUS NON NEGOTIABLE"
alias: "Thought: Jesus Non Negotiable"
parent: "topic.SPIRITUALITY"
en_content: "I must have Jesus...everything else is negotiable."
tags: ["jesus", "priority", "spirituality", "commitment", "devotion"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012c)
CREATE (t:THOUGHT {    name: "thought.JESUS NON NEGOTIABLE",
    alias: "Thought: Jesus Non Negotiable",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'priority', 'spirituality', 'commitment', 'devotion'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.JESUS NON NEGOTIABLE",
    ctype: "THOUGHT",
    en_title: "Jesus Non Negotiable",
    en_content: "I must have Jesus...everything else is negotiable.",
    es_title: "Jesús No Negociable",
    es_content: "Debo tener a Jesús...todo lo demás es negociable.",
    fr_title: "Jésus Non Négociable",
    fr_content: "Je dois avoir Jésus...tout le reste est négociable.",
    hi_title: "यीशु अपरिवर्तनीय",
    hi_content: "मुझे यीशु चाहिए...बाकी सब कुछ परिवर्तनीय है।",
    zh_title: "Yesu Buke Tanpan",
    zh_content: "Wo bixu yongyou Yesu...qita yiqie dou keyi tanpan."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.JESUS NON NEGOTIABLE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->JESUS NON NEGOTIABLE"
RETURN t, parent;
```
