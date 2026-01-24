---
name: thought.NOBODY
alias: "Thought: NOBODY"
type: THOUGHT
parent: topic.EVIL
tags:
- depravity
- religion
- apostasy
- spirituality
- hell
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.NOBODY",
    alias: "Thought: NOBODY",
    parent: "topic.EVIL",
    tags: ["depravity", "religion", "apostasy", "spirituality", "hell"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NOBODY",
    en_title: "NOBODY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOBODY" AND c.name = "content.NOBODY"
MERGE (t)-[:HAS_CONTENT {name: "edge.NOBODY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.NOBODY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->NOBODY"}]->(child);
```