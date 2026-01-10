---
name: thought.BACH AND GENIUS
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
ptopic: '"[[topic-MUSICOLOGY]]"'
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.BACH AND GENIUS",
    alias: "Thought: BACH AND GENIUS",
    parent: "topic.MUSIC",
    tags: ["bach", "genius", "music", "gift", "transcendence"],
    notes: "",
    level: 6
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
    hi_content: "जोहान सेबस्टियन बाख उन दुर्लभ आत्माओं में से एक हैं जिनका उपहार सभी प्रतिभाओं से परे है!"
    zh_title: "bā hè hé tiān cái",
    zh_content: "yuē hàn · sāi bā sī dì àn · bā hè shì nà xiē fēi fán de líng hún zhī yī ， tā de tiān fù chāo yuè le suǒ yǒu de tiān cái ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BACH AND GENIUS" AND c.name = "content.BACH AND GENIUS"
MERGE (t)-[:HAS_CONTENT {name: "edge.BACH AND GENIUS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MUSIC" AND child.name = "thought.BACH AND GENIUS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.MUSIC >BACH AND GENIUS"}]->(child);
```
