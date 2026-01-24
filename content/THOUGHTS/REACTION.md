---
name: thought.REACTION
alias: "Thought: REACTION"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- react
- feeling
- flesh
- circumstance
- truth
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.REACTION",
    alias: "Thought: REACTION",
    parent: "topic.PSYCHOLOGY",
    tags: ["react", "feeling", "flesh", "circumstance", "truth"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.REACTION",
    en_title: "REACTION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REACTION" AND c.name = "content.REACTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.REACTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.REACTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->REACTION"}]->(child);
```