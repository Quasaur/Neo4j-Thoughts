---
name: "thought.JESUS IN DISGUISE"
alias: "Thought: Image of God"
type: THOUGHT
en_content: "\"Each person you meet is Jesus in disguise.\" -- Mother Teresa"
parent: "topic.HUMANITY"
tags:
- humanity
- jesus
- empathy
- service
- neighbors
level: 3
neo4j: false
ptopic: 
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.JESUS IN DISGUISE",
    alias: "Thought: Image of God",
    parent: "topic.HUMANITY",
    tags: ["humanity", "jesus", "empathy", "service", "neighbors"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.JESUS IN DISGUISE",
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

MATCH (t:THOUGHT {name: "thought.JESUS IN DISGUISE"})
MATCH (c:CONTENT {name: "content.JESUS IN DISGUISE"})
MERGE (t)-[:HAS_CONTENT {name: "edge.JESUS IN DISGUISE"}]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.JESUS IN DISGUISE"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HUMANITY->JESUS IN DISGUISE"}]->(child);
```
