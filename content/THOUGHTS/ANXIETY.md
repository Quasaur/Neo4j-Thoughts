---
name: thought.ANXIETY
alias: "Thought: ANXIETY"
type: THOUGHT
parent: topic.FAITH
tags:
- peace
- faith
- carefree
- confident
- trust
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ANXIETY",
    alias: "Thought: ANXIETY",
    parent: "topic.FAITH",
    tags: ["peace", "faith", "carefree", "confident", "trust"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANXIETY",
    en_title: "ANXIETY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANXIETY" AND c.name = "content.ANXIETY"
MERGE (t)-[:HAS_CONTENT {name: "edge.ANXIETY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.ANXIETY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITH->ANXIETY"}]->(child);
```