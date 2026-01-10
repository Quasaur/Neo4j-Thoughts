---
name: "thought.WITTGENSTEIN DISCOVERY"
alias: "Thought: Wittgenstein Discovery"
type: THOUGHT
en_content: "I have discovered Ludwig Josef Johann Wittgenstein."
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- discovery
- wittgenstein
- logic
- thought
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.WITTGENSTEIN DISCOVERY",
    alias: "Thought: Wittgenstein Discovery",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'discovery', 'wittgenstein', 'logic', 'thought'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WITTGENSTEIN DISCOVERY",
    en_title: "Wittgenstein Discovery",
    en_content: "I have discovered Ludwig Josef Johann Wittgenstein.",
    es_title: "Descubrimiento de Wittgenstein",
    es_content: "He descubierto a Ludwig Wittgenstein.",
    fr_title: "Découverte de Wittgenstein",
    fr_content: "J'ai découvert Ludwig Wittgenstein.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "मैंने लुडविग विट्गेन्स्टाइन की खोज की।",
    zh_title: "wéi tè gēn sī tǎn",
    zh_content: "wǒ fā xiàn le wéi tè gēn sī tǎn."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WITTGENSTEIN DISCOVERY" AND c.name = "content.WITTGENSTEIN DISCOVERY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WITTGENSTEIN DISCOVERY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.WITTGENSTEIN DISCOVERY"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >WITTGENSTEIN DISCOVERY" }]->(child);
```
