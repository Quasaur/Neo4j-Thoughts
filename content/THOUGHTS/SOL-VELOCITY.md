---
name: thought.SOL_VELOCITY
alias: "Thought: SOL VELOCITY"
type: THOUGHT
parent: topic.CREATION
tags:
- sol
- sun
- star
- velocity
- speed
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SOL_VELOCITY",
    alias: "Thought: SOL VELOCITY",
    parent: "topic.CREATION",
    tags: ["sol", "sun", "star", "velocity", "speed"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SOL_VELOCITY",
    en_title: "SOL VELOCITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SOL_VELOCITY" AND c.name = "content.SOL_VELOCITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.SOL_VELOCITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SOL_VELOCITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->SOL_VELOCITY"}]->(child);
```