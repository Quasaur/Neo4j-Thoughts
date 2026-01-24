---
name: "thought.GLORY_TO_GOD"
alias: "Thought: GLORY TO GOD"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- thegloryofgod
- splendor
- purpose
- existence
- sovereignty
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GLORY_TO_GOD",
    alias: "Thought: GLORY TO GOD",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["thegloryofgod", "splendor", "purpose", "existence", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLORY_TO_GOD",
    en_title: "GLORY TO GOD",
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
WHERE t.name = "thought.GLORY_TO_GOD" AND c.name = "content.GLORY_TO_GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.GLORY_TO_GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.GLORY_TO_GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->GLORY_TO_GOD"}]->(child);
```
