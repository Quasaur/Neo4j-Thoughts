---
name: "thought.HATRED AND LOVE"
alias: "Thought: Hatred And Love"
type: THOUGHT
en_content: "One who is incapable of hatred is also incapable of love."
parent: "topic.PHILOSOPHY"
tags:
- love
- hatred
- character
- philosophy
- truth
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Nov-2012)
CREATE (t:THOUGHT {
    name: "thought.HATRED AND LOVE",
    alias: "Thought: Hatred And Love",
    parent: "topic.PHILOSOPHY",
    tags: ['love', 'hatred', 'character', 'philosophy', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HATRED AND LOVE",
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

MATCH (t:THOUGHT {name: "thought.HATRED AND LOVE"})
MATCH (c:CONTENT {name: "content.HATRED AND LOVE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.HATRED AND LOVE" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.HATRED AND LOVE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->HATRED AND LOVE" }]->(child);
```
