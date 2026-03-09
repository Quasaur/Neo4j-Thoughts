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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GLORY TO GOD" AND c.name = "content.GLORY TO GOD"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GLORY TO GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.GLORY TO GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->GLORY TO GOD"}]->(child);
```
