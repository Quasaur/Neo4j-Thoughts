---
type: THOUGHT
name: "thought.APOSTLES AS VISION"
alias: "Thought: Apostles As Vision"
parent: "topic.RELIGION"
en_content: "The Apostles loved Jesus' Vision because the Apostles WERE Jesus' Vision!"
tags: ["apostles", "vision", "jesus", "church", "history"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Oct-2012)
CREATE (t:THOUGHT {    name: "thought.APOSTLES AS VISION",
    alias: "Thought: Apostles As Vision",
    parent: "topic.RELIGION",
    tags: ['apostles', 'vision', 'jesus', 'church', 'history'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.APOSTLES AS VISION",
    ctype: "THOUGHT",
    en_title: "Apostles As Vision",
    en_content: "The Apostles loved Jesus' Vision because the Apostles WERE Jesus' Vision!",
    es_title: "Los Apóstoles como Visión",
    es_content: "¡Los Apóstoles amaban la Visión de Jesús porque los Apóstoles ERAN la Visión de Jesús!",
    fr_title: "Les Apôtres comme Vision",
    fr_content: "Les Apôtres aimaient la Vision de Jésus parce que les Apôtres ÉTAIENT la Vision de Jésus !",
    hi_title: "दृष्टि के रूप में प्रेरित",
    hi_content: "प्रेरितों ने यीशु की दृष्टि से प्यार किया क्योंकि प्रेरित यीशु की दृष्टि थे!",
    zh_title: "Shǐtú zuòwéi yìxiàng",
    zh_content: "Shǐtúmen rè'ài yēsū de yìxiàng, yīnwèi shǐtúmen jiùshì yēsū de yìxiàng!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.APOSTLES AS VISION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->APOSTLES AS VISION"
RETURN t, parent;
```
