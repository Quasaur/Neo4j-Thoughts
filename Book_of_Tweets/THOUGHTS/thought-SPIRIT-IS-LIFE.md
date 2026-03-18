---
type: THOUGHT
name: "thought.SPIRIT IS LIFE"
alias: "Thought: Spirit Is Life"
parent: "topic.THE GODHEAD"
en_content: "Spirit, not electricity, is Life."
tags: ["spirit", "life", "science", "power", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013a)
CREATE (t:THOUGHT {    name: "thought.SPIRIT IS LIFE",
    alias: "Thought: Spirit Is Life",
    parent: "topic.THE GODHEAD",
    tags: ['spirit', 'life', 'science', 'power', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.SPIRIT IS LIFE",
    ctype: "THOUGHT",
    en_title: "Spirit Is Life",
    en_content: "Spirit, not electricity, is Life.",
    es_title: "El Espíritu es Vida",
    es_content: "El Espíritu, no la electricidad, es la Vida.",
    fr_title: "L'Esprit est la Vie",
    fr_content: "L'Esprit, et non l'électricité, est la Vie.",
    hi_title: "आत्मा ही जीवन है",
    hi_content: "आत्मा, बिजली नहीं, जीवन है।",
    zh_title: "Líng shì shēngmìng  líng shì shēng mìng",
    zh_content: "Líng, ér bù shì diàn, shì shēngmìng.  líng ， ér bú shì diàn ， shì shēng mìng 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SPIRIT IS LIFE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->SPIRIT IS LIFE"
RETURN t, parent;
```
