---
name: thought.DEATH_ROW
alias: "Thought: DEATH ROW"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- condemnation
- world
- pardon
- receive
- jesus
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEATH_ROW",
    alias: "Thought: DEATH ROW",
    parent: "topic.THE-GOSPEL",
    tags: ["condemnation", "world", "pardon", "receive", "jesus"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEATH_ROW",
    en_title: "DEATH ROW",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEATH_ROW" AND c.name = "content.DEATH_ROW"
MERGE (t)-[:HAS_CONTENT {name: "edge.DEATH_ROW"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.DEATH_ROW"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->DEATH_ROW"}]->(child);
```