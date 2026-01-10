---
name: thought.IMAGINATION
alias: "Thought: IMAGINATION"
type: THOUGHT
parent: topic.UNDERSTANDING
tags:
- imagination
- imagery
- vision
- mind
- realization
neo4j: true
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
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
    en_title: "IMAGINATION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMAGINATION" AND c.name = "content.IMAGINATION"
MERGE (t)-[:HAS_CONTENT {name: "edge.IMAGINATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "thought.IMAGINATION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.UNDERSTANDING->IMAGINATION"}]->(child);
```