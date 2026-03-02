---
type: THOUGHT
name: "thought.TRANSCENDENT"
alias: "Thought: TRANSCENDENT"
parent: "topic.GRACE"
tags: ["pure", "untainted", "deliverance", "glorification", "jesus_christ"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TRANSCENDENT",
    alias: "Thought: TRANSCENDENT",
    parent: "topic.GRACE",
    tags: ["pure", "untainted", "deliverance", "glorification", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRANSCENDENT",
    ctype: "THOUGHT",
    en_title: "TRANSCENDENT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRANSCENDENT" AND c.name = "content.TRANSCENDENT"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.TRANSCENDENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TRANSCENDENT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->TRANSCENDENT"}]->(child);
```