---
name: thought.DARK_MATTER
alias: "Thought: DARK MATTER"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- genesis
- creation
- universe
- waters
- science
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DARK_MATTER",
    alias: "Thought: DARK MATTER",
    parent: "topic.COSMOLOGY",
    tags: ["genesis", "creation", "universe", "waters", "science"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DARK_MATTER",
    en_title: "DARK MATTER",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DARK_MATTER" AND c.name = "content.DARK_MATTER"
MERGE (t)-[:HAS_CONTENT {name: "edge.DARK_MATTER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.DARK_MATTER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->DARK_MATTER"}]->(child);
```