---
type: THOUGHT
name: "thought.HOLY-SPIRIT"
alias: "Thought: The Holy Spirit"
parent: "topic.THE GODHEAD"
en_content: "The Holy Spirit is God, and all men must be filled with Him."
tags: ["holy_spirit", "deity", "god", "fullness", "filling"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HOLY-SPIRIT",
    alias: "Thought: The Holy Spirit",
    parent: "topic.THE GODHEAD",
    tags: ["holy_spirit", "deity", "god", "fullness", "filling"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE HOLY SPIRIT",
    ctype: "THOUGHT",
    en_title: "The Holy Spirit",
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
WHERE t.name = "thought.HOLY-SPIRIT" AND c.name = "content.THE HOLY SPIRIT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HOLY-SPIRIT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.HOLY-SPIRIT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->HOLY-SPIRIT"}]->(child);
```
