---
type: THOUGHT
name: "thought.IMAGINATION"
alias: "Thought: IMAGINATION"
parent: "topic.UNDERSTANDING"
tags: ["imagination", "imagery", "vision", "mind", "realization"]
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.IMAGINATION",
    alias: "Thought: IMAGINATION",
    parent: "topic.UNDERSTANDING",
    tags: ["imagination", "imagery", "vision", "mind", "realization"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.IMAGINATION",
    ctype: "THOUGHT",
    en_title: "IMAGINATION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMAGINATION" AND c.name = "content.IMAGINATION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.IMAGINATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.IMAGINATION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.UNDERSTANDING->IMAGINATION"}]->(child);
```