---
type: THOUGHT
name: "thought.DESTROYING OUR PLANET"
alias: "Thought: Destroying Our Planet"
parent: "topic.MORALITY"
en_content: "Our technology, industry and greed are destroying our planet."
tags: ["technology", "greed", "environment", "planet", "destruction"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013b)
CREATE (t:THOUGHT {    name: "thought.DESTROYING OUR PLANET",
    alias: "Thought: Destroying Our Planet",
    parent: "topic.MORALITY",
    tags: ['technology', 'greed', 'environment', 'planet', 'destruction'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.DESTROYING OUR PLANET",
    ctype: "THOUGHT",
    en_title: "Destroying Our Planet",
    en_content: "Our technology, industry and greed are destroying our planet.",
    es_title: "Destruyendo Nuestro Planeta",
    es_content: "Nuestra tecnología, industria y codicia están destruyendo nuestro planeta.",
    fr_title: "Détruire Notre Planète",
    fr_content: "Notre technologie, notre industrie et notre cupidité détruisent notre planète.",
    hi_title: "हमारे ग्रह का विनाश",
    hi_content: "हमारी तकनीक, उद्योग और लालच हमारे ग्रह को नष्ट कर रहे हैं।",
    zh_title: "Cuīhuǐ Wǒmen de Xīngqiú",
    zh_content: "Wǒmen de jìshù, gōngyè hé tānlán zhèngzài cuīhuǐ wǒmen de xīngqiú."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DESTROYING OUR PLANET"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->DESTROYING OUR PLANET"
RETURN t, parent;
```
