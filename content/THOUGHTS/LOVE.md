---
name: thought.LOVE
alias: "Thought: LOVE"
type: THOUGHT
parent: topic.LOVE
tags:
- love
- spirit
- attitude
- selfless
- generosity
neo4j: true
ptopic: "[[topic-LOVE]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.LOVE",
    alias: "Thought: LOVE",
    parent: "topic.LOVE",
    tags: ["love", "spirit", "attitude", "selfless", "generosity"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOVE",
    en_title: "LOVE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE" AND c.name = "content.LOVE"
MERGE (t)-[:HAS_CONTENT {name: "edge.LOVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.LOVE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.LOVE->LOVE"}]->(child);
```