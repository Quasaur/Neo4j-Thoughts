---
type: THOUGHT
name: "thought.TREASURE"
alias: "Thought: TREASURE"
parent: "topic.RELIGION"
tags: ["spirituality", "treasure", "wealth", "prosperity", "jesuschrist"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TREASURE",
    alias: "Thought: TREASURE",
    parent: "topic.RELIGION",
    tags: ["spirituality", "treasure", "wealth", "prosperity", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TREASURE",
    en_title: "TREASURE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TREASURE" AND c.name = "content.TREASURE"
MERGE (t)-[:HAS_CONTENT {name: "edge.TREASURE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.TREASURE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->TREASURE"}]->(child);
```