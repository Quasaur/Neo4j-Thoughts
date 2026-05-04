---
type: "THOUGHT"
name: "thought.ATTENTION DESIRE"
alias: "Thought: Attention Desire"
parent: "topic.ATTITUDE"
en_title: "Thought: Attention Desire"
en_content: "I only want your attention when you don't want to give it to me."
tags: ["attitude", "attention", "human_nature", "desire", "pride"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ATTENTION DESIRE",
    alias: "Thought: Attention Desire",
    parent: "topic.ATTITUDE",
    tags: ["attitude", "attention", "human_nature", "desire", "pride"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ATTENTION DESIRE",
    ctype: "THOUGHT",
    en_title: "Thought: Attention Desire",
    en_content: "I only want your attention when you don't want to give it to me.",
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
ON CREATE SET r.name = "t.edge.ATTENTION DESIRE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ATTENTION DESIRE"
RETURN t, parent;
```
