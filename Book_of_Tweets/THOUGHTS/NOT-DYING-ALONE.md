---
name: "thought.NOT DYING ALONE"
alias: "Thought: Not Dying Alone"
type: THOUGHT
en_content: "God will let you die...but He will not let you die alone."
parent: "topic.SPIRITUALITY"
tags:
- death
- comfort
- presence
- spirituality
- compassion
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NOT DYING ALONE",
    alias: "Thought: Not Dying Alone",
    parent: "topic.SPIRITUALITY",
    tags: ['death', 'comfort', 'presence', 'spirituality', 'compassion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOT DYING ALONE",
    en_title: "Not Dying Alone",
    en_content: "God will let you die...but He will not let you die alone.",
    es_title: "No Morir Solo",
    es_content: "Dios te dejará morir...pero no te dejará morir solo.",
    fr_title: "Ne Pas Mourir Seul",
    fr_content: "Dieu te laissera mourir...mais Il ne te laissera pas mourir seul.",
    hi_title: "अकेले नहीं मरना",
    hi_content: "परमेश्वर तुम्हें मरने देगा...लेकिन वह तुम्हें अकेले नहीं मरने देगा।",
    zh_title: "Bu Gu Du Si Qu",
    zh_content: "Shang Di hui rang ni si qu...dan Ta bu hui rang ni gu du de si qu."
});

MATCH (t:THOUGHT {name: "thought.NOT DYING ALONE"})
MATCH (c:CONTENT {name: "content.NOT DYING ALONE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT DYING ALONE" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.NOT DYING ALONE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NOT DYING ALONE" }]->(child);
```
