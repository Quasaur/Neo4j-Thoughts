---
type: THOUGHT
name: "thought.HAPPINESS"
alias: "Thought: HAPPINESS"
parent: "topic.ATTITUDE"
tags: ["happy", "fulfilled", "satisfied", "delighted", "content"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HAPPINESS",
    alias: "Thought: HAPPINESS",
    parent: "topic.ATTITUDE",
    tags: ["happy", "fulfilled", "satisfied", "delighted", "content"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HAPPINESS",
    ctype: "THOUGHT",
    en_title: "HAPPINESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPINESS" AND c.name = "content.HAPPINESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.HAPPINESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HAPPINESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->HAPPINESS"}]->(child);
```