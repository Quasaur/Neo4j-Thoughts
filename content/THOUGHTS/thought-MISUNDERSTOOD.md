---
type: THOUGHT
name: "thought.MISUNDERSTOOD"
alias: "Thought: MISUNDERSTOOD"
parent: "topic.UNDERSTANDING"
tags: ["misunderfstood", "understanding", "communication", "fellowship", "intimacy"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MISUNDERSTOOD",
    alias: "Thought: MISUNDERSTOOD",
    parent: "topic.UNDERSTANDING",
    tags: ["misunderfstood", "understanding", "communication", "fellowship", "intimacy"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MISUNDERSTOOD",
    ctype: "THOUGHT",
    en_title: "MISUNDERSTOOD",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MISUNDERSTOOD" AND c.name = "content.MISUNDERSTOOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.MISUNDERSTOOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.MISUNDERSTOOD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.UNDERSTANDING->MISUNDERSTOOD"}]->(child);
```