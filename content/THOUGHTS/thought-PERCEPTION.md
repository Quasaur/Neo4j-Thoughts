---
type: THOUGHT
name: "thought.PERCEPTION"
alias: "Thought: Perception"
parent: "topic.ATTITUDE"
tags: ["attitude", "seeing", "observing", "perception", "selfimprovement"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PERCEPTION",
    alias: "Thought: Perception",
    parent: "topic.ATTITUDE",
    tags: ["attitude", "seeing", "observing", "perception", "selfimprovement"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERCEPTION",
    ctype: "THOUGHT",
    en_title: "Perception",
    en_content: "",
    es_title: "PERCEPCIÓN",
    es_content: "No siempre podemos cambiar lo que vemos... pero siempre podemos cambiar cómo lo vemos.",
    fr_title: "PERCEPTION",
    fr_content: "Nous ne pouvons pas toujours changer ce que nous voyons... mais nous pouvons toujours changer la façon dont nous le voyons.",
    hi_title: "धारणा",
    hi_content: "हम जो देखते हैं उसे हमेशा नहीं बदल सकते...लेकिन हम उसे देखने का तरीका हमेशा बदल सकते हैं।",
    zh_title: "dòng chá lì",
    zh_content: "wǒ men bù néng zǒng shì gǎi biàn wǒ men suǒ kàn dào de …… dàn wǒ men zǒng shì kě yǐ gǎi biàn wǒ men kàn dài tā de fāng shì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PERCEPTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->PERCEPTION"
RETURN t, parent;
```
