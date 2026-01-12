---
name: "thought.TERROR TO ENEMIES"
alias: "Thought: Divine Justice"
en_content: "God is only a Terror to His enemies."
parent: topic.THE GODHEAD
tags:
  - divine_wrath
  - justice
  - holiness
  - judgment
  - gods_enemies
level: 1
neo4j: false
ptopic: 
type: THOUGHT
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TERROR TO ENEMIES",
    alias: "Thought: Divine Justice",
    parent: "topic.THE GODHEAD",
    tags: ["divine_wrath", "justice", "holiness", "judgment", "gods_enemies"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.TERROR TO ENEMIES",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TERROR TO ENEMIES" AND c.name = "content.TERROR TO ENEMIES"
MERGE (t)-[:HAS_CONTENT {name: "edge.TERROR TO ENEMIES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.TERROR TO ENEMIES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD >TERROR TO ENEMIES"}]->(child);
```
