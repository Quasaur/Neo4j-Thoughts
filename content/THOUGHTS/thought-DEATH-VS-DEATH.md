---
type: THOUGHT
name: "thought.DEATH VS DEATH"
alias: "Thought: Death Vs Death"
parent: "topic.THE-GOSPEL"
en_content: "Only GOD could come up with the idea of using death to destroy death!!!"
tags: ["death", "destroy", "idea", "god", "eternal_life"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEATH VS DEATH",
    alias: "Thought: Death Vs Death",
    parent: "topic.THE-GOSPEL",
    tags: ["death", "destroy", "idea", "god", "eternal_life"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEATH VS DEATH",
    ctype: "THOUGHT",
    en_title: "Death Vs Death",
    en_content: "Only GOD could come up with the idea of using death to destroy death!!!",
    es_title: "MUERTE CONTRA MUERTE",
    es_content: "¡¡¡Sólo a DIOS se le ocurrió la idea de usar la muerte para destruir la muerte!!!",
    fr_title: "MORT CONTRE MORT",
    fr_content: "Seul DIEU pouvait avoir l'idée d'utiliser la mort pour détruire la mort !!!",
    hi_title: "मृत्यु बनाम मृत्यु",
    hi_content: "केवल भगवान ही मृत्यु को नष्ट करने के लिए मृत्यु का उपयोग करने का विचार लेकर आ सकते हैं!!!",
    zh_title: "sǐ wáng yǔ sǐ wáng",
    zh_content: "zhǐ yǒu shàng dì cái néng xiǎng chū yòng sǐ wáng lái huǐ miè sǐ wáng de zhǔ yì ！！！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEATH VS DEATH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->DEATH VS DEATH"
RETURN t, parent;
```
