---
type: "THOUGHT"
name: "thought.DEFINE APATHY"
alias: "Thought: Apathy Defined"
parent: "topic.ATTITUDE"
en_title: "Thought: Apathy Defined"
en_content: "Love & Hate are not opposites; they are two halves of the same coin; the opposite of Love / Hate is Apathy."
tags: ["love", "hate", "apathy", "attitude", "philosophy"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE APATHY",
    alias: "Thought: Apathy Defined",
    parent: "topic.ATTITUDE",
    tags: ["love", "hate", "apathy", "attitude", "philosophy"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE APATHY",
    ctype: "THOUGHT",
    en_title: "Thought: Apathy Defined",
    en_content: "Love & Hate are not opposites; they are two halves of the same coin; the opposite of Love / Hate is Apathy.",
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
ON CREATE SET r.name = "t.edge.DEFINE APATHY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->DEFINE APATHY"
RETURN t, parent;
```
