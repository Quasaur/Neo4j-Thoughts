---
name: thought.GRATITUDE
alias: "Thought: GRATITUDE"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- thanksgiving
- humility
- decision
- mercy
- dead
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GRATITUDE",
    alias: "Thought: GRATITUDE",
    parent: "topic.ATTITUDE",
    tags: ["thanksgiving", "humility", "decision", "mercy", "dead"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRATITUDE",
    en_title: "GRATITUDE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GRATITUDE" AND c.name = "content.GRATITUDE"
MERGE (t)-[:HAS_CONTENT {name: "edge.GRATITUDE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.GRATITUDE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->GRATITUDE"}]->(child);
```