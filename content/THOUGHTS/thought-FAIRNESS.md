---
type: THOUGHT
name: "thought.FAIRNESS"
alias: "Thought: Fairness"
parent: "topic.JUSTICE"
tags: ["justice", "fairness", "mercy", "forgiveness", "compassion"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FAIRNESS",
    alias: "Thought: Fairness",
    parent: "topic.JUSTICE",
    tags: ["justice", "fairness", "mercy", "forgiveness", "compassion"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FAIRNESS",
    ctype: "THOUGHT",
    en_title: "Fairness",
    en_content: "",
    es_title: "JUSTICIA",
    es_content: "La misericordia nunca es justa.",
    fr_title: "JUSTICE",
    fr_content: "La miséricorde n'est jamais juste.",
    hi_title: "फेयरनेस",
    hi_content: "दया कभी भी उचित नहीं होती.",
    zh_title: "gōng píng xìng",
    zh_content: "lián mǐn cóng lái dōu bú shì gōng píng de 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FAIRNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.JUSTICE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.JUSTICE->FAIRNESS"
RETURN t, parent;
```
