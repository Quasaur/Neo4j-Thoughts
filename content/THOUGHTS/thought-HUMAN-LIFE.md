---
type: THOUGHT
name: "thought.HUMAN LIFE"
alias: "Thought: Human Life"
parent: "topic.WORSHIP"
en_content: "The purpose of intelligent human life is to Worship, Obey and Serve The Godhead."
tags: ["humanity", "godhead", "intelligent", "life", "purpose"]
ptopic: "[[topic-WORSHIP]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HUMAN LIFE",
    alias: "Thought: Human Life",
    parent: "topic.WORSHIP",
    tags: ["humanity", "godhead", "intelligent", "life", "purpose"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN LIFE",
    ctype: "THOUGHT",
    en_title: "Human Life",
    en_content: "The purpose of intelligent human life is to Worship, Obey and Serve The Godhead.",
    es_title: "VIDA HUMANA",
    es_content: "El propósito de la vida humana inteligente es Adorar, Obedecer y Servir a la Divinidad.",
    fr_title: "VIE HUMAINE",
    fr_content: "Le but de la vie humaine intelligente est d’adorer, d’obéir et de servir la Divinité.",
    hi_title: "मानव जीवन",
    hi_content: "बुद्धिमान मानव जीवन का उद्देश्य भगवान की पूजा, आज्ञापालन और सेवा करना है।",
    zh_title: "rén lèi shēng huó",
    zh_content: "zhì huì rén lèi shēng huó de mù dì shì chóng bài 、 fú cóng hé fú wù shén 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMAN LIFE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WORSHIP"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WORSHIP->HUMAN LIFE"
RETURN t, parent;
```
