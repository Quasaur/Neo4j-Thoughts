---
type: THOUGHT
name: "thought.GODS PERFECT LOVE"
alias: "Thought: Gods Perfect Love"
parent: "topic.THE GODHEAD"
en_content: "God loves us with ALL His Heart, Soul, Mind and Strength!"
tags: ["love", "god", "devotion", "majesty", "heart"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012c)
CREATE (t:THOUGHT {    name: "thought.GODS PERFECT LOVE",
    alias: "Thought: Gods Perfect Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'god', 'devotion', 'majesty', 'heart'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GODS PERFECT LOVE",
    ctype: "THOUGHT",
    en_title: "Gods Perfect Love",
    en_content: "God loves us with ALL His Heart, Soul, Mind and Strength!",
    es_title: "El Amor Perfecto de Dios",
    es_content: "¡Dios nos ama con TODO Su Corazón, Alma, Mente y Fuerza!",
    fr_title: "L'Amour Parfait de Dieu",
    fr_content: "Dieu nous aime de tout Son Cœur, Son Âme, Son Esprit et Sa Force !",
    hi_title: "परमेश्वर का सिद्ध प्रेम",
    hi_content: "परमेश्वर हमसे अपने सारे हृदय, आत्मा, मन और शक्ति से प्रेम करता है!",
    zh_title: "Shén de Wánměi Zhī Ài",
    zh_content: "Shén yòng Tā quánbù de Xīn, Línghún, Yìniàn hé Lìliàng ài wǒmen!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GODS PERFECT LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GODS PERFECT LOVE"
RETURN t, parent;
```
