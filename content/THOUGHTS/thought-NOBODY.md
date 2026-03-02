---
type: THOUGHT
name: "thought.NOBODY"
alias: "Thought: NOBODY"
parent: "topic.EVIL"
tags: ["depravity", "religion", "apostasy", "spirituality", "hell"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
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
    ctype: "THOUGHT",
    en_title: "NOBODY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOBODY" AND c.name = "content.NOBODY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.NOBODY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.NOBODY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->NOBODY"}]->(child);
```