---
name: thought.OBLIVION
alias: "Thought: OBLIVION"
type: THOUGHT
parent: topic.HISTORY
tags:
- apocalypse
- ele
- extinction
- oblivion
- thelastday
neo4j: true
ptopic: "[[topic-HISTORY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.OBLIVION",
    alias: "Thought: OBLIVION",
    parent: "topic.HISTORY",
    tags: ["apocalypse", "ele", "extinction", "oblivion", "thelastday"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OBLIVION",
    en_title: "OBLIVION",
    en_content: "# OBLIVION
The Lord Jesus said that humanity would be driven to the edge of extinction before He returns…and Jesus never lies."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OBLIVION" AND c.name = "content.OBLIVION"
MERGE (t)-[:HAS_CONTENT {name: "edge.OBLIVION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.OBLIVION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HISTORY->OBLIVION"}]->(child);
```