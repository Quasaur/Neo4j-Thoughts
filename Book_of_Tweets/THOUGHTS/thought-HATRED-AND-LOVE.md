---
type: THOUGHT
name: "thought.HATRED AND LOVE"
alias: "Thought: Hatred And Love"
parent: "topic.PHILOSOPHY"
en_content: "One who is incapable of hatred is also incapable of love."
tags: ["love", "hatred", "character", "philosophy", "truth"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Nov-2012)
CREATE (t:THOUGHT {    name: "thought.HATRED AND LOVE",
    alias: "Thought: Hatred And Love",
    parent: "topic.PHILOSOPHY",
    tags: ['love', 'hatred', 'character', 'philosophy', 'truth'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.HATRED AND LOVE",
    ctype: "THOUGHT",
    en_title: "Hatred And Love",
    en_content: "One who is incapable of hatred is also incapable of love.",
    es_title: "Odio Y Amor",
    es_content: "Quien es incapaz de odiar también es incapaz de amar.",
    fr_title: "Haine Et Amour",
    fr_content: "Celui qui est incapable de haine est aussi incapable d'amour.",
    hi_title: "घृणा और प्रेम",
    hi_content: "जो व्यक्ति घृणा करने में असमर्थ है, वह प्रेम करने में भी असमर्थ है।",
    zh_title: "Hen Yu Ai",
    zh_content: "Bu neng hen de ren ye bu neng ai."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HATRED AND LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->HATRED AND LOVE"
RETURN t, parent;
```
