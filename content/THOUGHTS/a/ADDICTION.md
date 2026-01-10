---
name: thought.ADDICTION
alias: "Thought: ADDICTION"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- sanctification
- addiction
- flesh
- thecross
- jesuschrist
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ADDICTION",
    alias: "Thought: ADDICTION",
    parent: "topic.PSYCHOLOGY",
    tags: ["sanctification", "addiction", "flesh", "thecross", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ADDICTION",
    en_title: "ADDICTION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ADDICTION" AND c.name = "content.ADDICTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.ADDICTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ADDICTION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->ADDICTION"}]->(child);
```