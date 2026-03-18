---
type: THOUGHT
name: "thought.LOVE"
alias: "Thought: Love"
parent: "topic.LOVE"
tags: ["love", "spirit", "attitude", "selfless", "generosity"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---



```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOVE",
    alias: "Thought: Love",
    parent: "topic.LOVE",
    tags: ["love", "spirit", "attitude", "selfless", "generosity"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE",
    ctype: "THOUGHT",
    en_title: "Love",
    en_content: "",
    es_title: "AMAR",
    es_content: "El amor es mucho más que un simple sentimiento... ¡Es una decisión de tratar a alguien tan bien o mejor de lo que te tratas a ti mismo!",
    fr_title: "AMOUR",
    fr_content: "L'amour est bien plus qu'un simple sentiment... C'est une décision de traiter quelqu'un aussi bien, voire mieux, que vous-même !",
    hi_title: "प्यार",
    hi_content: "प्यार महज़ एक एहसास से कहीं ज़्यादा है...यह किसी के साथ उतना ही अच्छा या उससे बेहतर व्यवहार करने का निर्णय है जितना आप अपने साथ करते हैं!",
    zh_title: "ài",
    zh_content: "ài bù jǐn jǐn shì yī zhǒng gǎn jué …… tā shì yí gè jué dìng ， duì dài mǒu rén jiù xiàng duì dài zì jǐ yī yàng hǎo ， shèn zhì gèng hǎo ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->LOVE"
RETURN t, parent;
```
