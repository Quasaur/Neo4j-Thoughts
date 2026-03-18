---
type: THOUGHT
name: "thought.BETTER WORLD"
alias: "Thought: A Better World"
parent: "topic.APOCALYPSE"
en_content: "The Better World is coming! Apocalypse!"
tags: ["apocalypse", "world", "future", "hope", "new_earth"]
ptopic: "[[topic-APOCALYPSE]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {    
	name: "thought.BETTER WORLD",
    alias: "Thought: A Better World",
    parent: "topic.APOCALYPSE",
    tags: ["apocalypse", "world", "future", "hope", "new_earth"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.BETTER WORLD",
    ctype: "THOUGHT",
    en_title: "Thought: A Better World",
    en_content: "The Better World is coming! Apocalypse!",
    es_title: "Pensamiento: Un mundo mejor",
    es_content: "¡El Mundo Mejor está llegando! ¡Apocalipsis!",
    fr_title: "Pensée : Un monde meilleur",
    fr_content: "Le Monde Meilleur arrive ! Apocalypse !",
    hi_title: "विचार: एक बेहतर दुनिया",
    hi_content: "बेहतर दुनिया आ रही है! सर्वनाश!",
    zh_title: "sī xiǎng : yí gè gèng měi hǎo de shì jiè",
    zh_content: "Gèng měihǎo de shìjiè jíjiāng láilín! Qǐshìlù!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BETTER WORLD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.APOCALYPSE->BETTER WORLD"
RETURN t, parent;
```
