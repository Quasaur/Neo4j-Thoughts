---
type: THOUGHT
name: "thought.LOST SCIENTISTS"
alias: "Thought: Lost Scientists"
parent: "topic.COSMOLOGY"
en_content: "The truth is that scientists have had to admit that they're lost beyond the Big Bang."
tags: ["science", "bigbang", "lost", "creatiion", "origin"]
ptopic: "[[topic-COSMOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOST SCIENTISTS",
    alias: "Thought: Lost Scientists",
    parent: "topic.COSMOLOGY",
    tags: ["science", "bigbang", "lost", "creatiion", "origin"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOST SCIENTISTS",
    ctype: "THOUGHT",
    en_title: "Lost Scientists",
    en_content: "The truth is that scientists have had to admit that they're lost beyond the Big Bang.",
    es_title: "CIENTÍFICOS PERDIDOS",
    es_content: "La verdad es que los científicos han tenido que admitir que están perdidos más allá del Big Bang.",
    fr_title: "SCIENTIFIQUES PERDUS",
    fr_content: "La vérité est que les scientifiques ont dû admettre qu’ils sont perdus au-delà du Big Bang.",
    hi_title: "खोए हुए वैज्ञानिक",
    hi_content: "सच्चाई यह है कि वैज्ञानिकों को यह स्वीकार करना पड़ा है कि वे बिग बैंग से परे खो गए हैं।",
    zh_title: "mí shī de kē xué jiā",
    zh_content: "shì shí shì ， kē xué jiā men bù dé bù chéng rèn ， tā men zài dà bào zhà zhī hòu jiù mí shī le 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOST SCIENTISTS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.COSMOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.COSMOLOGY->LOST SCIENTISTS"
RETURN t, parent;
```
