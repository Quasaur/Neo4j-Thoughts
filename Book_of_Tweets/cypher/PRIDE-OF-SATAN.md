---
name: "thought.PRIDE OF SATAN"
alias: "Thought: Pride Of Satan"
type: THOUGHT
en_content: "\"I'm the center of my universe...why can't I be the center of everyone else's?\" -- The Devil"
parent: "topic.EVIL"
tags:
- pride
- devil
- evil
- selfishness
- deception
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.PRIDE OF SATAN",
    alias: "Thought: Pride Of Satan",
    parent: "topic.EVIL",
    tags: ['pride', 'devil', 'evil', 'selfishness', 'deception'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIDE OF SATAN",
    en_title: "Pride Of Satan",
    en_content: "\"I'm the center of my universe...why can't I be the center of everyone else's?\" -- The Devil",
    es_title: "Orgullo de satanás",
    es_content: "\",
    fr_title: "Fierté de Satan",
    fr_content: "\",
    hi_title: "शैतान का गौरव",
    hi_content: "\",
    zh_title: "撒旦的骄傲",
    zh_content: "\"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIDE OF SATAN" AND c.name = "content.PRIDE OF SATAN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIDE OF SATAN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.PRIDE OF SATAN"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >PRIDE OF SATAN" }]->(child);
```
