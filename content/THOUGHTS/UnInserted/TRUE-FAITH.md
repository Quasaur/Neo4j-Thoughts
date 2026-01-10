---
name: thought.TRUE_FAITH
alias: "Thought: TRUE FAITH"
type: THOUGHT
parent: topic.FAITH
tags:
- faith
- trust
- confidence
- obedience
- submission
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TRUE_FAITH",
    alias: "Thought: TRUE FAITH",
    parent: "topic.FAITH",
    tags: ["faith", "trust", "confidence", "obedience", "submission"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TRUE_FAITH",
    en_title: "TRUE FAITH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUE_FAITH" AND c.name = "content.TRUE_FAITH"
MERGE (t)-[:HAS_CONTENT {name: "edge.TRUE_FAITH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.TRUE_FAITH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITH->TRUE_FAITH"}]->(child);
```