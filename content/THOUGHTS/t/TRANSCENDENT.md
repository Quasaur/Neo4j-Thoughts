---
name: thought.TRANSCENDENT
alias: "Thought: TRANSCENDENT"
type: THOUGHT
parent: topic.GRACE
tags:
- pure
- untainted
- deliverance
- glorification
- jesuschrist
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TRANSCENDENT",
    alias: "Thought: TRANSCENDENT",
    parent: "topic.GRACE",
    tags: ["pure", "untainted", "deliverance", "glorification", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRANSCENDENT",
    en_title: "TRANSCENDENT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRANSCENDENT" AND c.name = "content.TRANSCENDENT"
MERGE (t)-[:HAS_CONTENT {name: "edge.TRANSCENDENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TRANSCENDENT"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->TRANSCENDENT"}]->(child);
```