---
type: THOUGHT
name: "thought.GOD THE DREAMER"
alias: "Thought: God The Dreamer"
parent: "topic.PHILOSOPHY"
en_content: "Existence is a Dream--but we're not the dreamers...God is!"
tags: ["reality", "dream", "existence", "philosophy", "creator"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Oct-2010)
CREATE (t:THOUGHT {    name: "thought.GOD THE DREAMER",
    alias: "Thought: God The Dreamer",
    parent: "topic.PHILOSOPHY",
    tags: ['reality', 'dream', 'existence', 'philosophy', 'creator'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.GOD THE DREAMER",
    ctype: "THOUGHT",
    en_title: "God The Dreamer",
    en_content: "Existence is a Dream--but we're not the dreamers...God is!",
    es_title: "dios el soñador",
    es_content: "La existencia es un sueño, pero nosotros no somos los soñadores... ¡Dios sí lo es!",
    fr_title: "Dieu le rêveur",
    fr_content: "L'existence est un rêve, mais nous ne sommes pas des rêveurs... Dieu l'est !",
    hi_title: "सपने देखने वाला भगवान",
    hi_content: "अस्तित्व एक सपना है--लेकिन हम सपने देखने वाले नहीं हैं...ईश्वर है!",
    zh_title: "mèng xiǎng jiā shàng dì",
    zh_content: "cún zài shì yí gè mèng xiǎng —— dàn wǒ men bú shì mèng xiǎng jiā …… shàng dì cái shì ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD THE DREAMER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->GOD THE DREAMER"
RETURN t, parent;
```
