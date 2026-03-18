---
type: THOUGHT
name: "thought.LOSING MY MIND"
alias: "Thought: Losing My Mind"
parent: "topic.PSYCHOLOGY"
en_content: "I was insane until I lost my mind!"
tags: ["insanity", "mind", "psychology", "paradox", "clarity"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011a)
CREATE (t:THOUGHT {    name: "thought.LOSING MY MIND",
    alias: "Thought: Losing My Mind",
    parent: "topic.PSYCHOLOGY",
    tags: ['insanity', 'mind', 'psychology', 'paradox', 'clarity'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.LOSING MY MIND",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOSING MY MIND"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->LOSING MY MIND"
RETURN t, parent;
```
