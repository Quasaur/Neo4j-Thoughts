---
name: "thought.REVELATION ISRAELI CHURCH"
alias: "Thought: Revelation Israeli Church"
type: THOUGHT
en_content: "Revelation is not about the gentile church as much as the Israeli church. In this context, everything starts to make sense."
parent: "topic.RELIGION"
tags:
- revelation
- israel
- church
- bible
- history
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2013)
CREATE (t:THOUGHT {
    name: "thought.REVELATION ISRAELI CHURCH",
    alias: "Thought: Revelation Israeli Church",
    parent: "topic.RELIGION",
    tags: ['revelation', 'israel', 'church', 'bible', 'history'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.REVELATION ISRAELI CHURCH",
    en_title: "Revelation Israeli Church",
    en_content: "Revelation is not about the gentile church as much as the Israeli church. In this context, everything starts to make sense.",
    es_title: "Apocalipsis Iglesia Israelí",
    es_content: "El Apocalipsis no trata tanto sobre la iglesia gentil como sobre la iglesia israelí. En este contexto, todo comienza a tener sentido.",
    fr_title: "Apocalypse Église Israélienne",
    fr_content: "L'Apocalypse ne concerne pas tant l'église des gentils que l'église israélienne. Dans ce contexte, tout commence à avoir du sens.",
    hi_title: "प्रकाशितवाक्य इस्राएली कलीसिया",
    hi_content: "प्रकाशितवाक्य अन्यजाति कलीसिया के बारे में उतना नहीं है जितना कि इस्राएली कलीसिया के बारे में है। इस संदर्भ में, सब कुछ समझ में आने लगता है।",
    zh_title: "Qǐshìlù Yǐsèliè Jiàohuì",
    zh_content: "Qǐshìlù bùshì guānyú wàibāngrén jiàohuì, ér gèng duō de shì guānyú Yǐsèliè jiàohuì. Zài zhège bèijǐng xià, yīqiè dōu kāishǐ biàn de yǒu yìyì le."
});

MATCH (t:THOUGHT {name: "thought.REVELATION ISRAELI CHURCH"})
MATCH (c:CONTENT {name: "content.REVELATION ISRAELI CHURCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.REVELATION ISRAELI CHURCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.REVELATION ISRAELI CHURCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >REVELATION ISRAELI CHURCH" }]->(child);
```
