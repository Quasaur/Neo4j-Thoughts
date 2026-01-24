---
title: "Thought: MOTION"
draft: false
type: THOUGHT
mling: false
tags:
  - rest
  - sabbath
  - peace
  - contentment
  - fullness
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MOTION",
    alias: "Thought: Movement",
    parent: "topic.THE GODHEAD",
    tags: ["rest", "sabbath", "peace", "contentment", "fullness"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MOTION",
    en_title: "MOTION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MOTION" AND c.name = "content.MOTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.MOTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MOTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->MOTION"}]->(child);
```
