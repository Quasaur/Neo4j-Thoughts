---
name: "thought.SPIRIT TRANSFORMING ENERGY"
alias: "Thought: Spirit Transforming Energy"
type: THOUGHT
en_content: "SPIRIT is so powerful; He can take frozen energy and transform it into Living Energy!"
parent: "topic.THE GODHEAD"
tags:
- spirit
- energy
- transformation
- power
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT TRANSFORMING ENERGY",
    alias: "Thought: Spirit Transforming Energy",
    parent: "topic.THE GODHEAD",
    tags: ['spirit', 'energy', 'transformation', 'power', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SPIRIT TRANSFORMING ENERGY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRIT TRANSFORMING ENERGY" AND c.name = "content.SPIRIT TRANSFORMING ENERGY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT TRANSFORMING ENERGY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.SPIRIT TRANSFORMING ENERGY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >SPIRIT TRANSFORMING ENERGY" }]->(child);
```
