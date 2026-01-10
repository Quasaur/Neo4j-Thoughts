---
name: thought.MODIFIED_GOSPEL
alias: "Thought: MODIFIED GOSPEL"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- gospel
- human
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MODIFIED_GOSPEL",
    alias: "Thought: MODIFIED GOSPEL",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "human"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.MODIFIED_GOSPEL",
    en_title: "MODIFIED GOSPEL",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MODIFIED_GOSPEL" AND c.name = "content.MODIFIED_GOSPEL"
MERGE (t)-[:HAS_CONTENT {name: "edge.MODIFIED_GOSPEL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.MODIFIED_GOSPEL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->MODIFIED_GOSPEL"}]->(child);
```