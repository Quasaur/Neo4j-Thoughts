---
name: "thought.INFINITE GOD"
alias: "Thought: Divine Magnitude"
en_content: "God is ALWAYS more than we think He is."
parent: topic.THE GODHEAD
tags:
  - infinite
  - godhead
  - majesty
  - understanding
  - limits
level: 1
neo4j: false
ptopic: 
type: THOUGHT
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INFINITE GOD",
    alias: "Thought: Divine Magnitude",
    parent: "topic.THE GODHEAD",
    tags: ["infinite", "godhead", "majesty", "understanding", "limits"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.INFINITE GOD",
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

MATCH (t:THOUGHT {name: "thought.INFINITE GOD"})
MATCH (c:CONTENT {name: "content.INFINITE GOD"})
MERGE (t)-[:HAS_CONTENT {name: "edge.INFINITE GOD"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.INFINITE GOD"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->INFINITE GOD"}]->(child);
```
