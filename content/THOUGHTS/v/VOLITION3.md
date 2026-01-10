---
name: thought.VOLITION3
alias: "Thought: THIRD VOLITION"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- freedom
- volition
- freewill
- accountability
- judgment
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VOLITION3",
    alias: "Thought: THIRD VOLITION",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "freewill", "accountability", "judgment"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION3",
    en_title: "THIRD VOLITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION3" AND c.name = "content.VOLITION3"
MERGE (t)-[:HAS_CONTENT {name: "edge.VOLITION3"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION3"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->VOLITION3"}]->(child);
```