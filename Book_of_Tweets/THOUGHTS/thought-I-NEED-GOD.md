---
type: THOUGHT
name: "thought.I NEED GOD"
alias: "Thought: I Need God"
parent: "topic.SPIRITUALITY"
en_content: "Revelation 20:11, 12: I don't need a universe to exist; I just need God."
tags: ["existence", "spirituality", "god", "eternity", "presence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011c)
CREATE (t:THOUGHT {    name: "thought.I NEED GOD",
    alias: "Thought: I Need God",
    parent: "topic.SPIRITUALITY",
    tags: ['existence', 'spirituality', 'god', 'eternity', 'presence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.I NEED GOD",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.I NEED GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->I NEED GOD"
RETURN t, parent;
```
