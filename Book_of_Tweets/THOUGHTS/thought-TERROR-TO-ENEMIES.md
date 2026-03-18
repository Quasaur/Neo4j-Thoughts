---
type: THOUGHT
name: "thought.TERROR TO ENEMIES"
alias: "Thought: Divine Justice"
parent: "topic.THE GODHEAD"
en_content: "God is only a Terror to His enemies."
tags: ["divine_wrath", "justice", "holiness", "judgment", "gods_enemies"]
ptopic:
level: 1
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.TERROR TO ENEMIES",
    alias: "Thought: Divine Justice",
    parent: "topic.THE GODHEAD",
    tags: ["divine_wrath", "justice", "holiness", "judgment", "gods_enemies"],
    level: 1});

CREATE (c:CONTENT {
    name: "content.TERROR TO ENEMIES",
    ctype: "THOUGHT",
    en_title: "Terror to Enemies",
    en_content: "God is only a Terror to His enemies.",
    es_title: "Terror para enemigos",
    es_content: "Dios es solo un Terror para sus enemigos.",
    fr_title: "Terreur des ennemis",
    fr_content: "Dieu n'est une Terreur que pour Ses ennemis.",
    hi_title: "dushmanon ko darr",
    hi_content: "ईश्वर केवल अपने शत्रुओं के लिए ही भयंकर है।",
    zh_title: "kǒng bù dírén",
    zh_content: "shàng dì zhǐ shì tā dírén de kǒng bù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TERROR TO ENEMIES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->TERROR TO ENEMIES"
RETURN t, parent;
```
