---
name: thought.FAIRNESS
alias: "Thought: FAIRNESS"
type: THOUGHT
parent: topic.JUSTICE
tags:
- justice
- fairness
- mercy
- forgiveness
- compassion
neo4j: true
ptopic: "[[topic-JUSTICE]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FAIRNESS",
    alias: "Thought: FAIRNESS",
    parent: "topic.JUSTICE",
    tags: ["justice", "fairness", "mercy", "forgiveness", "compassion"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FAIRNESS",
    en_title: "FAIRNESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAIRNESS" AND c.name = "content.FAIRNESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.FAIRNESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.FAIRNESS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->FAIRNESS"}]->(child);
```