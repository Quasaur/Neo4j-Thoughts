---
type: THOUGHT
name: "thought.ULTIMATE2"
alias: "Thought: THE ULTIMATE (2)"
en_content: "Every human that has ever lived will soon face either the Greatest Terror (God's Wrath) or the Greatest Pleasure (God's Grace)."
tags: ["deity", "wrath", "grace", "judgment", "acquittal"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ULTIMATE2",
    alias: "Thought: THE ULTIMATE (2)",
    parent: "topic.THE GODHEAD",
    tags: ["deity", "wrath", "grace", "judgment", "acquittal"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ULTIMATE2",
    ctype: "THOUGHT",
    en_title: "Ultimate2",
    en_content: "Every human that has ever lived will soon face either the Greatest Terror (God's Wrath) or the Greatest Pleasure (God's Grace).",
    es_title: "LO ÚLTIMO (2)",
    es_content: "Todo ser humano que alguna vez haya vivido pronto enfrentará el Mayor Terror (la Ira de Dios) o el Mayor Placer (la Gracia de Dios).",
    fr_title: "L'ULTIME (2)",
    fr_content: "Tout être humain ayant jamais vécu sera bientôt confronté soit à la plus grande terreur (la colère de Dieu), soit au plus grand plaisir (la grâce de Dieu).",
    hi_title: "परम (2)",
    hi_content: "प्रत्येक मानव जो कभी जीवित रहा है उसे जल्द ही सबसे बड़े आतंक (भगवान का क्रोध) या सबसे बड़ी खुशी (भगवान की कृपा) का सामना करना पड़ेगा।",
    zh_title: "zhōng jí  (2)",
    zh_content: "měi gè céng jīng shēng huó guò de rén lèi hěn kuài jiù huì miàn lín zuì dà de kǒng jù （ shàng dì de fèn nù ） huò zuì dà de kuài lè （ shàng dì de ēn diǎn ）。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ULTIMATE2"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->ULTIMATE2"
RETURN t, parent;
```
