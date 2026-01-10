---
name: thought.ENDING
alias: "Thought: ENDING"
type: THOUGHT
parent: topic.APOCALYPSE
tags:
- ending
- bible
- apocalypse
- judgment
- newjerusalem
neo4j: true
ptopic: "[[topic-APOCALYPSE]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ENDING",
    alias: "Thought: ENDING",
    parent: "topic.APOCALYPSE",
    tags: ["ending", "bible", "apocalypse", "judgment", "newjerusalem"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ENDING",
    en_title: "ENDING",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ENDING" AND c.name = "content.ENDING"
MERGE (t)-[:HAS_CONTENT {name: "edge.ENDING"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.APOCALYPSE" AND child.name = "thought.ENDING"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.APOCALYPSE->ENDING"}]->(child);
```