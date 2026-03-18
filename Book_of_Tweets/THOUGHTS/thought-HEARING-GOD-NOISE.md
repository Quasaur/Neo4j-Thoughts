---
type: THOUGHT
name: "thought.HEARING GOD NOISE"
alias: "Thought: Hearing God Noise"
parent: "topic.SPIRITUALITY"
en_content: "We cannot hear God through the noise of our own desire."
tags: ["spirituality", "desire", "listening", "prayer", "silence"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011a)
CREATE (t:THOUGHT {    name: "thought.HEARING GOD NOISE",
    alias: "Thought: Hearing God Noise",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'desire', 'listening', 'prayer', 'silence'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.HEARING GOD NOISE",
    ctype: "THOUGHT",
    en_title: "Hearing God Noise",
    en_content: "We cannot hear God through the noise of our own desire.",
    es_title: "Escuchar a Dios a Través del Ruido",
    es_content: "No podemos escuchar a Dios a través del ruido de nuestro propio deseo.",
    fr_title: "Entendre Dieu à Travers le Bruit",
    fr_content: "Nous ne pouvons pas entendre Dieu à travers le bruit de notre propre désir.",
    hi_title: "शोर के बीच परमेश्वर को सुनना",
    hi_content: "हम अपनी स्वयं की इच्छाओं के शोर के बीच परमेश्वर को नहीं सुन सकते।",
    zh_title: "Zàoyīn zhōng tīng shàngdì  zào yīn zhōng tīng shàng dì",
    zh_content: "Wǒmen wúfǎ tòuguò zìjǐ yùwàng de zàoyīn tīngdào shàngdì de shēngyīn.  wǒ men wú fǎ tòu guò zì jǐ yù wàng de zào yīn tīng dào shàng dì de shēng yīn 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEARING GOD NOISE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->HEARING GOD NOISE"
RETURN t, parent;
```
