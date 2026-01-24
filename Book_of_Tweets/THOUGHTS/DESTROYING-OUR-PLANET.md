---
name: "thought.DESTROYING OUR PLANET"
alias: "Thought: Destroying Our Planet"
type: THOUGHT
en_content: "Our technology, industry and greed are destroying our planet."
parent: "topic.MORALITY"
tags:
- technology
- greed
- environment
- planet
- destruction
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.DESTROYING OUR PLANET",
    alias: "Thought: Destroying Our Planet",
    parent: "topic.MORALITY",
    tags: ['technology', 'greed', 'environment', 'planet', 'destruction'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DESTROYING OUR PLANET",
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

MATCH (t:THOUGHT {name: "thought.DESTROYING OUR PLANET"})
MATCH (c:CONTENT {name: "content.DESTROYING OUR PLANET"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DESTROYING OUR PLANET" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.DESTROYING OUR PLANET"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->DESTROYING OUR PLANET" }]->(child);
```
