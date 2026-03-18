---
type: THOUGHT
name: "thought.GOD OF FINANCE"
alias: "Thought: God Of Finance"
parent: "topic.THE GODHEAD"
en_content: "Jesus Christ is The God of Finance and Economics."
tags: ["jesus", "finance", "economics", "provision", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011c)
CREATE (t:THOUGHT {    name: "thought.GOD OF FINANCE",
    alias: "Thought: God Of Finance",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'finance', 'economics', 'provision', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD OF FINANCE",
    ctype: "THOUGHT",
    en_title: "God Of Finance",
    en_content: "Jesus Christ is The God of Finance and Economics.",
    es_title: "Dios de las Finanzas",
    es_content: "Jesucristo es El Dios de las Finanzas y la Economía.",
    fr_title: "Dieu des Finances",
    fr_content: "Jésus-Christ est Le Dieu des Finances et de l'Économie.",
    hi_title: "वित्त के देव",
    hi_content: "यीशु मसीह वित्त और अर्थशास्त्र के देव हैं।",
    zh_title: "Cái zhèng zhī Shén",
    zh_content: "Yē sū Jī dū shì Cái zhèng hé Jīng jì xué zhī Shén."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD OF FINANCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD OF FINANCE"
RETURN t, parent;
```
