---
name: thought.PERSEVERANCE
alias: "Thought: PERSEVERANCE"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- persistence
- failure
- quitting
- consequence
- success
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PERSEVERANCE",
    alias: "Thought: PERSEVERANCE",
    parent: "topic.ATTITUDE",
    tags: ["persistence", "failure", "quitting", "consequence", "success"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERSEVERANCE",
    en_title: "PERSEVERANCE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERSEVERANCE" AND c.name = "content.PERSEVERANCE"
MERGE (t)-[:HAS_CONTENT {name: "edge.PERSEVERANCE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PERSEVERANCE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->PERSEVERANCE"}]->(child);
```