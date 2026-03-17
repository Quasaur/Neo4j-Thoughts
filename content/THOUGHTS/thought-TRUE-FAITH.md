---
type: THOUGHT
name: "thought.TRUE FAITH"
alias: "Thought: True Faith"
parent: "topic.FAITH"
en_content: "True Faith is believing in God enough to place His Revealed Will above my own."
tags: ["faith", "trust", "confidence", "obedience", "submission"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TRUE FAITH",
    alias: "Thought: True Faith",
    parent: "topic.FAITH",
    tags: ["faith", "trust", "confidence", "obedience", "submission"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TRUE FAITH",
    ctype: "THOUGHT",
    en_title: "True Faith",
    en_content: "True Faith is believing in God enough to place His Revealed Will above my own.",
    es_title: "FE VERDADERA",
    es_content: "La verdadera fe es creer en Dios lo suficiente como para poner Su Voluntad Revelada por encima de la mía.",
    fr_title: "VRAIE FOI",
    fr_content: "La vraie foi consiste à croire suffisamment en Dieu pour placer sa volonté révélée au-dessus de la mienne.",
    hi_title: "सत्य विश्वास",
    hi_content: "सच्चा विश्वास ईश्वर में इतना विश्वास करना है कि उसकी प्रकट इच्छा को अपनी इच्छा से ऊपर रख सकूं।",
    zh_title: "zhēn shí de xìn yǎng",
    zh_content: "zhēn zhèng de xìn yǎng shì duì shàng dì de xìn yǎng ， zú yǐ jiāng tā suǒ qǐ shì de yì zhì zhì yú wǒ zì jǐ de yì zhì zhī shàng 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TRUE FAITH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITH->TRUE FAITH"
RETURN t, parent;
```
