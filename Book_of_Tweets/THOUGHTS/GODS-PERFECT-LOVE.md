---
name: "thought.GODS PERFECT LOVE"
alias: "Thought: Gods Perfect Love"
type: THOUGHT
en_content: "God loves us with ALL His Heart, Soul, Mind and Strength!"
parent: "topic.THE GODHEAD"
tags:
- love
- god
- devotion
- majesty
- heart
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012c)
CREATE (t:THOUGHT {
    name: "thought.GODS PERFECT LOVE",
    alias: "Thought: Gods Perfect Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'god', 'devotion', 'majesty', 'heart'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS PERFECT LOVE",
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

MATCH (t:THOUGHT {name: "thought.GODS PERFECT LOVE"})
MATCH (c:CONTENT {name: "content.GODS PERFECT LOVE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS PERFECT LOVE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GODS PERFECT LOVE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GODS PERFECT LOVE" }]->(child);
```
