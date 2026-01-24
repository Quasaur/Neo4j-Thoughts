---
name: thought.INSATIABLE
alias: "Thought: INSATIABLE"
type: THOUGHT
parent: topic.EVIL
tags:
- flesh
- carnal
- animalistic
- impetuous
- instinctual
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INSATIABLE",
    alias: "Thought: INSATIABLE",
    parent: "topic.EVIL",
    tags: ["flesh", "carnal", "animalistic", "impetuous", "instinctual"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INSATIABLE",
    en_title: "INSATIABLE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INSATIABLE" AND c.name = "content.INSATIABLE"
MERGE (t)-[:HAS_CONTENT {name: "edge.INSATIABLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.INSATIABLE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->INSATIABLE"}]->(child);
```