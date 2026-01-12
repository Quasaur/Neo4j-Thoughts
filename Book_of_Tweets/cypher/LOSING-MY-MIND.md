---
name: "thought.LOSING MY MIND"
alias: "Thought: Losing My Mind"
type: THOUGHT
en_content: "I was insane until I lost my mind!"
parent: "topic.PSYCHOLOGY"
tags:
- insanity
- mind
- psychology
- paradox
- clarity
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.LOSING MY MIND",
    alias: "Thought: Losing My Mind",
    parent: "topic.PSYCHOLOGY",
    tags: ['insanity', 'mind', 'psychology', 'paradox', 'clarity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOSING MY MIND",
    en_title: "Losing My Mind",
    en_content: "I was insane until I lost my mind!",
    es_title: "Perdiendo Mi Mente",
    es_content: "¡Estaba loco hasta que perdí mi mente!",
    fr_title: "Perdre Mon Esprit",
    fr_content: "J'étais fou jusqu'à ce que je perde mon esprit !",
    hi_title: "अपना मन खोना",
    hi_content: "मैं तब तक पागल था जब तक मैंने अपना मन नहीं खोया!",
    zh_title: "Shi Qu Wo De Li Zhi",
    zh_content: "Zhi dao wo shi qu le li zhi, wo cai fa xian zi ji yi zhi dou shi feng kuang de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOSING MY MIND" AND c.name = "content.LOSING MY MIND"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOSING MY MIND" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LOSING MY MIND"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >LOSING MY MIND" }]->(child);
```
