---
type: THOUGHT
name: "thought.EARTH STORMS"
alias: "Thought: Earth Storms"
parent: "topic.ASTROPHYSICS"
en_content: "Earth has about 16 million storms per year...God is Great!"
tags: ["creation", "earth", "storms", "power", "majesty"]
ptopic: "[[topic-ASTROPHYSICS]]"
level: 5
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.EARTH STORMS",
    alias: "Thought: Earth Storms",
    parent: "topic.ASTROPHYSICS",
    tags: ['creation', 'earth', 'storms', 'power', 'majesty'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.EARTH STORMS",
    ctype: "THOUGHT",
    en_title: "Thought: Earth Storms",
    en_content: "Earth has about 16 million storms per year...God is Great!",
    es_title: "Pensamiento: Tormentas terrestres",
    es_content: "La Tierra tiene aproximadamente 16 millones de tormentas por año...¡Dios es Grande!",
    fr_title: "Pensée : Tempêtes terrestres",
    fr_content: "La Terre a environ 16 millions de tempêtes par an...Dieu est Grand !",
    hi_title: "विचार: पृथ्वी तूफान",
    hi_content: "पृथ्वी पर प्रतिवर्ष लगभग 1.6 करोड़ तूफान आते हैं...परमेश्वर महान है!",
    zh_title: "sī xiǎng : dì qiú fēng bào",
    zh_content: "Dìqiú měinián dàyuē yǒu 1600 wàn cì fēngbào...Shàngdì shì wěidà de!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EARTH STORMS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ASTROPHYSICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ASTROPHYSICS->EARTH STORMS"
RETURN t, parent;
```
