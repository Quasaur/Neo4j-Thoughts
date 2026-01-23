---
name: "thought.APOCALYPSE BETTER WORLD"
alias: "Thought: Apocalypse Better World"
type: THOUGHT
en_content: "The Better World is coming! Apocalypse!"
parent: "topic.APOCALYPSE"
tags:
- apocalypse
- world
- future
- hope
level: 5
neo4j: false
ptopic: "[[topic-APOCALYPSE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.APOCALYPSE BETTER WORLD",
    alias: "Thought: Apocalypse Better World",
    parent: "topic.APOCALYPSE",
    tags: ['apocalypse', 'world', 'future', 'hope'],
    notes: "",
    level: 5
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
    zh_title: "Qǐshìlù gèng shìjiè",
    zh_content: "Gèng měihǎo de shìjiè jíjiāng láilín! Qǐshìlù!"
});

MATCH (t:THOUGHT {name: "thought.APOCALYPSE BETTER WORLD"})
MATCH (c:CONTENT {name: "content.APOCALYPSE BETTER WORLD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.APOCALYPSE BETTER WORLD" }]->(c);

MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MATCH (child:THOUGHT {name: "thought.APOCALYPSE BETTER WORLD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "APOCALYPSE->APOCALYPSE BETTER WORLD" }]->(child);
```
