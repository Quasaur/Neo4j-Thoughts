---
name: thought.BEHIND
alias: "Thought: BEHIND"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- divine
- sovereignty
- impetus
- control
- all
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.BEHIND",
    alias: "Thought: BEHIND",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["divine", "sovereignty", "impetus", "control", "all"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BEHIND",
    en_title: "BEHIND",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BEHIND" AND c.name = "content.BEHIND"
MERGE (t)-[:HAS_CONTENT {name: "edge.BEHIND"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.BEHIND"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->BEHIND"}]->(child);
```