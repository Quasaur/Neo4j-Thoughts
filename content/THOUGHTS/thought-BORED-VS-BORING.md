---
type: THOUGHT
name: "thought.BORED VS BORING"
alias: "Thought: Bored vs Boring"
parent: "topic.ATTITUDE"
en_content: "Better to be bored than to be boring."
tags: ["boredom", "personality", "attitude", "character", "irony"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BORED VS BORING",
    alias: "Thought: Bored Vs Boring",
    parent: "topic.ATTITUDE",
    tags: ["boredom", "personality", "attitude", "character", "irony"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BORED VS BORING",
    ctype: "THOUGHT",
    en_title: "Thought: Bored vs Boring",
    en_content: "Better to be bored than to be boring.",
    es_title: "Pensamiento: Aburrido versus Aburridor",
    es_content: "Mejor estar aburrido que ser aburridor.",
    fr_title: "Pensée : Ennuyé ou Ennuyeux",
    fr_content: "Mieux vaut s'ennuyer que d'être ennuyeux.",
    hi_title: "विचार: ऊब बनाम उबाऊ",
    hi_content: "ऊबा होना उबाऊ होने से बेहतर है।",
    zh_title: "xiǎng fǎ : wú liáo yǔ wú liáo",
    zh_content: "wú liáo zǒng bǐ wú liáo hǎo ."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BORED VS BORING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->BORED VS BORING"
RETURN t, parent;
```
