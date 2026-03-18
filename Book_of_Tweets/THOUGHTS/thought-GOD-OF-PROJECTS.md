---
type: THOUGHT
name: "thought.GOD OF PROJECTS"
alias: "Thought: God Of Projects"
parent: "topic.THE GODHEAD"
en_content: "Jesus Christ is The God of Project Management."
tags: ["jesus", "administration", "order", "management", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011b)
CREATE (t:THOUGHT {    name: "thought.GOD OF PROJECTS",
    alias: "Thought: God Of Projects",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'administration', 'order', 'management', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD OF PROJECTS",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD OF PROJECTS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD OF PROJECTS"
RETURN t, parent;
```
