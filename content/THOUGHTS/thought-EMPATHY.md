---
type: THOUGHT
name: "thought.EMPATHY"
alias: "Thought: EMPATHY"
parent: "topic.LOVE"
tags: ["emptiness", "void", "hunger", "addiction", "spirituality"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
---





```Cypher
CREATE (t:THOUGHT {
    name: "thought.EMPATHY",
    alias: "Thought: EMPATHY",
    parent: "topic.LOVE",
    tags: ["emptiness", "void", "hunger", "addiction", "spirituality"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EMPATHY",
    en_title: "EMPATHY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EMPATHY" AND c.name = "content.EMPATHY"
MERGE (t)-[:HAS_CONTENT {name: "edge.EMPATHY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.EMPATHY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.LOVE->EMPATHY"}]->(child);
```