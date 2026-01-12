---
name: "thought.GOD WANTS ME"
alias: "Thought: God Wants Me"
type: THOUGHT
en_content: "Everybody demands something from me, but only God wants me."
parent: "topic.THE GODHEAD"
tags:
- love
- desire
- god
- relationship
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2012c)
CREATE (t:THOUGHT {
    name: "thought.GOD WANTS ME",
    alias: "Thought: God Wants Me",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'desire', 'god', 'relationship', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD WANTS ME",
    en_title: "God Wants Me",
    en_content: "Everybody demands something from me, but only God wants me.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD WANTS ME" AND c.name = "content.GOD WANTS ME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD WANTS ME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD WANTS ME"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD WANTS ME" }]->(child);
```
