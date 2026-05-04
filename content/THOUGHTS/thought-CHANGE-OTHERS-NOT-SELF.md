---
type: "THOUGHT"
name: "thought.CHANGE OTHERS NOT SELF"
alias: "Thought: Change Others, Not Self"
parent: "topic.ATTITUDE"
en_title: "Thought: Change Others, Not Self"
en_content: "We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it."
tags: ["change", "growth", "attitude", "pain", "transformation"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.CHANGE OTHERS NOT SELF",
    alias: "Thought: Change Others, Not Self",
    parent: "topic.ATTITUDE",
    tags: ["change", "growth", "attitude", "pain", "transformation"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHANGE OTHERS NOT SELF",
    ctype: "THOUGHT",
    en_title: "Thought: Change Others, Not Self",
    en_content: "We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it.",
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
ON CREATE SET r.name = "t.edge.CHANGE OTHERS NOT SELF"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->CHANGE OTHERS NOT SELF"
RETURN t, parent;
```
