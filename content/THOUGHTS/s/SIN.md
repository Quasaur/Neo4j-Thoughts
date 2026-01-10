---
name: thought.SIN
alias: "Thought: SIN"
type: THOUGHT
parent: topic.GRACE
tags:
- grace
- gospel
- love
- power
- jesuschrist
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SIN",
    alias: "Thought: SIN",
    parent: "topic.GRACE",
    tags: ["grace", "gospel", "love", "power", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN",
    en_title: "SIN",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SIN" AND c.name = "content.SIN"
MERGE (t)-[:HAS_CONTENT {name: "edge.SIN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SIN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->SIN"}]->(child);
```