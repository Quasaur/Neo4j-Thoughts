---
name: thought.ANOTHER_SINNER
alias: "Thought: ANOTHER SINNER"
type: THOUGHT
parent: topic.EVIL
tags:
- satan
- sinner
- inferior
- god
- christ
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ANOTHER_SINNER",
    alias: "Thought: ANOTHER SINNER",
    parent: "topic.EVIL",
    tags: ["satan", "sinner", "inferior", "god", "christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANOTHER_SINNER",
    en_title: "ANOTHER SINNER",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANOTHER_SINNER" AND c.name = "content.ANOTHER_SINNER"
MERGE (t)-[:HAS_CONTENT {name: "edge.ANOTHER_SINNER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.ANOTHER_SINNER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->ANOTHER_SINNER"}]->(child);
```