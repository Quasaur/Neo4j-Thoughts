---
name: thought.PERCEPTION
alias: "Thought: PERCEPTION"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- attitude
- seeing
- observing
- perception
- selfimprovement
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PERCEPTION",
    alias: "Thought: PERCEPTION",
    parent: "topic.ATTITUDE",
    tags: ["attitude", "seeing", "observing", "perception", "selfimprovement"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERCEPTION",
    en_title: "PERCEPTION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERCEPTION" AND c.name = "content.PERCEPTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.PERCEPTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PERCEPTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->PERCEPTION"}]->(child);
```