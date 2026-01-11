---
title: "Thought: GOD AWARENESS"
draft: false
type: THOUGHT
mling: false
tags:
  - faith
  - awareness
  - self
  - god
  - worship
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GOD_AWARENESS",
    alias: "Thought: GOD AWARENESS",
    parent: "topic.THE-GODHEAD",
    tags: ["faith", "awareness", "self", "god", "worship"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD_AWARENESS",
    en_title: "GOD AWARENESS",
    en_content: "Self-awareness is the second most precious gift God has given us; the first is God-awareness!",
    es_title: "CONCIENCIA DE DIOS",
    es_content: "La autoconciencia es el segundo regalo más preciado que Dios nos ha dado; ¡El primero es la conciencia de Dios!",
    fr_title: "SENSIBILISATION À DIEU",
    fr_content: "La conscience de soi est le deuxième don le plus précieux que Dieu nous a fait ; le premier est la conscience de Dieu !",
    hi_title: "ईश्वर जागरूकता",
    hi_content: "आत्म-जागरूकता ईश्वर द्वारा हमें दिया गया दूसरा सबसे कीमती उपहार है; पहला है ईश्वर-जागरूकता!",
    zh_title: "shàng dì yì shí",
    zh_content: "zì wǒ yì shí shì shàng dì cì yǔ wǒ men de dì èr jiàn zuì zhēn guì de lǐ wù 。 dì yí gè shì shén de yì shí ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD_AWARENESS" AND c.name = "content.GOD_AWARENESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.GOD_AWARENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GODHEAD" AND child.name = "thought.GOD_AWARENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GODHEAD->GOD_AWARENESS"}]->(child);
```
