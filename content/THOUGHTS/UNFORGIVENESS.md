---
name: thought.UNFORGIVENESS
alias: "Thought: UNFORGIVENESS"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- unforgiveness
- hell
- unmerciful
- condemnation
- salvation
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.UNFORGIVENESS",
    alias: "Thought: UNFORGIVENESS",
    parent: "topic.ATTITUDE",
    tags: ["unforgiveness", "hell", "unmerciful", "condemnation", "salvation"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNFORGIVENESS",
    en_title: "UNFORGIVENESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNFORGIVENESS" AND c.name = "content.UNFORGIVENESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.UNFORGIVENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.UNFORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->UNFORGIVENESS"}]->(child);
```