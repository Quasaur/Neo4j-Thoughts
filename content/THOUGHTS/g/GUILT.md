---
name: thought.GUILT
alias: "Thought: GUILT"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- guilt
- expression
- ego
- self
- conscience
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GUILT",
    alias: "Thought: GUILT",
    parent: "topic.PSYCHOLOGY",
    tags: ["guilt", "expression", "ego", "self", "conscience"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GUILT",
    en_title: "GUILT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GUILT" AND c.name = "content.GUILT"
MERGE (t)-[:HAS_CONTENT {name: "edge.GUILT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.GUILT"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->GUILT"}]->(child);
```