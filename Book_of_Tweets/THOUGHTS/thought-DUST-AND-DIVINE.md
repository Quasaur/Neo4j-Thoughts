---
type: THOUGHT
name: "thought.DUST AND DIVINE"
alias: "Thought: Image of God"
parent: "topic.HUMANITY"
en_content: "We are dust...that look like God."
tags: ["humanity", "creation", "dust", "divine_image", "paradox"]
ptopic:
level: 3
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.DUST AND DIVINE",
    alias: "Thought: Image of God",
    parent: "topic.HUMANITY",
    tags: ["humanity", "creation", "dust", "divine_image", "paradox"],
    level: 3});

CREATE (c:CONTENT {
    name: "content.DUST AND DIVINE",
    ctype: "THOUGHT",
    en_title: "Dust and Divine",
    en_content: "We are dust...that look like God.",
    es_title: "Polvo y divino",
    es_content: "Somos polvo... que se parece a Dios.",
    fr_title: "Poussière et divin",
    fr_content: "Nous sommes de la poussière... qui ressemble à Dieu.",
    hi_title: "dhuool aur divy",
    hi_content: "हम धूल हैं... जो भगवान की तरह दिखते हैं।",
    zh_title: "Chén'āi yǔ shénshèng",
    zh_content: "wǒ men shì chén āi... què xiàng shàng dì."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DUST AND DIVINE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->DUST AND DIVINE"
RETURN t, parent;
```
