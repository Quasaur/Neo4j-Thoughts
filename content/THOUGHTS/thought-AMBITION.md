---
type: THOUGHT
name: "thought.AMBITION"
alias: "Thought: AMBITION"
parent: "topic.THE-GOSPEL"
tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.AMBITION",
    alias: "Thought: AMBITION",
    parent: "topic.THE-GOSPEL",
    tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.AMBITION",
    ctype: "THOUGHT",
    en_title: "AMBITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMBITION" AND c.name = "content.AMBITION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.AMBITION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.AMBITION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->AMBITION"}]->(child);
```