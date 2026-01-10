---
name: thought.SCIENCE_CONSPIRACY
alias: "Thought: SCIENCE CONSPIRACY"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- science
- cosmology
- geocentricity
- michelson
- creationism
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SCIENCE_CONSPIRACY",
    alias: "Thought: SCIENCE CONSPIRACY",
    parent: "topic.COSMOLOGY",
    tags: ["science", "cosmology", "geocentricity", "michelson", "creationism"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SCIENCE_CONSPIRACY",
    en_title: "SCIENCE CONSPIRACY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SCIENCE_CONSPIRACY" AND c.name = "content.SCIENCE_CONSPIRACY"
MERGE (t)-[:HAS_CONTENT {name: "edge.SCIENCE_CONSPIRACY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.SCIENCE_CONSPIRACY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->SCIENCE_CONSPIRACY"}]->(child);
```