---
type: THOUGHT
name: "thought.GOD THE RECYCLER"
alias: "Thought: God The Recycler"
parent: "topic.ENVIRONMENTAL SCIENCE"
en_content: "God recycles."
tags: ["recycling", "creation", "god", "restoration", "humor"]
ptopic: "[[topic-ENVIRONMENTAL-SCIENCE]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD THE RECYCLER",
    alias: "Thought: God The Recycler",
    parent: "topic.ENVIRONMENTAL SCIENCE",
    tags: ['recycling', 'creation', 'god', 'restoration', 'humor'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.GOD THE RECYCLER",
    ctype: "THOUGHT",
    en_title: "God The Recycler",
    en_content: "God recycles.",
    es_title: "Dios El Reciclador",
    es_content: "Dios recicla.",
    fr_title: "Dieu Le Recycleur",
    fr_content: "Dieu recycle.",
    hi_title: "परमेश्वर पुनर्चक्रणकर्ता",
    hi_content: "परमेश्वर पुनर्चक्रण करता है।",
    zh_title: "Shàngdì Shì Huíshōu Zhě",
    zh_content: "Shàngdì huíshōu lìyòng."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD THE RECYCLER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ENVIRONMENTAL SCIENCE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ENVIRONMENTAL SCIENCE->GOD THE RECYCLER"
RETURN t, parent;
```
