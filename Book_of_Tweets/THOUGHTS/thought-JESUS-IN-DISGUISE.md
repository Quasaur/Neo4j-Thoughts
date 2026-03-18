---
type: THOUGHT
name: "thought.JESUS IN DISGUISE"
alias: "Thought: Image of God"
parent: "topic.HUMANITY"
en_content: "\"Each person you meet is Jesus in disguise.\" -- Mother Teresa"
tags: ["humanity", "jesus", "empathy", "service", "neighbors"]
ptopic:
level: 3
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.JESUS IN DISGUISE",
    alias: "Thought: Image of God",
    parent: "topic.HUMANITY",
    tags: ["humanity", "jesus", "empathy", "service", "neighbors"],
    level: 3});

CREATE (c:CONTENT {
    name: "content.JESUS IN DISGUISE",
    ctype: "THOUGHT",
    en_title: "Jesus in Disguise",
    en_content: "\"Each person you meet is Jesus in disguise.\" -- Mother Teresa",
    es_title: "Jesús disfrazado",
    es_content: "\"Cada persona que conoces es Jesús disfrazado\". -- Madre Teresa",
    fr_title: "Jésus déguisé",
    fr_content: "\"Chaque personne que vous rencontrez est Jésus déguisé.\" -- Mère Teresa",
    hi_title: "vesh badalakar yeeshu",
    hi_content: "\"आप जिस भी व्यक्ति से मिलते हैं वह वेश बदलकर यीशु है।\" -- मदर टेरेसा",
    zh_title: "qiáo zhuāng de yēsū",
    zh_content: "“nǐ suǒ yù dào de měi yí gè rén dōu shì qiáo zhuāng de yēsū.” -- tè lǐ shā xiū nǚ"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.JESUS IN DISGUISE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->JESUS IN DISGUISE"
RETURN t, parent;
```
