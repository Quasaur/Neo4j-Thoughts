---
name: thought.THE_QUICK_AND_THE_DEAD
alias: "Thought: THE QUICK AND THE DEAD"
type: THOUGHT
parent: topic.SPIRITUALITY
tags:
- eternallife
- immortality
- spirituality
- god
- jesuschrist
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_QUICK_AND_THE_DEAD",
    alias: "Thought: THE QUICK AND THE DEAD",
    parent: "topic.SPIRITUALITY",
    tags: ["eternallife", "immortality", "spirituality", "god", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE_QUICK_AND_THE_DEAD",
    en_title: "THE QUICK AND THE DEAD",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_QUICK_AND_THE_DEAD" AND c.name = "content.THE_QUICK_AND_THE_DEAD"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_QUICK_AND_THE_DEAD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.THE_QUICK_AND_THE_DEAD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY->THE_QUICK_AND_THE_DEAD"}]->(child);
```