---
name: thought.WILL_VS_WILL
alias: "Thought: WILL VS WILL"
type: THOUGHT
parent: topic.FAITHFULNESS
tags:
- selfdenial
- humility
- seekyefirst
- god
- divinewill
neo4j: true
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WILL_VS_WILL",
    alias: "Thought: WILL VS WILL",
    parent: "topic.FAITHFULNESS",
    tags: ["selfdenial", "humility", "seekyefirst", "god", "divinewill"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WILL_VS_WILL",
    en_title: "WILL VS WILL",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WILL_VS_WILL" AND c.name = "content.WILL_VS_WILL"
MERGE (t)-[:HAS_CONTENT {name: "edge.WILL_VS_WILL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.WILL_VS_WILL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITHFULNESS->WILL_VS_WILL"}]->(child);
```