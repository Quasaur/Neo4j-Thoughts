---
type: THOUGHT
name: "thought.GLORY TO GOD"
alias: "Thought: Glory to God"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "Whether by Righteousness or Wickedness, we all exist to glorify God!"
tags: ["the_glory_of_god", "splendor", "purpose", "existence", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GLORY TO GOD",
    alias: "Thought: Glory to God",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["the_glory_of_god", "splendor", "purpose", "existence", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLORY TO GOD",
    ctype: "THOUGHT",
    en_title: "Glory to God",
    en_content: "Whether by Righteousness or Wickedness, we all exist to glorify God!",
    es_title: "GLORIA A DIOS",
    es_content: "Ya sea por Justicia o por Maldad, ¡todos existimos para glorificar a Dios!",
    fr_title: "GLOIRE À DIEU",
    fr_content: "Que ce soit par la justice ou par la méchanceté, nous existons tous pour glorifier Dieu !",
    hi_title: "भगवान की जय",
    hi_content: "चाहे धार्मिकता से या दुष्टता से, हम सभी परमेश्वर की महिमा करने के लिए मौजूद हैं!",
    zh_title: "róng yào guī yú shén",
    zh_content: "wú lùn shì zhèng yì hái shì xié è ， wǒ men de cún zài dōu shì wèi le róng yào shàng dì ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GLORY TO GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->GLORY TO GOD"
RETURN t, parent;
```
