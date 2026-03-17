---
type: THOUGHT
name: "thought.FIRST RULE"
alias: "Thought: First Rule"
parent: "topic.HUMOR"
en_content: "First rule of Twitter: you do not talk about FaceBook. (dying of laughter)."
tags: ["humor", "comedy", "social", "media", "movie"]
ptopic: "[[topic-HUMOR]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FIRST RULE",
    alias: "Thought: First Rule",
    parent: "topic.HUMOR",
    tags: ["humor", "comedy", "social", "media", "movie"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FIRST RULE",
    ctype: "THOUGHT",
    en_title: "First Rule",
    en_content: "First rule of Twitter: you do not talk about FaceBook. (dying of laughter).",
    es_title: "PRIMERA REGLA",
    es_content: "Primera regla de Twitter: no se habla de Facebook. Morir de risa.",
    fr_title: "PREMIÈRE RÈGLE",
    fr_content: "Première règle de Twitter : on ne parle pas de Facebook. Mourir de rire.",
    hi_title: "पहला नियम",
    hi_content: "First rule of Twitter: you do not talk about FaceBook. (dying of laughter).",
    zh_title: "dì yī tiáo guī zé",
    zh_content: "Twitter  de dì yī tiáo guī zé ： nǐ bù néng tán lùn  Facebook。 xiào sǐ le 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FIRST RULE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMOR"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMOR->FIRST RULE"
RETURN t, parent;
```
