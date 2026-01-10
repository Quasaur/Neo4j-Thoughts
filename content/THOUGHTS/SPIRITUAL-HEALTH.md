---
name: thought.SPIRITUAL_HEALTH
alias: "Thought: SPIRITUAL HEALTH"
type: THOUGHT
parent: topic.SPIRITUALITY
tags:
- health
- spiritual
- god
- allpleasing
- character
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SPIRITUAL_HEALTH",
    alias: "Thought: SPIRITUAL HEALTH",
    parent: "topic.SPIRITUALITY",
    tags: ["health", "spiritual", "god", "allpleasing", "character"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPIRITUAL_HEALTH",
    en_title: "SPIRITUAL HEALTH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRITUAL_HEALTH" AND c.name = "content.SPIRITUAL_HEALTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.SPIRITUAL_HEALTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SPIRITUAL_HEALTH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY->SPIRITUAL_HEALTH"}]->(child);
```