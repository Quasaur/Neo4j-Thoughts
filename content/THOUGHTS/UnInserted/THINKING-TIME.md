---
name: thought.THINKING_TIME
alias: "Thought: THINKING TIME"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- thinking
- time
- focus
- priorities
- god
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THINKING_TIME",
    alias: "Thought: THINKING TIME",
    parent: "topic.PSYCHOLOGY",
    tags: ["thinking", "time", "focus", "priorities", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THINKING_TIME",
    en_title: "THINKING TIME",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THINKING_TIME" AND c.name = "content.THINKING_TIME"
MERGE (t)-[:HAS_CONTENT {name: "edge.THINKING_TIME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.THINKING_TIME"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->THINKING_TIME"}]->(child);
```