---
type: "THOUGHT"
name: "thought.BORED VS BORING"
alias: "Thought: Bored vs Boring"
parent: "topic.ATTITUDE"
en_title: "Thought: Bored vs Boring"
en_content: "Better to be bored than to be boring."
tags: ["boredom", "personality", "attitude", "character", "irony"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BORED VS BORING",
    alias: "Thought: Bored vs Boring",
    parent: "topic.ATTITUDE",
    tags: ["boredom", "personality", "attitude", "character", "irony"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BORED VS BORING",
    ctype: "THOUGHT",
    en_title: "Thought: Bored vs Boring",
    en_content: "Better to be bored than to be boring.",
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
ON CREATE SET r.name = "t.edge.BORED VS BORING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->BORED VS BORING"
RETURN t, parent;
```
