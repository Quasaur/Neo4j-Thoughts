---
type: THOUGHT
name: "thought.FORGIVENESS"
alias: "Thought: FORGIVENESS"
parent: "topic.MERCY"
tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesus_christ"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FORGIVENESS",
    alias: "Thought: FORGIVENESS",
    parent: "topic.MERCY",
    tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesus_christ"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FORGIVENESS",
    ctype: "THOUGHT",
    en_title: "FORGIVENESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FORGIVENESS" AND c.name = "content.FORGIVENESS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FORGIVENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.FORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MERCY->FORGIVENESS"}]->(child);
```