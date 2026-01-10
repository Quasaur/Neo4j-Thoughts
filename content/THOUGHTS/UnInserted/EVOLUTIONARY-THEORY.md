---
name: thought.EVOLUTIONARY_THEORY
alias: "Thought: EVOLUTIONARY THEORY"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- evolution
- theory
- unlawful
- unproven
- unscientific
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EVOLUTIONARY_THEORY",
    alias: "Thought: EVOLUTIONARY THEORY",
    parent: "topic.COSMOLOGY",
    tags: ["evolution", "theory", "unlawful", "unproven", "unscientific"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTIONARY_THEORY",
    en_title: "EVOLUTIONARY THEORY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVOLUTIONARY_THEORY" AND c.name = "content.EVOLUTIONARY_THEORY"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVOLUTIONARY_THEORY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.EVOLUTIONARY_THEORY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->EVOLUTIONARY_THEORY"}]->(child);
```