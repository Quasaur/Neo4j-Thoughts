---
type: THOUGHT
name: "thought.MOTHER OF JESUS"
alias: "Thought: Mother Of Jesus"
parent: "topic.THE GODHEAD"
en_content: "Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God."
tags: ["mary", "jesus", "divinity", "theology", "incarnation"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011c)
CREATE (t:THOUGHT {    name: "thought.MOTHER OF JESUS",
    alias: "Thought: Mother Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['mary', 'jesus', 'divinity', 'theology', 'incarnation'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.MOTHER OF JESUS",
    ctype: "THOUGHT",
    en_title: "Mother Of Jesus",
    en_content: "Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God.",
    es_title: "Madre de Jesús",
    es_content: "María es la madre BIOLÓGICA de Jesús, no la madre ESPIRITUAL de Dios.",
    fr_title: "Mère de Jésus",
    fr_content: "Marie est la mère BIOLOGIQUE de Jésus, non la mère SPIRITUELLE de Dieu.",
    hi_title: "यीशु की माता",
    hi_content: "मरियम यीशु की जैविक माता है, परमेश्वर की आध्यात्मिक माता नहीं।",
    zh_title: "Yesu de muqin",
    zh_content: "Maliya shi Yesu de shengwu muqin, bushi Shen de shengling muqin."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MOTHER OF JESUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->MOTHER OF JESUS"
RETURN t, parent;
```
