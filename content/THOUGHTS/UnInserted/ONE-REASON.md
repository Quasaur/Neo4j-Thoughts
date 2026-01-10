---
name: thought.ONE_REASON
alias: "Thought: ONE REASON"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- apocalypse
- lakeoffire
- pride
- judgment
- jesuschrist
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ONE_REASON",
    alias: "Thought: ONE REASON",
    parent: "topic.ATTITUDE",
    tags: ["apocalypse", "lakeoffire", "pride", "judgment", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ONE_REASON",
    en_title: "ONE REASON",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ONE_REASON" AND c.name = "content.ONE_REASON"
MERGE (t)-[:HAS_CONTENT {name: "edge.ONE_REASON"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ONE_REASON"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->ONE_REASON"}]->(child);
```