---
type: THOUGHT
name: "thought.SPIRIT TRANSFORMING ENERGY"
alias: "Thought: Spirit Transforming Energy"
parent: "topic.THE GODHEAD"
en_content: "SPIRIT is so powerful; He can take frozen energy and transform it into Living Energy!"
tags: ["spirit", "energy", "transformation", "power", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013b)
CREATE (t:THOUGHT {    name: "thought.SPIRIT TRANSFORMING ENERGY",
    alias: "Thought: Spirit Transforming Energy",
    parent: "topic.THE GODHEAD",
    tags: ['spirit', 'energy', 'transformation', 'power', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.SPIRIT TRANSFORMING ENERGY",
    ctype: "THOUGHT",
    en_title: "Spirit Transforming Energy",
    en_content: "SPIRIT is so powerful; He can take frozen energy and transform it into Living Energy!",
    es_title: "Energía Transformadora del Espíritu",
    es_content: "¡El ESPÍRITU es tan poderoso; Él puede tomar energía congelada y transformarla en Energía Viviente!",
    fr_title: "Énergie Transformatrice de l'Esprit",
    fr_content: "L'ESPRIT est si puissant ; Il peut prendre l'énergie figée et la transformer en Énergie Vivante !",
    hi_title: "आत्मा की परिवर्तनकारी शक्ति",
    hi_content: "आत्मा इतनी शक्तिशाली है; वह जमी हुई ऊर्जा को लेकर उसे जीवित ऊर्जा में बदल सकती है!",
    zh_title: "Shèng Líng Biàn Huà Néng Liàng",
    zh_content: "SHÈNG LÍNG rú cǐ qiáng dà; Tā kě yǐ jiāng dòng jié de néng liàng zhuǎn huà wéi Shēng Mìng Néng Liàng!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SPIRIT TRANSFORMING ENERGY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->SPIRIT TRANSFORMING ENERGY"
RETURN t, parent;
```
