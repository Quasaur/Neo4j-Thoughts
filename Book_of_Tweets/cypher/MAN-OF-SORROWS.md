---
name: "thought.MAN OF SORROWS"
alias: "Thought: Man Of Sorrows"
type: THOUGHT
en_content: "Jesus was a Man of sorrows...acquainted with grief--not because of what they did to Him, but what they did to each other!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- sorrow
- grief
- humanity
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.MAN OF SORROWS",
    alias: "Thought: Man Of Sorrows",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'sorrow', 'grief', 'humanity', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MAN OF SORROWS",
    en_title: "Man Of Sorrows",
    en_content: "Jesus was a Man of sorrows...acquainted with grief--not because of what they did to Him, but what they did to each other!",
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
WHERE t.name = "thought.MAN OF SORROWS" AND c.name = "content.MAN OF SORROWS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MAN OF SORROWS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MAN OF SORROWS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MAN OF SORROWS" }]->(child);
```
