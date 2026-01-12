---
name: "thought.PRAYER FOR WISDOM"
alias: "Thought: Prayer For Wisdom"
type: THOUGHT
en_content: "Lord Jesus, fill my mind with Your Wisdom; fill my heart with Your Love; fill my bowels with Your Mercy!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- wisdom
- love
- mercy
- jesus
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.PRAYER FOR WISDOM",
    alias: "Thought: Prayer For Wisdom",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'wisdom', 'love', 'mercy', 'jesus'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER FOR WISDOM",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRAYER FOR WISDOM" AND c.name = "content.PRAYER FOR WISDOM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER FOR WISDOM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER FOR WISDOM"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER FOR WISDOM" }]->(child);
```
