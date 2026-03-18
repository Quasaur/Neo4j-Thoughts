---
type: THOUGHT
name: "thought.VOLITION5"
alias: "Thought: Fifth Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["freedom", "volition", "free_will", "ignorance", "flatearth"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VOLITION5",
    alias: "Thought: Fifth Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "free_will", "ignorance", "flatearth"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION5",
    ctype: "THOUGHT",
    en_title: "Fifth Volition",
    en_content: "",
    es_title: "QUINTA VOLICIÓN",
    es_content: "Durante cientos de años existió una TIERRA PLANA en Europa por culpa de la IGNORANCIA; Lo mismo ocurre con el LIBRE ALBEDRÍO.",
    fr_title: "CINQUIÈME VOLITION",
    fr_content: "Pendant des centaines d’années, une TERRE PLATE a existé en Europe à cause de l’IGNORANCE ; il en est de même avec le LIBRE ARBITRE.",
    hi_title: "पांचवी इच्छा",
    hi_content: "अज्ञानता के कारण यूरोप में सैकड़ों वर्षों तक चपटी पृथ्वी अस्तित्व में रही; स्वतंत्र इच्छा के साथ भी ऐसा ही है।",
    zh_title: "dì wǔ zhì yuàn",
    zh_content: "yóu yú wú zhī ， ōu zhōu shù bǎi nián lái yì zhí cún zài dì píng lùn 。 zì yóu yì zhì yě shì rú cǐ 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VOLITION5"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->VOLITION5"
RETURN t, parent;
```
