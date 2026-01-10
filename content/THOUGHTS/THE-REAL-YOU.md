---
name: thought.THE_REAL_YOU
alias: "Thought: THE REAL YOU"
type: THOUGHT
parent: topic.GRACE
tags:
- identity
- selfimage
- imageofgod
- christian
- jesuschrist
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_REAL_YOU",
    alias: "Thought: THE REAL YOU",
    parent: "topic.GRACE",
    tags: ["identity", "selfimage", "imageofgod", "christian", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THE_REAL_YOU",
    en_title: "THE REAL YOU",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_REAL_YOU" AND c.name = "content.THE_REAL_YOU"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_REAL_YOU"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.THE_REAL_YOU"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->THE_REAL_YOU"}]->(child);
```