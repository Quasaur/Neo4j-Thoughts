---
type: THOUGHT
name: "thought.MERCY OF JESUS"
alias: "Thought: Mercy Of Jesus"
parent: "topic.THE GODHEAD"
en_content: "Jesus is FAR MORE merciful and compassionate than you are!"
tags: ["jesus", "mercy", "compassion", "divinity", "love"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Nov-2011)
CREATE (t:THOUGHT {    name: "thought.MERCY OF JESUS",
    alias: "Thought: Mercy Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'mercy', 'compassion', 'divinity', 'love'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.MERCY OF JESUS",
    ctype: "THOUGHT",
    en_title: "Mercy Of Jesus",
    en_content: "Jesus is FAR MORE merciful and compassionate than you are!",
    es_title: "Misericordia de Jesús",
    es_content: "¡Jesús es MUCHO MÁS misericordioso y compasivo de lo que tú eres!",
    fr_title: "Miséricorde de Jésus",
    fr_content: "Jésus est BIEN PLUS miséricordieux et compatissant que vous ne l'êtes !",
    hi_title: "यीशु की दया",
    hi_content: "यीशु आपसे कहीं अधिक दयालु और करुणामय हैं!",
    zh_title: "Yesu de Cibei",
    zh_content: "Yesu bi ni geng jia cibei he fuyou tongqingxin!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MERCY OF JESUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->MERCY OF JESUS"
RETURN t, parent;
```
