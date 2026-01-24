---
name: "thought.ALWAYS ADVENTIST"
alias: "Thought: Always Adventist"
type: THOUGHT
en_content: "A part of me will always be Adventist, I guess (smile)."
parent: "topic.RELIGION"
tags:
- identity
- religion
- adventism
- reflection
- faith
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.ALWAYS ADVENTIST",
    alias: "Thought: Always Adventist",
    parent: "topic.RELIGION",
    tags: ['identity', 'religion', 'adventism', 'reflection', 'faith'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ALWAYS ADVENTIST",
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

MATCH (t:THOUGHT {name: "thought.ALWAYS ADVENTIST"})
MATCH (c:CONTENT {name: "content.ALWAYS ADVENTIST"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALWAYS ADVENTIST" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.ALWAYS ADVENTIST"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION->ALWAYS ADVENTIST" }]->(child);
```
