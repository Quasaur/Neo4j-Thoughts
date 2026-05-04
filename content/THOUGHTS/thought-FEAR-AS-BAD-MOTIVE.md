---
type: "THOUGHT"
name: "thought.FEAR AS BAD MOTIVE"
alias: "Thought: Fear As Bad Motive"
parent: "topic.ATTITUDE"
en_title: "Thought: Fear As Bad Motive"
en_content: "Fear is rarely a good motive for any action."
tags: ["fear", "motive", "action", "attitude", "character"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FEAR AS BAD MOTIVE",
    alias: "Thought: Fear As Bad Motive",
    parent: "topic.ATTITUDE",
    tags: ["fear", "motive", "action", "attitude", "character"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FEAR AS BAD MOTIVE",
    ctype: "THOUGHT",
    en_title: "Thought: Fear As Bad Motive",
    en_content: "Fear is rarely a good motive for any action.",
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
ON CREATE SET r.name = "t.edge.FEAR AS BAD MOTIVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->FEAR AS BAD MOTIVE"
RETURN t, parent;
```
