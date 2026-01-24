---
name: thought.PREDESTINED
alias: "Thought: PREDESTINED"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- sovereignty
- election
- lordship
- chosen
- jesuschrist
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PREDESTINED",
    alias: "Thought: PREDESTINED",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["sovereignty", "election", "lordship", "chosen", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PREDESTINED",
    en_title: "PREDESTINED",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PREDESTINED" AND c.name = "content.PREDESTINED"
MERGE (t)-[:HAS_CONTENT {name: "edge.PREDESTINED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.PREDESTINED"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->PREDESTINED"}]->(child);
```