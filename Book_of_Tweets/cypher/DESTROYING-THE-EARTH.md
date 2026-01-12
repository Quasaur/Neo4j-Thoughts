---
name: "thought.DESTROYING THE EARTH"
alias: "Thought: Destroying The Earth"
type: THOUGHT
en_content: "God will destroy us for destroying the Earth (Revelation 11:18)."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- earth
- destruction
- sovereignty
- bible
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013c)
CREATE (t:THOUGHT {
    name: "thought.DESTROYING THE EARTH",
    alias: "Thought: Destroying The Earth",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'earth', 'destruction', 'sovereignty', 'bible'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DESTROYING THE EARTH",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DESTROYING THE EARTH" AND c.name = "content.DESTROYING THE EARTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DESTROYING THE EARTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.DESTROYING THE EARTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >DESTROYING THE EARTH" }]->(child);
```
