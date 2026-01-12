---
name: "thought.GOD OF FINANCE"
alias: "Thought: God Of Finance"
type: THOUGHT
en_content: "Jesus Christ is The God of Finance and Economics."
parent: "topic.THE GODHEAD"
tags:
- jesus
- finance
- economics
- provision
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011c)
CREATE (t:THOUGHT {
    name: "thought.GOD OF FINANCE",
    alias: "Thought: God Of Finance",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'finance', 'economics', 'provision', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD OF FINANCE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD OF FINANCE" AND c.name = "content.GOD OF FINANCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD OF FINANCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD OF FINANCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD OF FINANCE" }]->(child);
```
