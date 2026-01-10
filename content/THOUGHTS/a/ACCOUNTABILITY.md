---
name: thought.ACCOUNTABILITY
alias: "Thought: ACCOUNTABILITY"
type: THOUGHT
parent: topic.HUMANITY
tags:
- god
- lord
- judgment
- accountable
- responsible
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ACCOUNTABILITY",
    alias: "Thought: ACCOUNTABILITY",
    parent: "topic.HUMANITY",
    tags: ["god", "lord", "judgment", "accountable", "responsible"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    en_title: "ACCOUNTABILITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACCOUNTABILITY" AND c.name = "content.ACCOUNTABILITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.ACCOUNTABILITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.ACCOUNTABILITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMANITY->ACCOUNTABILITY"}]->(child);
```