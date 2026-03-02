---
type: THOUGHT
name: "thought.SENTIENCE"
alias: "Thought: SENTIENCE"
parent: "topic.SPIRITS"
tags: ["spirits", "sentience", "god", "selfaware", "iam"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SENTIENCE",
    alias: "Thought: SENTIENCE",
    parent: "topic.SPIRITS",
    tags: ["spirits", "sentience", "god", "selfaware", "iam"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SENTIENCE",
    ctype: "THOUGHT",
    en_title: "SENTIENCE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SENTIENCE" AND c.name = "content.SENTIENCE"
MERGE (t)-[:HAS_CONTENT {name: "edge.SENTIENCE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITS" AND child.name = "thought.SENTIENCE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITS->SENTIENCE"}]->(child);
```