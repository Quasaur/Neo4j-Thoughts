---
name: thought.DIALOGUE
alias: "Thought: DIALOGUE"
type: THOUGHT
parent: topic.EVIL
tags:
- devil
- ego
- slave
- sin
- tongue
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIALOGUE",
    alias: "Thought: DIALOGUE",
    parent: "topic.EVIL",
    tags: ["devil", "ego", "slave", "sin", "tongue"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DIALOGUE",
    en_title: "DIALOGUE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIALOGUE" AND c.name = "content.DIALOGUE"
MERGE (t)-[:HAS_CONTENT {name: "edge.DIALOGUE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.DIALOGUE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->DIALOGUE"}]->(child);
```