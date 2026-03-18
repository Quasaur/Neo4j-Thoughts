---
type: THOUGHT
name: "thought.ALWAYS ADVENTIST"
alias: "Thought: Always Adventist"
parent: "topic.RELIGION"
en_content: "A part of me will always be Adventist, I guess (smile)."
tags: ["identity", "religion", "adventism", "reflection", "faith"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2011c)
CREATE (t:THOUGHT {    name: "thought.ALWAYS ADVENTIST",
    alias: "Thought: Always Adventist",
    parent: "topic.RELIGION",
    tags: ['identity', 'religion', 'adventism', 'reflection', 'faith'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.ALWAYS ADVENTIST",
    ctype: "THOUGHT",
    en_title: "Always Adventist",
    en_content: "A part of me will always be Adventist, I guess (smile).",
    es_title: "Siempre Adventista",
    es_content: "Una parte de mí siempre será adventista, supongo (sonrisa).",
    fr_title: "Toujours Adventiste",
    fr_content: "Une partie de moi sera toujours adventiste, je suppose (sourire).",
    hi_title: "हमेशा एडवेंटिस्ट",
    hi_content: "मेरा एक हिस्सा हमेशा एडवेंटिस्ट रहेगा, मुझे लगता है (मुस्कान)।",
    zh_title: "Yǒngyuǎn de fùlín",
    zh_content: "Wǒ xiǎng, wǒ de yībùfèn jiāng yǒngyuǎn shì fùlín xìntú (wēixiào)."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ALWAYS ADVENTIST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->ALWAYS ADVENTIST"
RETURN t, parent;
```
