---
name: "thought.SAYING NO TO SELF"
alias: "Thought: Saying No To Self"
type: THOUGHT
en_content: "Only a person who can say no to themselves can say no to the world and to the devil."
parent: "topic.SPIRITUALITY"
tags:
- discipline
- self_denial
- world
- devil
- character
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.SAYING NO TO SELF",
    alias: "Thought: Saying No To Self",
    parent: "topic.SPIRITUALITY",
    tags: ['discipline', 'self_denial', 'world', 'devil', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SAYING NO TO SELF",
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

MATCH (t:THOUGHT {name: "thought.SAYING NO TO SELF"})
MATCH (c:CONTENT {name: "content.SAYING NO TO SELF"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SAYING NO TO SELF" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.SAYING NO TO SELF"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->SAYING NO TO SELF" }]->(child);
```
