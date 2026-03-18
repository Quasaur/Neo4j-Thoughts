---
type: THOUGHT
name: "thought.SHOWING MERCY"
alias: "Thought: Showing Mercy"
parent: "topic.MORALITY"
en_content: "Everybody wants Mercy...few show Mercy."
tags: ["mercy", "morality", "character", "compassion", "judgment"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jan-2011)
CREATE (t:THOUGHT {    name: "thought.SHOWING MERCY",
    alias: "Thought: Showing Mercy",
    parent: "topic.MORALITY",
    tags: ['mercy', 'morality', 'character', 'compassion', 'judgment'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SHOWING MERCY",
    ctype: "THOUGHT",
    en_title: "Showing Mercy",
    en_content: "Everybody wants Mercy...few show Mercy.",
    es_title: "Mostrar Misericordia",
    es_content: "Todos quieren Misericordia...pocos muestran Misericordia.",
    fr_title: "Faire Miséricorde",
    fr_content: "Tout le monde veut la Miséricorde...peu font Miséricorde.",
    hi_title: "दया दिखाना",
    hi_content: "सभी दया चाहते हैं...कुछ ही दया दिखाते हैं।",
    zh_title: "Xian Shi Ci Bei",
    zh_content: "Ren Ren Dou Xiang Yao Ci Bei...Que Shao You Ren Xian Shi Ci Bei."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SHOWING MERCY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->SHOWING MERCY"
RETURN t, parent;
```
