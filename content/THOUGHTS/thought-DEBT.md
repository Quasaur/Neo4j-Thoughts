---
type: THOUGHT
name: "thought.DEBT"
alias: "Thought: Debt"
parent: "topic.ENTITLEMENT"
tags: ["debt", "entitlement", "apocalypse", "worship", "grace"]
ptopic: "[[topic-ENTITLEMENT]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEBT",
    alias: "Thought: Debt",
    parent: "topic.ENTITLEMENT",
    tags: ["debt", "entitlement", "apocalypse", "worship", "grace"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEBT",
    ctype: "THOUGHT",
    en_title: "Debt",
    en_content: "A nation of debtors is a nation of slaves.",
    es_title: "DEUDA",
    es_content: "Una nación de deudores es una nación de esclavos.",
    fr_title: "DETTE",
    fr_content: "Une nation de débiteurs est une nation d’esclaves.",
    hi_title: "ऋृण",
    hi_content: "कर्ज़दारों का राष्ट्र गुलामों का राष्ट्र होता है।",
    zh_title: "zhài wù",
    zh_content: "yí gè zhài wù rén de guó jiā jiù shì yí gè nú lì de guó jiā 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEBT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ENTITLEMENT"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ENTITLEMENT->DEBT"
RETURN t, parent;
```
