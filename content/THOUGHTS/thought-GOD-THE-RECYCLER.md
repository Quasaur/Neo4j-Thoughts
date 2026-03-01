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
---





```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.GOD THE RECYCLER",
    alias: "Thought: God The Recycler",
    parent: "topic.ENVIRONMENTAL SCIENCE",
    tags: ['recycling', 'creation', 'god', 'restoration', 'humor'],
    notes: "",
    level: 6
});

CREATE (c:CONTENT {
    name: "content.GOD THE RECYCLER",
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

MATCH (t:THOUGHT {name: "thought.GOD THE RECYCLER"})
MATCH (c:CONTENT {name: "content.GOD THE RECYCLER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD THE RECYCLER" }]->(c);

MATCH (parent:TOPIC {name: "topic.ENVIRONMENTAL SCIENCE"})
MATCH (child:THOUGHT {name: "thought.GOD THE RECYCLER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "ENVIRONMENTAL SCIENCE->GOD THE RECYCLER" }]->(child);
```
