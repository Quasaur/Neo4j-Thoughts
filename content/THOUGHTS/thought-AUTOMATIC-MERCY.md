---
type: "THOUGHT"
name: "thought.AUTOMATIC MERCY"
alias: "Thought: Automatic Mercy"
parent: "topic.ATTITUDE"
en_title: "Thought: Automatic Mercy"
en_content: "God’s love for sinners doesn’t negate His utter hatred of sin. Mercy is neither owed nor deserved and should NEVER be presumed."
tags: ["spirituality", "mercy", "hatred", "gospel", "life"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.AUTOMATIC MERCY",
    alias: "Thought: Automatic Mercy",
    parent: "topic.ATTITUDE",
    tags: ["spirituality", "mercy", "hatred", "gospel", "life"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AUTOMATIC MERCY",
    ctype: "THOUGHT",
    en_title: "Thought: Automatic Mercy",
    en_content: "God’s love for sinners doesn’t negate His utter hatred of sin. Mercy is neither owed nor deserved and should NEVER be presumed.",
    es_title: "",
    es_content: "",
    fr_title: "",
    fr_content: "",
    hi_title: "",
    hi_content: "",
    zh_title: "",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AUTOMATIC MERCY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->AUTOMATIC MERCY"
RETURN t, parent;
```
