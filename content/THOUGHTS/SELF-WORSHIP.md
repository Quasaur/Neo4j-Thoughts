---
name: thought.SELF_WORSHIP
alias: "Thought: SELF WORSHIP"
type: THOUGHT
parent: topic.RELIGION
tags:
- narcissism
- selfworship
- religion
- humanitarian
- evolution
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SELF_WORSHIP",
    alias: "Thought: SELF WORSHIP",
    parent: "topic.RELIGION",
    tags: ["narcissism", "selfworship", "religion", "humanitarian", "evolution"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SELF_WORSHIP",
    en_title: "SELF WORSHIP",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF_WORSHIP" AND c.name = "content.SELF_WORSHIP"
MERGE (t)-[:HAS_CONTENT {name: "edge.SELF_WORSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.SELF_WORSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.RELIGION->SELF_WORSHIP"}]->(child);
```