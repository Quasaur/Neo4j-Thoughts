---
name: "thought.APOCALYPSE BETTER WORLD"
alias: "Thought: Apocalypse Better World"
type: THOUGHT
en_content: "The Better World is coming! Apocalypse!"
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- apocalypse
- world
- future
- hope
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.APOCALYPSE BETTER WORLD",
    alias: "Thought: Apocalypse Better World",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['apocalypse', 'world', 'future', 'hope'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.APOCALYPSE BETTER WORLD",
    en_title: "Apocalypse Better World",
    en_content: "The Better World is coming! Apocalypse!",
    es_title: "Apocalipsis Mundo Mejor",
    es_content: "¡El Mundo Mejor está llegando! ¡Apocalipsis!",
    fr_title: "Apocalypse Monde Meilleur",
    fr_content: "Le Monde Meilleur arrive ! Apocalypse !",
    hi_title: "सर्वनाश बेहतर दुनिया",
    hi_content: "बेहतर दुनिया आ रही है! सर्वनाश!",
    zh_title: "启示录更美好的世界",
    zh_content: "更美好的世界即将来临！启示录！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.APOCALYPSE BETTER WORLD" AND c.name = "content.APOCALYPSE BETTER WORLD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.APOCALYPSE BETTER WORLD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.APOCALYPSE BETTER WORLD"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >APOCALYPSE BETTER WORLD" }]->(child);
```
