---
name: "thought.SUNS ENERGY CORE"
alias: "Thought: Suns Energy Core"
type: THOUGHT
en_content: "Energy generated in the Sun's core takes a million years to reach its surface: God is great!"
parent: "topic.ASTROPHYSICS"
tags:
- science
- sun
- energy
- creation
- time
level: 5
neo4j: true
ptopic: "[[topic-ASTROPHYSICS]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.SUNS ENERGY CORE",
    alias: "Thought: Suns Energy Core",
    parent: "topic.CREATION",
    tags: ['science', 'sun', 'energy', 'creation', 'time'],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.SUNS ENERGY CORE",
    en_title: "Suns Energy Core",
    en_content: "Energy generated in the Sun's core takes a million years to reach its surface: God is great!",
    es_title: "El Núcleo Energético del Sol",
    es_content: "La energía generada en el núcleo del Sol tarda un millón de años en llegar a su superficie: ¡Dios es grande!",
    fr_title: "Le Noyau Énergétique du Soleil",
    fr_content: "L'énergie générée dans le noyau du Soleil met un million d'années à atteindre sa surface : Dieu est grand !",
    hi_title: "सूर्य की ऊर्जा केंद्र",
    hi_content: "सूर्य के केंद्र में उत्पन्न ऊर्जा को उसकी सतह तक पहुंचने में एक मिलियन वर्ष लगते हैं: परमेश्वर महान है!",
    zh_title: "Tàiyáng néngliàng héxīn 太阳能量核心",
    zh_content: "Tàiyáng héxīn zhōng chǎnshēng de néngliàng xūyào yī bǎi wàn nián cái néng dàodá qi biǎomiàn: Shàngdì zhēn wěidà! 太阳核心中产生的能量需要一百万年才能到达其表面：上帝真伟大！"
});

MATCH (t:THOUGHT {name: "thought.SUNS ENERGY CORE"})
MATCH (c:CONTENT {name: "content.SUNS ENERGY CORE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUNS ENERGY CORE" }]->(c);

MATCH (parent:TOPIC {name: "topic.ASTROPHYSICS"})
MATCH (child:THOUGHT {name: "thought.SUNS ENERGY CORE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "ASTROPHYSICS->SUNS ENERGY CORE" }]->(child);
```
