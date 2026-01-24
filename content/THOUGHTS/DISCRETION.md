---
name: thought.DISCRETION
alias: "Thought: DISCRETION"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- discretion
- sensitivity
- tactfulness
- relationships
- wisdom
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DISCRETION",
    alias: "Thought: DISCRETION",
    parent: "topic.PSYCHOLOGY",
    tags: ["discretion", "sensitivity", "tactfulness", "relationships", "wisdom"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DISCRETION",
    en_title: "DISCRETION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DISCRETION" AND c.name = "content.DISCRETION"
MERGE (t)-[:HAS_CONTENT {name: "edge.DISCRETION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.DISCRETION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->DISCRETION"}]->(child);
```