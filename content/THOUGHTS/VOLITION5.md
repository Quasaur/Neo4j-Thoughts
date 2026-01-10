---
name: thought.VOLITION5
alias: "Thought: FIFTH VOLITION"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- freedom
- volition
- freewill
- ignorance
- flatearth
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION5",
    alias: "Thought: FIFTH VOLITION",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "freewill", "ignorance", "flatearth"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION5",
    en_title: "FIFTH VOLITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION5" AND c.name = "content.VOLITION5"
MERGE (t)-[:HAS_CONTENT {name: "edge.VOLITION5"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION5"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->VOLITION5"}]->(child);
```