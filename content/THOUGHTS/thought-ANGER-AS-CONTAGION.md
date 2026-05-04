---
type: "THOUGHT"
name: "thought.ANGER AS CONTAGION"
alias: "Thought: Anger As Contagion"
parent: "topic.ATTITUDE"
en_title: "Thought: Anger As Contagion"
en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason."
tags: ["anger", "reason", "soul", "attitude", "character"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ANGER AS CONTAGION",
    alias: "Thought: Anger As Contagion",
    parent: "topic.ATTITUDE",
    tags: ["anger", "reason", "soul", "attitude", "character"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ANGER AS CONTAGION",
    ctype: "THOUGHT",
    en_title: "Thought: Anger As Contagion",
    en_content: "Anger is a contagion that easily leaps from soul to soul where there is an absence of reason.",
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
ON CREATE SET r.name = "t.edge.ANGER AS CONTAGION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ANGER AS CONTAGION"
RETURN t, parent;
```
