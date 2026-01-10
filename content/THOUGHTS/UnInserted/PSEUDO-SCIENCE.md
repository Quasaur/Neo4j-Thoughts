---
name: thought.PSEUDO_SCIENCE
alias: "Thought: PSEUDO-SCIENCE"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- science
- divinity
- pseudoscience
- truth
- deity
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PSEUDO_SCIENCE",
    alias: "Thought: PSEUDO-SCIENCE",
    parent: "topic.COSMOLOGY",
    tags: ["science", "divinity", "pseudoscience", "truth", "deity"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PSEUDO_SCIENCE",
    en_title: "PSEUDO-SCIENCE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PSEUDO_SCIENCE" AND c.name = "content.PSEUDO_SCIENCE"
MERGE (t)-[:HAS_CONTENT {name: "edge.PSEUDO_SCIENCE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.PSEUDO_SCIENCE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->PSEUDO_SCIENCE"}]->(child);
```