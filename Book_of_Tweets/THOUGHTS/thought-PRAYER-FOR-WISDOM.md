---
type: THOUGHT
name: "thought.PRAYER FOR WISDOM"
alias: "Thought: Prayer For Wisdom"
parent: "topic.SPIRITUALITY"
en_content: "Lord Jesus, fill my mind with Your Wisdom; fill my heart with Your Love; fill my bowels with Your Mercy!"
tags: ["prayer", "wisdom", "love", "mercy", "jesus"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Nov-2011)
CREATE (t:THOUGHT {    name: "thought.PRAYER FOR WISDOM",
    alias: "Thought: Prayer For Wisdom",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'wisdom', 'love', 'mercy', 'jesus'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.PRAYER FOR WISDOM",
    ctype: "THOUGHT",
    en_title: "Prayer For Wisdom",
    en_content: "Lord Jesus, fill my mind with Your Wisdom; fill my heart with Your Love; fill my bowels with Your Mercy!",
    es_title: "Oración Por Sabiduría",
    es_content: "¡Señor Jesús, llena mi mente con Tu Sabiduría; llena mi corazón con Tu Amor; llena mis entrañas con Tu Misericordia!",
    fr_title: "Prière Pour La Sagesse",
    fr_content: "Seigneur Jésus, remplis mon esprit de Ta Sagesse; remplis mon cœur de Ton Amour; remplis mes entrailles de Ta Miséricorde!",
    hi_title: "बुद्धि के लिए प्रार्थना",
    hi_content: "प्रभु यीशु, मेरे मन को अपनी बुद्धि से भर दें; मेरे हृदय को अपने प्रेम से भर दें; मेरी अंतड़ियों को अपनी दया से भर दें!",
    zh_title: "Qiú Zhìhuì De Qídǎo",
    zh_content: "Zhǔ Yēsū, qǐng yòng Nǐ de Zhìhuì chōngmǎn wǒ de xīnlíng; yòng Nǐ de Ài chōngmǎn wǒ de xīn; yòng Nǐ de Císhàn chōngmǎn wǒ de féicháng!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRAYER FOR WISDOM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->PRAYER FOR WISDOM"
RETURN t, parent;
```
