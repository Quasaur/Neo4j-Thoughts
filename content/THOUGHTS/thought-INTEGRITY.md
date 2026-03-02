---
type: THOUGHT
name: "thought.INTEGRITY"
alias: "Thought: INTEGRITY"
parent: "topic.MORALITY"
tags: ["stand", "True", "integrity", "character", "godliness"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INTEGRITY",
    alias: "Thought: INTEGRITY",
    parent: "topic.MORALITY",
    tags: ["stand", "True", "integrity", "character", "godliness"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INTEGRITY",
    en_title: "INTEGRITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INTEGRITY" AND c.name = "content.INTEGRITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.INTEGRITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.INTEGRITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MORALITY->INTEGRITY"}]->(child);
```