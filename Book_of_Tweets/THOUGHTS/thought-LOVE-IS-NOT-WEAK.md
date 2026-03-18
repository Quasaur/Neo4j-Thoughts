---
type: THOUGHT
name: "thought.LOVE IS NOT WEAK"
alias: "Thought: Love Is Not Weak"
parent: "topic.LOVE"
en_content: "Love is not weak."
tags: ["love", "power", "strength", "character", "truth"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2012b)
CREATE (t:THOUGHT {    name: "thought.LOVE IS NOT WEAK",
    alias: "Thought: Love Is Not Weak",
    parent: "topic.LOVE",
    tags: ['love', 'power', 'strength', 'character', 'truth'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.LOVE IS NOT WEAK",
    ctype: "THOUGHT",
    en_title: "Love Is Not Weak",
    en_content: "Love is not weak.",
    es_title: "El Amor No Es Débil",
    es_content: "El amor no es débil.",
    fr_title: "L'Amour N'Est Pas Faible",
    fr_content: "L'amour n'est pas faible.",
    hi_title: "प्रेम दुर्बल नहीं है",
    hi_content: "प्रेम दुर्बल नहीं है।",
    zh_title: "Ài Bù Ruòxiǎo",
    zh_content: "Ài bù ruòxiǎo."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE IS NOT WEAK"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->LOVE IS NOT WEAK"
RETURN t, parent;
```
