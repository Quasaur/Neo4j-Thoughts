---
name: "thought.ANNIHILATION OF EVIL"
alias: "Thought: Annihilation Of Evil"
type: THOUGHT
en_content: "Evil itself is doomed to annihilation...forever."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- evil
- destruction
- sovereignty
- prophecy
- forever
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.ANNIHILATION OF EVIL",
    alias: "Thought: Annihilation Of Evil",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['evil', 'destruction', 'sovereignty', 'prophecy', 'forever'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ANNIHILATION OF EVIL",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANNIHILATION OF EVIL" AND c.name = "content.ANNIHILATION OF EVIL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ANNIHILATION OF EVIL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.ANNIHILATION OF EVIL"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >ANNIHILATION OF EVIL" }]->(child);
```
