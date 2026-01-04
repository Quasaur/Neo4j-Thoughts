---
name: "thought.GOD OF PROJECTS"
alias: "Thought: God Of Projects"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- jesus
- administration
- order
- management
- divinity
level: 1
neo4j: true
insert: true
---
# God Of Projects

> [!Thought-en]
> Jesus Christ is The God of Project Management.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011b)
CREATE (t:THOUGHT {
    name: "thought.GOD OF PROJECTS",
    alias: "Thought: God Of Projects",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'administration', 'order', 'management', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD OF PROJECTS",
    en_title: "God Of Projects",
    en_content: "Jesus Christ is The God of Project Management.",
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
WHERE t.name = "thought.GOD OF PROJECTS" AND c.name = "content.GOD OF PROJECTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD OF PROJECTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD OF PROJECTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD OF PROJECTS" }]->(child);
```