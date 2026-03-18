---
type: THOUGHT
name: "thought.RESPECT AND AFFECTION"
alias: "Thought: Respect And Affection"
parent: "topic.MORALITY"
en_content: "Respect breeds affection."
tags: ["respect", "affection", "relationship", "morality", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2011b)
CREATE (t:THOUGHT {    name: "thought.RESPECT AND AFFECTION",
    alias: "Thought: Respect And Affection",
    parent: "topic.MORALITY",
    tags: ['respect', 'affection', 'relationship', 'morality', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.RESPECT AND AFFECTION",
    ctype: "THOUGHT",
    en_title: "Respect And Affection",
    en_content: "Respect breeds affection.",
    es_title: "Respeto Y Afecto",
    es_content: "El respeto engendra afecto.",
    fr_title: "Respect Et Affection",
    fr_content: "Le respect engendre l'affection.",
    hi_title: "सम्मान और स्नेह",
    hi_content: "सम्मान स्नेह को जन्म देता है।",
    zh_title: "Zun Zhong Yu Ai Qing",
    zh_content: "Zun zhong zi yang ai qing."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RESPECT AND AFFECTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->RESPECT AND AFFECTION"
RETURN t, parent;
```
