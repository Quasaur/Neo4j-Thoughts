---
type: THOUGHT
name: "thought.ANNIHILATION OF EVIL"
alias: "Thought: Annihilation Of Evil"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "Evil itself is doomed to annihilation...forever."
tags: ["evil", "destruction", "sovereignty", "prophecy", "forever"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ANNIHILATION OF EVIL",
    alias: "Thought: Annihilation Of Evil",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['evil', 'destruction', 'sovereignty', 'prophecy', 'forever'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ANNIHILATION OF EVIL",
    ctype: "THOUGHT",
    en_title: "Annihilation Of Evil",
    en_content: "Evil itself is doomed to annihilation...forever.",
    es_title: "Aniquilación del Mal",
    es_content: "El mal mismo está condenado a la aniquilación... para siempre.",
    fr_title: "Anéantissement du Mal",
    fr_content: "Le mal lui-même est voué à l'anéantissement... pour toujours.",
    hi_title: "बुराई का विनाश",
    hi_content: "बुराई स्वयं विनाश के लिए अभिशप्त है... हमेशा के लिए।",
    zh_title: "Xié'è de huǐmiè",
    zh_content: "Xié'è běnshēn zhùdìng yào bèi huǐmiè... yǒngyuǎn."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ANNIHILATION OF EVIL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->ANNIHILATION OF EVIL"
RETURN t, parent;
```
