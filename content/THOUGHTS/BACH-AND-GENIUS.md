---
name: "thought.BACH AND GENIUS"
alias: "Thought: Gift of Genius"
type: THOUGHT
tags:
  - bach
  - genius
  - music
  - gift
  - transcendence
en_content: Johann Sebastian Bach is one of those rare souls whose gifts transcend all genius!
parent: topic.MUSIC
level: 5
neo4j: true
ptopic: '"[[topic-MUSIC]]"'
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.BACH AND GENIUS",
    alias: "Thought: BACH AND GENIUS",
    parent: "topic.MUSIC",
    tags: ["bach", "genius", "music", "gift", "transcendence"],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.BACH AND GENIUS",
    en_title: "BACH AND GENIUS",
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

MATCH (t:THOUGHT {name: "thought.BACH AND GENIUS"})
MATCH (c:CONTENT {name: "content.BACH AND GENIUS"})
MERGE (t)-[:HAS_CONTENT {name: "edge.BACH AND GENIUS"}]->(c);

MATCH (parent:TOPIC {name: "topic.MUSIC"})
MATCH (child:THOUGHT {name: "thought.BACH AND GENIUS"})
MERGE (parent)-[:HAS_THOUGHT {name: "edge.MUSIC >BACH AND GENIUS"}]->(child);
```
