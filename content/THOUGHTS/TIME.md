---
name: thought.TIME
alias: "Thought: TIME"
type: THOUGHT
parent: topic.JUSTICE
tags:
- spirituality
- damnation
- soul
- lakeoffire
- judgment
neo4j: true
ptopic: "[[topic-JUSTICE]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TIME",
    alias: "Thought: TIME",
    parent: "topic.JUSTICE",
    tags: ["spirituality", "damnation", "soul", "lakeoffire", "judgment"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.TIME",
    en_title: "TIME",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TIME" AND c.name = "content.TIME"
MERGE (t)-[:HAS_CONTENT {name: "edge.TIME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.TIME"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->TIME"}]->(child);
```