---
type: THOUGHT
name: "thought.WITTGENSTEIN DISCOVERY"
alias: "Thought: Wittgenstein Discovery"
parent: "topic.PHILOSOPHY"
en_content: "I have discovered Ludwig Josef Johann Wittgenstein."
tags: ["philosophy", "discovery", "wittgenstein", "logic", "thought"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jul-2010)
CREATE (t:THOUGHT {    name: "thought.WITTGENSTEIN DISCOVERY",
    alias: "Thought: Wittgenstein Discovery",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'discovery', 'wittgenstein', 'logic', 'thought'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.WITTGENSTEIN DISCOVERY",
    ctype: "THOUGHT",
    en_title: "Wittgenstein Discovery",
    en_content: "I have discovered Ludwig Josef Johann Wittgenstein.",
    es_title: "Descubrimiento de Wittgenstein",
    es_content: "He descubierto a Ludwig Wittgenstein.",
    fr_title: "Découverte de Wittgenstein",
    fr_content: "J'ai découvert Ludwig Wittgenstein.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "मैंने लुडविग विट्गेन्स्टाइन की खोज की।",
    zh_title: "Wéitègēnsītǎn fāxiàn",
    zh_content: "wǒ fā xiàn le wéi tè gēn sī tǎn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WITTGENSTEIN DISCOVERY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->WITTGENSTEIN DISCOVERY"
RETURN t, parent;
```
