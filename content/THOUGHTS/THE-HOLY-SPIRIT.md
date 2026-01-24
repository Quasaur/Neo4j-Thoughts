---
title: "Thought: THE HOLY SPIRIT"
draft: false
type: THOUGHT
mling: false
tags:
  - holy_spirit
  - deity
  - god
  - fullness
  - filling
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_HOLY_SPIRIT",
    alias: "Thought: THE HOLY SPIRIT",
    parent: "topic.THE-GODHEAD",
    tags: ["holy_spirit", "deity", "god", "fullness", "filling"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE_HOLY_SPIRIT",
    en_title: "THE HOLY SPIRIT",
    en_content: "The Holy Spirit is God, and all men must be filled with Him.",
    es_title: "EL ESPÍRITU SANTO",
    es_content: "El Espíritu Santo es Dios y todos los hombres deben ser llenos de Él.",
    fr_title: "LE SAINT-ESPRIT",
    fr_content: "Le Saint-Esprit est Dieu et tous les hommes doivent être remplis de Lui.",
    hi_title: "पवित्र आत्मा",
    hi_content: "पवित्र आत्मा परमेश्वर है, और सभी मनुष्यों को उससे भरा होना चाहिए।",
    zh_title: "shèng líng",
    zh_content: "shèng líng shì shén ， suǒ yǒu rén dōu bì xū bèi tā chōng mǎn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_HOLY_SPIRIT" AND c.name = "content.THE_HOLY_SPIRIT"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_HOLY_SPIRIT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GODHEAD" AND child.name = "thought.THE_HOLY_SPIRIT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GODHEAD->THE_HOLY_SPIRIT"}]->(child);
```
