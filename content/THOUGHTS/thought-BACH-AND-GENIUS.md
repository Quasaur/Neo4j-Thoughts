---
type: THOUGHT
name: "thought.BACH AND GENIUS"
alias: "Thought: Gift of Genius"
parent: "topic.MUSIC"
en_content: "Johann Sebastian Bach is one of those rare souls whose gifts transcend all genius!"
tags: ["bach", "genius", "music", "gift", "transcendence"]
ptopic: "[[topic-MUSIC]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BACH AND GENIUS",
    alias: "Thought: Gift of Genius",
    parent: "topic.MUSIC",
    tags: ["bach", "genius", "music", "gift", "transcendence"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.BACH AND GENIUS",
    ctype: "THOUGHT",
    en_title: "Bach and Genius",
    en_content: "Johann Sebastian Bach is one of those rare souls whose gifts transcend all genius!",
    es_title: "BACH Y GENIO",
    es_content: "¡Johann Sebastian Bach es una de esas raras almas cuyos dones trascienden todo genio!",
    fr_title: "BACH ET GÉNIE",
    fr_content: "Johann Sebastian Bach est l'une de ces rares âmes dont les dons transcendent tout génie !",
    hi_title: "बाख और प्रतिभा",
    hi_content: "जोहान सेबस्टियन बाख उन दुर्लभ आत्माओं में से एक हैं जिनका उपहार सभी प्रतिभाओं से परे है!",
    zh_title: "Bāhè hé tiāncái 巴赫和天才",
    zh_content: "Yuēhàn · Sāibāsīdì'ān · Bāhè shì nàxiē fēifán de línghún zhī yī, tā de tiānfù chāoyuè le suǒyǒu de tiāncái! 约翰·塞巴斯蒂安·巴赫是那些非凡的灵魂之一，他的天赋超越了所有的天才！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BACH AND GENIUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MUSIC"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MUSIC->BACH AND GENIUS"
RETURN t, parent;
```
