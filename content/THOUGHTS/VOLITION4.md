---
name: thought.VOLITION4
alias: "Thought: FOURTH VOLITION"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- freedom
- volition
- freewill
- hell
- damnation
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION4",
    alias: "Thought: FOURTH VOLITION",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "freewill", "hell", "damnation"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION4",
    en_title: "FOURTH VOLITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION4" AND c.name = "content.VOLITION4"
MERGE (t)-[:HAS_CONTENT {name: "edge.VOLITION4"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION4"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->VOLITION4"}]->(child);
```