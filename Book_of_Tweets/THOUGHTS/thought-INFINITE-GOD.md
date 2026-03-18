---
type: THOUGHT
name: "thought.INFINITE GOD"
alias: "Thought: Divine Magnitude"
parent: "topic.THE GODHEAD"
en_content: "God is ALWAYS more than we think He is."
tags: ["infinite", "godhead", "majesty", "understanding", "limits"]
ptopic:
level: 1
neo4j: false
---

```Cypher
CREATE (t:THOUGHT {    name: "thought.INFINITE GOD",
    alias: "Thought: Divine Magnitude",
    parent: "topic.THE GODHEAD",
    tags: ["infinite", "godhead", "majesty", "understanding", "limits"],
    level: 1});

CREATE (c:CONTENT {
    name: "content.INFINITE GOD",
    ctype: "THOUGHT",
    en_title: "Infinite God",
    en_content: "God is ALWAYS more than we think He is.",
    es_title: "Dios infinito",
    es_content: "Dios es SIEMPRE más de lo que pensamos que es.",
    fr_title: "Dieu infini",
    fr_content: "Dieu est TOUJOURS plus que ce que nous pensons qu'Il est.",
    hi_title: "anant bhagavaan",
    hi_content: "भगवान हमेशा उससे कहीं अधिक है जितना हम सोचते हैं।",
    zh_title: "wú xiàn shàng dì",
    zh_content: "shàng dì zǒng shì bǐ wǒ men xiǎng xiàng de gèng jiā jí dà."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INFINITE GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->INFINITE GOD"
RETURN t, parent;
```
