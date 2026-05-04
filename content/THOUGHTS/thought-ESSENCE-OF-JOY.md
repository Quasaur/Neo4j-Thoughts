---
type: "THOUGHT"
name: "thought.ESSENCE OF JOY"
alias: "Thought: The Essence of Joy"
parent: "topic.ATTITUDE"
en_title: "Thought: The Essence of Joy"
en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I."
tags: ["joy", "god", "majesty", "discovery", "attitude"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ESSENCE OF JOY",
    alias: "Thought: The Essence of Joy",
    parent: "topic.ATTITUDE",
    tags: ["joy", "god", "majesty", "discovery", "attitude"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ESSENCE OF JOY",
    ctype: "THOUGHT",
    en_title: "Thought: The Essence of Joy",
    en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I.",
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
ON CREATE SET r.name = "t.edge.ESSENCE OF JOY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ESSENCE OF JOY"
RETURN t, parent;
```
