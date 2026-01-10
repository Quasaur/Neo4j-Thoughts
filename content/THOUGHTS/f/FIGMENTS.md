---
name: thought.FIGMENTS
alias: "Thought: FIGMENTS"
type: THOUGHT
parent: topic.CREATION
tags:
- imagination
- fables
- lessreal
- fictitious
- created
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FIGMENTS",
    alias: "Thought: FIGMENTS",
    parent: "topic.CREATION",
    tags: ["imagination", "fables", "lessreal", "fictitious", "created"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FIGMENTS",
    en_title: "FIGMENTS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FIGMENTS" AND c.name = "content.FIGMENTS"
MERGE (t)-[:HAS_CONTENT {name: "edge.FIGMENTS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.FIGMENTS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->FIGMENTS"}]->(child);
```