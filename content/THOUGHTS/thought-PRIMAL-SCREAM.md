---
type: THOUGHT
name: "thought.PRIMAL SCREAM"
alias: "Thought: Primal Scream"
parent: "topic.HUMOR"
en_content: "I believe in the Primal Scream."
tags: ["painting", "expression", "humor", "comedy", "faith"]
ptopic: "[[topic-HUMOR]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PRIMAL SCREAM",
    alias: "Thought: Primal Scream",
    parent: "topic.HUMOR",
    tags: ["painting", "expression", "humor", "comedy", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIMAL SCREAM",
    ctype: "THOUGHT",
    en_title: "Primal Scream",
    en_content: "I believe in the Primal Scream.",
    es_title: "GRITO PRIMARIO",
    es_content: "Creo en el Grito Primordial.",
    fr_title: "CRI PRIMAL",
    fr_content: "Je crois au Primal Scream.",
    hi_title: "प्रारंभिक चीख",
    hi_content: "मैं प्राइमल स्क्रीम में विश्वास करता हूं।",
    zh_title: "yuán shǐ jiān jiào",
    zh_content: "wǒ xiāng xìn yuán shǐ jiān jiào 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRIMAL SCREAM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMOR"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMOR->PRIMAL SCREAM"
RETURN t, parent;
```
