---
name: "thought.UNITY IN CHRIST"
alias: "Thought: Unity In Christ"
type: THOUGHT
en_content: "True unity of spirit, soul, body, family, community and nation lies only in Jesus Christ."
parent: "topic.THE GODHEAD"
tags:
- unity
- jesus
- christ
- community
- connection
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.UNITY IN CHRIST",
    alias: "Thought: Unity In Christ",
    parent: "topic.THE GODHEAD",
    tags: ['unity', 'jesus', 'christ', 'community', 'connection'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.UNITY IN CHRIST",
    en_title: "Unity In Christ",
    en_content: "True unity of spirit, soul, body, family, community and nation lies only in Jesus Christ.",
    es_title: "Unidad En Cristo",
    es_content: "La verdadera unidad del espíritu, alma, cuerpo, familia, comunidad y nación reside únicamente en Jesucristo.",
    fr_title: "Unité En Christ",
    fr_content: "La véritable unité de l'esprit, de l'âme, du corps, de la famille, de la communauté et de la nation ne se trouve qu'en Jésus-Christ.",
    hi_title: "मसीह में एकता",
    hi_content: "आत्मा, प्राण, शरीर, परिवार, समुदाय और राष्ट्र की सच्ची एकता केवल यीशु मसीह में ही निहित है।",
    zh_title: "Zai Jidu Li De He Yi",
    zh_content: "Ling hun, shen ti, jia ting, she qu he guo jia de zhen zheng he yi zhi cun zai yu Ye Su Ji Du zhong."
});

MATCH (t:THOUGHT {name: "thought.UNITY IN CHRIST"})
MATCH (c:CONTENT {name: "content.UNITY IN CHRIST"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNITY IN CHRIST" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.UNITY IN CHRIST"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >UNITY IN CHRIST" }]->(child);
```
