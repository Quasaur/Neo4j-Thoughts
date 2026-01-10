---
name: thought.VALENTINE
alias: "Thought: VALENTINE"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- valentine
- couples
- romance
- relationships
- love
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VALENTINE",
    alias: "Thought: VALENTINE",
    parent: "topic.PSYCHOLOGY",
    tags: ["valentine", "couples", "romance", "relationships", "love"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.VALENTINE",
    en_title: "VALENTINE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VALENTINE" AND c.name = "content.VALENTINE"
MERGE (t)-[:HAS_CONTENT {name: "edge.VALENTINE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.VALENTINE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->VALENTINE"}]->(child);
```