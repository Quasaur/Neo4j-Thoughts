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
neo4j: true
ptopic: 
insert: true
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
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
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
