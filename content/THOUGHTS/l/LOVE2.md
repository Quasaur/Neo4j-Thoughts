---
name: thought.LOVE2
alias: "Thought: LOVE 2"
type: THOUGHT
parent: topic.LOVE
tags:
- love
- sacrificial
- give
- selfless
- cause
neo4j: true
ptopic: "[[topic-LOVE]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LOVE2",
    alias: "Thought: LOVE 2",
    parent: "topic.LOVE",
    tags: ["love", "sacrificial", "give", "selfless", "cause"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE2",
    en_title: "LOVE 2",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE2" AND c.name = "content.LOVE2"
MERGE (t)-[:HAS_CONTENT {name: "edge.LOVE2"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.LOVE2"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.LOVE->LOVE2"}]->(child);
```