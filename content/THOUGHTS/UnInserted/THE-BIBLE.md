---
name: thought.THE_BIBLE
alias: "Thought: THE BIBLE"
type: THOUGHT
parent: topic.HISTORY
tags:
- apocalypse
- bible
- rock
- spirituality
- delusion
neo4j: true
ptopic: "[[topic-HISTORY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_BIBLE",
    alias: "Thought: THE BIBLE",
    parent: "topic.HISTORY",
    tags: ["apocalypse", "bible", "rock", "spirituality", "delusion"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THE_BIBLE",
    en_title: "THE BIBLE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_BIBLE" AND c.name = "content.THE_BIBLE"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_BIBLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.THE_BIBLE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HISTORY->THE_BIBLE"}]->(child);
```