---
name: thought.DIFFICULTY
alias: "Thought: DIFFICULTY"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- difficulty
- challenge
- struggle
- humility
- confession
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIFFICULTY",
    alias: "Thought: DIFFICULTY",
    parent: "topic.ATTITUDE",
    tags: ["difficulty", "challenge", "struggle", "humility", "confession"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIFFICULTY",
    en_title: "DIFFICULTY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIFFICULTY" AND c.name = "content.DIFFICULTY"
MERGE (t)-[:HAS_CONTENT {name: "edge.DIFFICULTY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.DIFFICULTY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->DIFFICULTY"}]->(child);
```