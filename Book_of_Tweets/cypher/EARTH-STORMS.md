---
name: "thought.EARTH STORMS"
alias: "Thought: Earth Storms"
type: THOUGHT
en_content: "Earth has about 16 million storms per year...God is Great!"
parent: "topic.CREATION"
tags:
- creation
- earth
- storms
- power
- majesty
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011a)
CREATE (t:THOUGHT {
    name: "thought.EARTH STORMS",
    alias: "Thought: Earth Storms",
    parent: "topic.CREATION",
    tags: ['creation', 'earth', 'storms', 'power', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EARTH STORMS",
    en_title: "Earth Storms",
    en_content: "Earth has about 16 million storms per year...God is Great!",
    es_title: "Tormentas Terrestres",
    es_content: "La Tierra tiene aproximadamente 16 millones de tormentas por año...¡Dios es Grande!",
    fr_title: "Tempêtes Terrestres",
    fr_content: "La Terre a environ 16 millions de tempêtes par an...Dieu est Grand !",
    hi_title: "पृथ्वी के तूफान",
    hi_content: "पृथ्वी पर प्रतिवर्ष लगभग 1.6 करोड़ तूफान आते हैं...परमेश्वर महान है!",
    zh_title: "Dìqiú Fēngbào",
    zh_content: "Dìqiú měinián dàyuē yǒu 1600 wàn cì fēngbào...Shàngdì shì wěidà de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EARTH STORMS" AND c.name = "content.EARTH STORMS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EARTH STORMS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.EARTH STORMS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >EARTH STORMS" }]->(child);
```
