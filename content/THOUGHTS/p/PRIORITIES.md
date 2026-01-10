---
name: thought.PRIORITIES
alias: "Thought: PRIORITIES"
type: THOUGHT
parent: topic.WISDOM
tags:
- priorities
- seekyefirst
- divinewill
- god
- faith
neo4j: true
ptopic: "[[topic-WISDOM]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PRIORITIES",
    alias: "Thought: PRIORITIES",
    parent: "topic.WISDOM",
    tags: ["priorities", "seekyefirst", "divinewill", "god", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PRIORITIES",
    en_title: "PRIORITIES",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIORITIES" AND c.name = "content.PRIORITIES"
MERGE (t)-[:HAS_CONTENT {name: "edge.PRIORITIES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.PRIORITIES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.WISDOM->PRIORITIES"}]->(child);
```