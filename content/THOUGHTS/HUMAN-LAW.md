---
name: thought.HUMAN_LAW
alias: "Thought: HUMAN LAW"
type: THOUGHT
parent: topic.LAW
tags:
- humanity
- god
- accountable
- law
- hope
neo4j: true
ptopic: "[[topic-LAW]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN_LAW",
    alias: "Thought: HUMAN LAW",
    parent: "topic.LAW",
    tags: ["humanity", "god", "accountable", "law", "hope"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMAN_LAW",
    en_title: "HUMAN LAW",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN_LAW" AND c.name = "content.HUMAN_LAW"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMAN_LAW"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LAW" AND child.name = "thought.HUMAN_LAW"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.LAW->HUMAN_LAW"}]->(child);
```