---
name: "thought.LOVE IS NOT WEAK"
alias: "Thought: Love Is Not Weak"
type: THOUGHT
en_content: "Love is not weak."
parent: "topic.LOVE"
tags:
- love
- power
- strength
- character
- truth
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2012b)
CREATE (t:THOUGHT {
    name: "thought.LOVE IS NOT WEAK",
    alias: "Thought: Love Is Not Weak",
    parent: "topic.LOVE",
    tags: ['love', 'power', 'strength', 'character', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE IS NOT WEAK",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE IS NOT WEAK" AND c.name = "content.LOVE IS NOT WEAK"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE IS NOT WEAK" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.LOVE IS NOT WEAK"
MERGE (parent)-[:HAS_THOUGHT { "name": "LOVE >LOVE IS NOT WEAK" }]->(child);
```
