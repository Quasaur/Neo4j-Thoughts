---
type: THOUGHT
name: "thought.ANOTHER SINNER"
alias: "Thought: Another Sinner"
parent: "topic.EVIL"
en_content: "Satan is just another sinner."
tags: ["satan", "sinner", "inferior", "god", "christ"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ANOTHER SINNER",
    alias: "Thought: Another Sinner",
    parent: "topic.EVIL",
    tags: ["satan", "sinner", "inferior", "god", "christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANOTHER SINNER",
    ctype: "THOUGHT",
    en_title: "Another Sinner",
    en_content: "Satan is just another sinner.",
    es_title: "OTRO PECADOR",
    es_content: "Satanás es simplemente otro pecador.",
    fr_title: "UN AUTRE PÉCHEUR",
    fr_content: "Satan n'est qu'un autre pécheur.",
    hi_title: "एक और पापी",
    hi_content: "शैतान एक और पापी है.",
    zh_title: "lìng yí gè zuì rén",
    zh_content: "sā dàn zhǐ bù guò shì lìng yí gè zuì rén 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ANOTHER SINNER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->ANOTHER SINNER"
RETURN t, parent;
```
