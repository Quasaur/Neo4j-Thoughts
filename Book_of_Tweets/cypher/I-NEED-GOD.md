---
name: "thought.I NEED GOD"
alias: "Thought: I Need God"
type: THOUGHT
en_content: "Revelation 20:11, 12: I don't need a universe to exist; I just need God."
parent: "topic.SPIRITUALITY"
tags:
- existence
- spirituality
- god
- eternity
- presence
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011c)
CREATE (t:THOUGHT {
    name: "thought.I NEED GOD",
    alias: "Thought: I Need God",
    parent: "topic.SPIRITUALITY",
    tags: ['existence', 'spirituality', 'god', 'eternity', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.I NEED GOD",
    en_title: "I Need God",
    en_content: "Revelation 20:11, 12: I don't need a universe to exist; I just need God.",
    es_title: "Necesito a Dios",
    es_content: "Apocalipsis 20:11, 12: No necesito que exista un universo; solo necesito a Dios.",
    fr_title: "J'ai Besoin de Dieu",
    fr_content: "Apocalypse 20:11, 12: Je n'ai pas besoin qu'un univers existe; j'ai juste besoin de Dieu.",
    hi_title: "मुझे परमेश्वर की आवश्यकता है",
    hi_content: "प्रकाशितवाक्य 20:11, 12: मुझे ब्रह्मांड के अस्तित्व की आवश्यकता नहीं है; मुझे केवल परमेश्वर की आवश्यकता है।",
    zh_title: "Wo Xuyao Shen",
    zh_content: "Qishi Lu 20:11, 12: Wo bu xuyao yizou yuchou cai cunzai; wo zhi xuyao Shen."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.I NEED GOD" AND c.name = "content.I NEED GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.I NEED GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.I NEED GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >I NEED GOD" }]->(child);
```
