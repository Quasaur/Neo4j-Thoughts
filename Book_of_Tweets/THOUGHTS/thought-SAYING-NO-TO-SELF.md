---
type: THOUGHT
name: "thought.SAYING NO TO SELF"
alias: "Thought: Saying No To Self"
parent: "topic.SPIRITUALITY"
en_content: "Only a person who can say no to themselves can say no to the world and to the devil."
tags: ["discipline", "self_denial", "world", "devil", "character"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012c)
CREATE (t:THOUGHT {    name: "thought.SAYING NO TO SELF",
    alias: "Thought: Saying No To Self",
    parent: "topic.SPIRITUALITY",
    tags: ['discipline', 'self_denial', 'world', 'devil', 'character'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.SAYING NO TO SELF",
    ctype: "THOUGHT",
    en_title: "Saying No To Self",
    en_content: "Only a person who can say no to themselves can say no to the world and to the devil.",
    es_title: "Decir No a Uno Mismo",
    es_content: "Solo una persona que puede decirse no a sí misma puede decir no al mundo y al diablo.",
    fr_title: "Dire Non à Soi-Même",
    fr_content: "Seule une personne qui peut se dire non à elle-même peut dire non au monde et au diable.",
    hi_title: "स्वयं को ना कहना",
    hi_content: "केवल वह व्यक्ति जो स्वयं को ना कह सकता है, वही संसार और शैतान को ना कह सकता है।",
    zh_title: "Dui Ziji Shuo Bu",
    zh_content: "Zhiyou neng dui ziji shuo bu de ren, cai neng dui shijie he mogui shuo bu."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SAYING NO TO SELF"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->SAYING NO TO SELF"
RETURN t, parent;
```
