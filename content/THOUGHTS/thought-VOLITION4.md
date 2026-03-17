---
type: THOUGHT
name: "thought.VOLITION4"
alias: "Thought: Fourth Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "hell", "damnation"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VOLITION4",
    alias: "Thought: Fourth Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "hell", "damnation"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION4",
    ctype: "THOUGHT",
    en_title: "Fourth Volition",
    en_content: "",
    es_title: "CUARTA VOLICIÓN",
    es_content: "Si el libre albedrío te lleva al infierno, ¿cuál era el punto?",
    fr_title: "QUATRIÈME VOLITION",
    fr_content: "Si le Libre Arbitre vous met en Enfer, à quoi ça sert ???",
    hi_title: "चौथी इच्छा",
    hi_content: "यदि स्वतंत्र इच्छा आपको नर्क में डाल देती है, तो बात क्या थी???",
    zh_title: "dì sì cì yì yuàn",
    zh_content: "rú guǒ zì yóu yì zhì ràng nǐ xià dì yù ， nà hái yǒu shén me yì yì ？？？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VOLITION4"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE-SOVEREIGNTY->VOLITION4"
RETURN t, parent;
```
