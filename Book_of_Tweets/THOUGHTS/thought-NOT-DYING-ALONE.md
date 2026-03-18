---
type: THOUGHT
name: "thought.NOT DYING ALONE"
alias: "Thought: Not Dying Alone"
parent: "topic.SPIRITUALITY"
en_content: "God will let you die...but He will not let you die alone."
tags: ["death", "comfort", "presence", "spirituality", "compassion"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Jan-2012)
CREATE (t:THOUGHT {    name: "thought.NOT DYING ALONE",
    alias: "Thought: Not Dying Alone",
    parent: "topic.SPIRITUALITY",
    tags: ['death', 'comfort', 'presence', 'spirituality', 'compassion'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.NOT DYING ALONE",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOT DYING ALONE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->NOT DYING ALONE"
RETURN t, parent;
```
