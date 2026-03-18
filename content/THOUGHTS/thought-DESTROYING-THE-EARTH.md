---
type: THOUGHT
name: "thought.DESTROYING THE EARTH"
alias: "Thought: Destroying The Earth"
parent: "topic.ENVIRONMENTAL SCIENCE"
en_content: "God will destroy us for destroying the Earth (Revelation 11:18)."
tags: ["judgment", "earth", "destruction", "sovereignty", "bible"]
ptopic: "[[topic-ENVIRONMENTAL-SCIENCE]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DESTROYING THE EARTH",
    alias: "Thought: Destroying The Earth",
    parent: "topic.ENVIRONMENTAL SCIENCE",
    tags: ['judgment', 'earth', 'destruction', 'sovereignty', 'bible'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.DESTROYING THE EARTH",
    ctype: "THOUGHT",
    en_title: "Destroying The Earth",
    en_content: "God will destroy us for destroying the Earth (Revelation 11:18).",
    es_title: "Destruyendo la Tierra",
    es_content: "Dios nos destruirá por destruir la Tierra (Apocalipsis 11:18).",
    fr_title: "Détruire la Terre",
    fr_content: "Dieu nous détruira pour avoir détruit la Terre (Apocalypse 11:18).",
    hi_title: "पृथ्वी का नाश",
    hi_content: "पृथ्वी को नष्ट करने के लिए परमेश्वर हमें नष्ट करेगा (प्रकाशितवाक्य 11:18)।",
    zh_title: "Huimie Diqiu",
    zh_content: "Shangdi hui yinwei women huimie diqiu er huimie women (Qishilu 11:18)."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DESTROYING THE EARTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ENVIRONMENTAL SCIENCE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ENVIRONMENTAL SCIENCE->DESTROYING THE EARTH"
RETURN t, parent;
```
