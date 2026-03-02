---
type: THOUGHT
name: "thought.PERSECUTION"
alias: "Thought: PERSECUTION"
parent: "topic.RELIGION"
tags: ["persecution", "christianity", "original", "authentic", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PERSECUTION",
    alias: "Thought: PERSECUTION",
    parent: "topic.RELIGION",
    tags: ["persecution", "christianity", "original", "authentic", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PERSECUTION",
    ctype: "THOUGHT",
    en_title: "PERSECUTION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERSECUTION" AND c.name = "content.PERSECUTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.PERSECUTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.PERSECUTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->PERSECUTION"}]->(child);
```