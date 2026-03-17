---
type: THOUGHT
name: "thought.MOTION"
alias: "Thought: Movement"
en_content: |
  Everything that exists is MOVING…
  …except God. Even when He MOVES, God is at REST
  …GLORY!!!!!!!!!!!!!!!!!!!!"
tags: ["rest", "sabbath", "peace", "contentment", "fullness"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MOTION",
    alias: "Thought: Movement",
    parent: "topic.THE GODHEAD",
    tags: ["rest", "sabbath", "peace", "contentment", "fullness"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MOTION",
    ctype: "THOUGHT",
    en_title: "Motion",
    en_content: "Everything that exists is MOVING…
…except God. Even when He MOVES, God is at REST
…GLORY!!!!!!!!!!!!!!!!!!!!",
    es_title: "MOVIMIENTO",
    es_content: "Todo lo que existe se MUEVE...
...excepto Dios. Incluso cuando Él SE MUEVE, Dios está en DESCANSO
…¡¡¡GLORIA!!!!!!!!!!!!!!!!!!!!",
    fr_title: "MOUVEMENT",
    fr_content: "Tout ce qui existe bouge…
…sauf Dieu. Même quand Il BOUGE, Dieu est au REPOS
…GLOIRE!!!!!!!!!!!!!!!!!!!!",
    hi_title: "गति",
    hi_content: "जो कुछ भी अस्तित्व में है वह गतिमान है...
...भगवान को छोड़कर. जब वह चलता है, तब भी भगवान विश्राम में होता है
...महिमा!!!!!!!!!!!!!!!!!!",
    zh_title: "yùn dòng",
    zh_content: "cún zài de yī qiè dōu zài yí dòng ……
…… chú le shàng dì 。 jí shǐ dāng tā yí dòng shí ， shàng dì yě shì jìng zhǐ de 
… róng yào !!!!!!!!!!!!!!!!!!!!!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MOTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->MOTION"
RETURN t, parent;
```
