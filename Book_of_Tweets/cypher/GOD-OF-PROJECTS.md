---
name: "thought.GOD OF PROJECTS"
alias: "Thought: God Of Projects"
type: THOUGHT
en_content: "Jesus Christ is The God of Project Management."
parent: "topic.THE GODHEAD"
tags:
- jesus
- administration
- order
- management
- divinity
level: 1
neo4j: true
ptopic: 
---

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
    es_title: "Dios de Proyectos",
    es_content: "Jesucristo es El Dios de la Gestión de Proyectos.",
    fr_title: "Dieu des Projets",
    fr_content: "Jésus-Christ est Le Dieu de la Gestion de Projets.",
    hi_title: "परियोजनाओं के परमेश्वर",
    hi_content: "यीशु मसीह परियोजना प्रबंधन के परमेश्वर हैं।",
    zh_title: "Xiangmu de Shen",
    zh_content: "Yesu Jidu shi Xiangmu Guanli de Shen."
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
