---
name: "thought.SPIRIT IS LIFE"
alias: "Thought: Spirit Is Life"
type: THOUGHT
en_content: "Spirit, not electricity, is Life."
parent: "topic.THE GODHEAD"
tags:
- spirit
- life
- science
- power
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT IS LIFE",
    alias: "Thought: Spirit Is Life",
    parent: "topic.THE GODHEAD",
    tags: ['spirit', 'life', 'science', 'power', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.SPIRIT IS LIFE",
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

MATCH (t:THOUGHT {name: "thought.SPIRIT IS LIFE"})
MATCH (c:CONTENT {name: "content.SPIRIT IS LIFE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT IS LIFE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.SPIRIT IS LIFE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->SPIRIT IS LIFE" }]->(child);
```
