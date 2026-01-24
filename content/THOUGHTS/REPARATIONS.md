---
name: thought.REPARATIONS
alias: "Thought: REPARATIONS"
type: THOUGHT
parent: topic.JUSTICE
tags:
- reparations
- slavery
- blackamericans
- compensation
- justice
neo4j: true
ptopic: "[[topic-JUSTICE]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.REPARATIONS",
    alias: "Thought: REPARATIONS",
    parent: "topic.JUSTICE",
    tags: ["reparations", "slavery", "blackamericans", "compensation", "justice"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.REPARATIONS",
    en_title: "REPARATIONS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REPARATIONS" AND c.name = "content.REPARATIONS"
MERGE (t)-[:HAS_CONTENT {name: "edge.REPARATIONS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.REPARATIONS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->REPARATIONS"}]->(child);
```