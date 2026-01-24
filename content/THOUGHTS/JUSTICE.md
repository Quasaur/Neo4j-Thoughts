---
name: thought.JUSTICE
alias: "Thought: Justice"
type: THOUGHT
parent: topic.JUSTICE
tags:
- justice
- spirituality
- forgiveness
- gospel
- fair
neo4j: true
ptopic: "[[topic-JUSTICE]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.JUSTICE",
    alias: "Thought: Justice",
    parent: "topic.JUSTICE",
    tags: ["justice", "spirituality", "forgiveness", "gospel", "fair"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.JUSTICE",
    en_title: "Justice",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.JUSTICE" AND c.name = "content.JUSTICE"
MERGE (t)-[:HAS_CONTENT {name: "edge.JUSTICE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.JUSTICE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->JUSTICE"}]->(child);
```