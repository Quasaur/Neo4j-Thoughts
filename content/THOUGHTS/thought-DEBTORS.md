---
type: THOUGHT
name: "thought.DEBTORS"
alias: "Thought: Debtors"
parent: "topic.ECONOMICS"
tags: ["economics", "nation", "debtors", "slaves", "liability"]
ptopic: "[[topic-ECONOMICS]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEBTORS",
    alias: "Thought: Debtors",
    parent: "topic.ECONOMICS",
    tags: ["economics", "nation", "debtors", "slaves", "liability"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEBTORS",
    ctype: "THOUGHT",
    en_title: "Debtors",
    en_content: "A nation of debtors is a nation of slaves.",
    es_title: "DEUDORES",
    es_content: "Una nación de deudores es una nación de esclavos.",
    fr_title: "DÉBITEURS",
    fr_content: "Une nation de débiteurs est une nation d’esclaves.",
    hi_title: "देनदार",
    hi_content: "कर्ज़दारों का राष्ट्र गुलामों का राष्ट्र होता है।",
    zh_title: "zhài wù rén",
    zh_content: "yí gè zhài wù rén de guó jiā jiù shì yí gè nú lì de guó jiā 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEBTORS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ECONOMICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ECONOMICS->DEBTORS"
RETURN t, parent;
```
